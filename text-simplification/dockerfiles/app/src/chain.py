
#Basic imports
import logging
import os
import re
import requests

#Other app imports
from prompts import (
    PROMPT_W_EXAMPLES,
    PROMPT_WITHOUT_EXAMPLES,
    PROMPT_END,
    PROMPT_ONLY_EXAMPLES,
    PROMPT_EXAMPLES_ONE_INSTRUCTION,
)


def call_api(prompt):
    url = "http://10.10.78.13:8000/v1/completions"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama3-8b-instruct",
        "prompt": prompt,
        "max_tokens": 300,
        "temperature": 0.5
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    return response.json()['choices'][0]['text']

def format_response(llm_response:str)->str:
    # it's a known issue that mixtral generates lists and/or numbered paragraphs, this removes them
    llm_response = llm_response.replace(". ", ".\n")
    llm_response = re.sub(r"^\d\.\n|\n\d\.\n|\n\d\d\.\n|\n *[-*] *\w", "\n", llm_response).strip()
    return llm_response

def execute_chain(task:str, input:dict, format:bool=True)-> str:
    """Executes a chain for a given task"""

    input_text = f"""Original input text: {input}"""
    chain = PROMPT_W_EXAMPLES + input_text + PROMPT_END
    llm_response = call_api(chain)

    logging.info(f'PromptTemplate:\n{chain}\nInput:\n{input}\nOutput:\n{llm_response}')

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
