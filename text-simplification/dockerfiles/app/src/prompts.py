SIMPLE_ENGLISH_PROMPT_MIXTRAL_0SHOT = {
    "prompt_text": """[INST] Re-write the input text into a Simple English text.
Simple English is a version of the English language that aims to present information in a way that is easy to understand for individuals with learning disabilities. 
Texts in Simple English must follow these requirements:
- Each sentence expresses only one idea. 
- Do not enumerate sentences or paragraphs.
- The subject of each sentence must be explicit. Do not use pronouns as subjects.
- Use short sentences and simple vocabulary. Be repetitive if necessary.
- Do not use negations.
- Do not use too many numbers or mathematical denominations. If there is no choice but to insert a number, always use digits.
- Do not use confusing metaphors or complex comparisons.
- Be clear, concise, direct and coherent.
- Do not use technical terms, abbreviations and initials.
- Avoid unnecessary ideas, words, sentences or phrases.
Input text:
{text}
Rewritten text: [/INST] """,
    "variables": ["text"],
}

EVAL_PROMPT_MIXTRAL = {
    "prompt_text": """[INST] Assign a score (0-10 points) to the translation of the following text from English to Simple English.
Simple English is a version of the English language that aims to present information in a way that is easy to understand for individuals with limited proficiency in English or those who are learning the language. 
Texts in Simple English must follow these 10 requirements. Assing 1 point per requirement met.
1. Each sentence expresses only one idea.
2. The subject of each sentence must be explicit. Do not use pronouns as subjects.
3. Use short sentences and simple vocabulary. Use simple and direct language.
4. Do not use negations.
5. Do not use too many numbers or mathematical denominations. If there is no choice but to insert a number, always use digits.
6. Do not use confusing metaphors or complex comparisons.
7. Be clear, concise and direct.
8. Do not use technical terms, abbreviations and initials.
9. Text should be clear and coherent.
10. Avoid unnecessary ideas, words, sentences or phrases.
Original text (English):
{input_text}
Rewritten text (Simple English):
{ouput_text}
Score: [/INST] """,
    "variables": ["input_text", "output_text"],
}

SIMPLE_CONCEPT_PROMPT_MIXTRAL_0SHOT = {
    "prompt_text": """[INST] Explain the following concept in Simple English within the given context. 
Simple English is a version of the English language that aims to present information in a way that is easy to understand for individuals with learning disabilities. 
Texts in Simple English must follow these requirements:
- Each sentence expresses only one idea. 
- Do not enumerate sentences or paragraphs.
- The subject of each sentence must be explicit. Do not use pronouns as subjects.
- Use short sentences and simple vocabulary. Be repetitive if necessary.
- Do not use negations.
- Do not use too many numbers or mathematical denominations. If there is no choice but to insert a number, always use digits.
- Do not use confusing metaphors or complex comparisons.
- Be clear, concise, direct and coherent.
- Do not use technical terms, abbreviations and initials.
- Avoid unnecessary ideas, words, sentences or phrases.
Context: {answer_text}
Concept to explain: {concept}
Explanation: [/INST] """,
    "variables": ["answer_text", "concept"],
}

SIMPLE_ENGLISH_PROMPT = {
    "prompt_text": """Simple English is a version of the English language that aims to present information in a way that is easy to understand for individuals with limited proficiency in English or those who are learning the language. Text in on Simple English are written with shorter sentences, simpler vocabulary, and a straightforward structure, making the content more accessible to a diverse audience. The primary goal is to provide clear and concise information on a wide range of topics, catering to readers who may find the regular English more challenging to comprehend. The simplicity of language in Simple English is intended to facilitate learning and understanding for a broad audience.
Instruction: Translate the input text to Simple English. Make sure it complies with the following requirements:
- Express only one idea per sentence.
- Each sentence should not start with a list number.
- One sentence per line.
- Make sure the subject of each sentence it is explicit. Do not use pronouns as subjects.
- Use short sentences and simple language
- Avoid negative sentences
- Avoid using too many numbers or mathematical denominations. If there is no choice but to insert a number, always use digits.
- Do not use confusing metaphors or comparisons.
- Use only one message per sentence.
- Be clear, concise and direct.
- Use simple and direct language.
- Avoid technical terms, abbreviations and initials.
- The content must follow a clear and coherent order.
- All unnecessary ideas, words, sentences or phrases should be avoided or deleted.
- Explain in a simple way by means of a vocabulary, if necessary, those words that are words that are considered somewhat difficult to understand.
If the input text is already in Simple English, say "The input text is already in Simple English." and nothing else.
Input text:
{text}
Output text: """,
    "variables": ["text"],
}

SIMPLE_CONCEPT_PROMPT = {
    "prompt_text": """Simple English is a version of the English language that aims to present information in a way that is easy to understand for individuals with limited proficiency in English or those who are learning the language. Text in on Simple English are written with shorter sentences, simpler vocabulary, and a straightforward structure, making the content more accessible to a diverse audience. The primary goal is to provide clear and concise information on a wide range of topics, catering to readers who may find the regular English more challenging to comprehend. The simplicity of language in Simple English is intended to facilitate learning and understanding for a broad audience.
Instruction: Define the input concept in Simple English within the given input context. Make sure it complies with the following requirements:
- Express only one idea per sentence.
- Make sure the subject of each sentence it is explicit. Do not use pronouns as subjects.
- Use short sentences and simple language
- Avoid negative sentences
- Avoid using too many numbers or mathematical denominations. If there is no choice but to insert a number, always use digits.
- Do not use confusing metaphors or comparisons.
- Use only one message per sentence.
- Be clear, concise and direct.
- Use simple and direct language.
- Avoid technical terms, abbreviations and initials.
- The content must follow a clear and coherent order.
- All unnecessary ideas, words, sentences or phrases should be avoided or deleted.
- Explain in a simple way by means of a vocabulary, if necessary, those words that are words that are considered somewhat difficult to understand.
Input context: {answer_text}
Input concept: {concept}
Output:""",
    "variables": ["answer_text", "concept"],
}


SIMPLE_ENGLISH_PROMPT_MIXTRAL_2SHOT = {
    'prompt_text' :
"""[INST] Rewrite the input text into a simpler and easier to understand ouput text. This output text is meant for people with learning and cognitive disabilities. Follow these two examples:
 
Original input text: The capybara or greater capybara (Hydrochoerus hydrochaeris) is a giant cavy rodent native to South America. It is the largest living rodent and a member of the genus Hydrochoerus. The only other extant member is the lesser capybara (Hydrochoerus isthmius). Its close relatives include guinea pigs and rock cavies, and it is more distantly related to the agouti, the chinchilla, and the nutria. The capybara inhabits savannas and dense forests, and lives near bodies of water. It is a highly social species and can be found in groups as large as 100 individuals, but usually live in groups of 10-20 individuals. The capybara is hunted for its meat and hide and also for grease from its thick fatty skin.
Simpler output text: The capybara is a big rodent.\nThe capybara lives in South America.\nThe capybara is the biggest rodent alive.\nIt lives in South America.\nCapybaras are part of the Hydrochoerus family.\nOther similar animals are: guinea pigs, rock cavies, chinchillas and otters.\nThe capybara lives in savannas and rainforests.\nThe capybara lives near places with water.\nThe capybara is a social animal.\nThe capybara lives in groups.\nHumans hunt capybaras because of their meat and their fat."

Original input text: The requirements for the front line of air traffic control are a poor match for AI's capabilities. People expect air traffic to continue to be the safest complex, high-technology system ever.It achieves this standard by adhering to procedures when practical, which is something AI can do, and by adapting and exercising good judgment whenever something unplanned occurs or a new operation is implemented - a notable weakness of today's AI. Indeed, it is when conditions are the worst - when controllers figure out how to handle aircraft with severe problems, airport crises or widespread airspace closures due to security concerns or infrastructure failures - that controllers' contributions to safety are the greatest.
Simpler output text: Air traffic control needs skills that Artificial Intelligence does not have.\nAir traffic systems are difficult technology systems.\nPeople think air traffic systems are very safe systems.\n Air traffic systems can take good decisions in unexpected situations.\nAir traffic systems adapt to changes.\nArtificial Intelligence adapts worse than air traffic systems.\nAir controllers help mantain security and safety specially when there are problems.

Input text:\n{text}
Output text: [/INST]""",
    'variables' : ['text']
}

SIMPLE_CONCEPT_PROMPT_MIXTRAL_2SHOT = {
     'prompt_text' :
"""[INST] Define the input concept taking into account the given input context. Define it in simpler and easier to understand way. This definition is meant for people with learning and cognitive disabilities. Follow these two examples:
 
Input concept: Savanna
Simple definition: \nThe Savanna is a type of ecosystem.\nThe Savanna is found in tropical regions.\nThere is grass and some trees in the Savanna.\nSavannas typically have warm temperatures.\nSavannas have both wet and dry seasons.\nLots of animals live in the Savannas.\nAnimales like zebras and lions live in the Savanna.
 
Input concept: Air Controller
Simple definition: \nAn air controller is a person.\nAn air controller helps guide airplanes safely.\nThey give instructions to airplanes in the sky and at airports.\nAir controllers make sure: planes take off and planes land.\nThey make sure planes fly in the right direction without bumping into each other.

Input context:\n{answer_text}
Input concept:\n{concept}
Simple definition: [/INST]""",
    'variables' : ['answer_text', 'concept']
}


SIMPLE_ENGLISH_PROMPT_MIXTRAL_FEWSHOT = {
'prompt_text' :
"""Instruction: Rewrite the input text into a simpler and easier to understand ouput text. This output text is meant for people with learning and cognitive disabilities. Follow these two examples:
 
Original input text: The capybara or greater capybara (Hydrochoerus hydrochaeris) is a giant cavy rodent native to South America. It is the largest living rodent and a member of the genus Hydrochoerus. The only other extant member is the lesser capybara (Hydrochoerus isthmius). Its close relatives include guinea pigs and rock cavies, and it is more distantly related to the agouti, the chinchilla, and the nutria. The capybara inhabits savannas and dense forests, and lives near bodies of water. It is a highly social species and can be found in groups as large as 100 individuals, but usually live in groups of 10–20 individuals. The capybara is hunted for its meat and hide and also for grease from its thick fatty skin.
Simpler output text: The capybara is a big rodent.\n The capybara lives in South America.\n The capybara is the biggest rodent alive.\n It lives in South America.\n Capybaras are part of the Hydrochoerus family.\n Other similar animals are: guinea pigs, rock cavies, chinchillas and otters.\n The capybara lives in savannas and rainforests.\n The capybara lives near places with water.\n The capybara is a social animal.\n The capybara lives in groups.\n Humans hunt capybaras because of their meat and their fat."
 
Original input text: The requirements for the front line of air traffic control are a poor match for AI’s capabilities. People expect air traffic to continue to be the safest complex, high-technology system ever. It achieves this standard by adhering to procedures when practical, which is something AI can do, and by adapting and exercising good judgment whenever something unplanned occurs or a new operation is implemented – a notable weakness of today’s AI. Indeed, it is when conditions are the worst – when controllers figure out how to handle aircraft with severe problems, airport crises or widespread airspace closures due to security concerns or infrastructure failures – that controllers’ contributions to safety are the greatest.
Simpler output text: Air traffic control needs skills that Artificial Intelligence does not have.\n Air traffic systems are difficult technology systems.\n People think air traffic systems are very safe systems.\n Air traffic systems can take good decisions in unexpected situations.\n Air traffic systems adapt to changes.\n Artificial Intelligence adapts worse than air traffic systems.\n Air controllers help mantain security and safety specially when there are problems.
 
Input text:
{text}
Output text: """,
    'variables' : ['text']
}

SIMPLE_CONCEPT_PROMPT_MIXTRAL_FEWSHOT = {
'prompt_text' :
"""Instruction: Define the input concept taking into account the given input context. Define it in simpler and easier to understand way. This definition is meant for people with learning and cognitive disabilities. Follow these two examples:
 
Input concept: Savanna
Simple output Definition: The Savanna is a type of ecosystem.\n The Savanna is found in tropical regions.\n There is grass and some trees in the Savanna.\n Savannas typically have warm temperatures.\n Savannas have both wet and dry seasons.\n Lots of animals live in the Savannas.\n Animales like zebras and lions live in the Savanna.
 
Input concept: Air Controller
Simple output Definition: An air controller is a person.\n An air controller helps guide airplanes safely.\n They give instructions to airplanes in the sky and at airports.\n  Air controllers make sure: planes take off and planes land.\n They make sure planes fly in the right direction without bumping into each other.\n
Input context: {answer_text}
Input concept: {concept}
Output:""",
    'variables' : ['answer_text', 'concept']
}

all_prompts = {
    'VertexAI': {
        'simplify': SIMPLE_ENGLISH_PROMPT, 
        'explain': SIMPLE_CONCEPT_PROMPT,
        'evaluate': EVAL_PROMPT_MIXTRAL
        },
    'CTC_Madrid': {
        'simplify': SIMPLE_ENGLISH_PROMPT_MIXTRAL_FEWSHOT,
        'explain': SIMPLE_CONCEPT_PROMPT_MIXTRAL_FEWSHOT,
        'evaluate': EVAL_PROMPT_MIXTRAL
        },
    'CTC_Boeblingen': {
        'simplify': SIMPLE_ENGLISH_PROMPT_MIXTRAL_FEWSHOT,
        'explain': SIMPLE_CONCEPT_PROMPT_MIXTRAL_FEWSHOT,
        'evaluate': EVAL_PROMPT_MIXTRAL
        },
}
