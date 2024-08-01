
#Basic imports
import logging
import os
import re

#Langchain imports
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
#-> for future from langchain_nvidia_ai_endpoints import ChatNVIDIA

#Other app imports
from prompts import all_prompts


#-> remove following later
#Config for the Mixtral Model we use in the beginning in the CTC in Madrid
mixtral_config = {
    "endpoint_url":"http://10.10.78.11:8081/",
    "max_new_tokens":512,
    "top_k":10,
    "top_p":0.95,
    "typical_p":0.95,
    "temperature":0.01,
}

def format_response(llm_response:str)->str:
    # it's a known issue that mixtral generates lists and/or numbered paragraphs, this removes them
    llm_response = llm_response.replace(". ", ".\n")
    llm_response = re.sub(r"^\d\.\n|\n\d\.\n|\n\d\d\.\n|\n *[-*] *\w", "\n", llm_response).strip()
    return llm_response

def execute_chain(task:str, input:dict, format:bool=True)-> str:
    """Executes a chain for a given task"""
    provider = "CTC_Madrid"
    logging.info(f'ModelType set. Using {provider}.')

    if provider == "CTC_Madrid":
        llm = HuggingFaceEndpoint(**mixtral_config)
    #-> for future     elif provider == "NIM_CTC_Madrid":
    #-> for future         llm = ChatNVIDIA(model="mistral_7b")

    else:
        raise Exception('Missing `ModelType` configuration setting. Please set the enviornment variable `ModelType`.\n export ModelType=\'CTC_Madrid\'')

    #Create prompt Template https://python.langchain.com/v0.2/docs/how_to/sequence/#related
    prompt_template = ChatPromptTemplate.from_template(
        all_prompts[provider][task]["prompt_text"]
    )
    chain = prompt_template | llm | StrOutputParser()
    llm_response = chain.invoke(input)  #["text"].strip()

    logging.info(f'PromptTemplate:\n{prompt_template}\nInput:\n{input}\nOutput:\n{llm_response}')

    if format:
        llm_response = format_response(llm_response)
        logging.info(f'Formatted Response.\nOutput:\n{llm_response}')

    return llm_response

def simplify_text(original_text: str)-> str:
    #Check if the input text has a specific length so simplification makes sense: 
    if len(original_text) < 50:
        return "Please input a longer text. Minimun 50 characters."

    return execute_chain('simplify',{'text':original_text})


def explain_term(answer_text: str, concept: str)-> str:

    llm_response = execute_chain('explain',{"answer_text": answer_text, "concept": concept})
    
    # Split the response into lines
    response_lines = llm_response.split('\n')
 
    # Ensure the response has at most 10 lines
    if len(response_lines) > 10:
        llm_response = '\n'.join(response_lines[:10])
        
    return llm_response