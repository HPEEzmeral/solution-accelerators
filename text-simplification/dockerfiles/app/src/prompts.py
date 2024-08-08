PROMPT_W_EXAMPLES = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nRewrite the input text into a simpler and easier to understand ouput text. This output text is meant for people with learning and cognitive disabilities. Please do so by:

- Each sentence expresses only one idea.
- Do not enumerate sentences or paragraphs.
- Do not start sentences with pronouns. Do not use "I", "you", "he" "she" "we" or "they"
- The subject of each sentence must be explicit (full name)
- Do not use pronouns as subjects. Do not use "I", "you", "he" "she" "we" or "they"
- Each sentence must explicitly mention the noun that performs the action.
- Use short sentences and simple vocabulary. 
- Be repetitive if necessary.
- Do not use negations.
- Do not use too many numbers or mathematical denominations. If there is no choice but to insert a number, always use digits.
- Do not use confusing metaphors or complex comparisons.
- Do not use technical terms, abbreviations and initials.

Follow these two examples:
Original input text: The capybara or greater capybara (Hydrochoerus hydrochaeris) is a giant cavy rodent native to South America. It is the largest living rodent and a member of the genus Hydrochoerus. The only other extant member is the lesser capybara (Hydrochoerus isthmius). Its close relatives include guinea pigs and rock cavies, and it is more distantly related to the agouti, the chinchilla, and the nutria. The capybara inhabits savannas and dense forests, and lives near bodies of water. It is a highly social species and can be found in groups as large as 100 individuals, but usually live in groups of 10–20 individuals. The capybara is hunted for its meat and hide and also for grease from its thick fatty skin.
Simpler output text: The capybara is a big rodent.\n The capybara lives in South America.\n The capybara is the biggest rodent alive.\n The capybara lives in South America.\n Capybaras are part of the Hydrochoerus family.\n Other similar animals are: guinea pigs, rock cavies, chinchillas and otters.\n The capybara lives in savannas and rainforests.\n The capybara lives near places with water.\n The capybara is a social animal.\n The capybara lives in groups.\n Humans hunt capybaras because of their meat and their fat."
Original input text: The requirements for the front line of air traffic control are a poor match for AI’s capabilities. People expect air traffic to continue to be the safest complex, high-technology system ever. It achieves this standard by adhering to procedures when practical, which is something AI can do, and by adapting and exercising good judgment whenever something unplanned occurs or a new operation is implemented – a notable weakness of today’s AI. Indeed, it is when conditions are the worst – when controllers figure out how to handle aircraft with severe problems, airport crises or widespread airspace closures due to security concerns or infrastructure failures – that controllers’ contributions to safety are the greatest.
Simpler output text: Air traffic control needs skills that Artificial Intelligence does not have.\n Air traffic systems are difficult technology systems.\n People think air traffic systems are very safe systems.\n Air traffic systems can take good decisions in unexpected situations.\n Air traffic systems adapt to changes.\n Artificial Intelligence adapts worse than air traffic systems.\n Air controllers help mantain security and safety specially when there are problems.<|eot_id|><|start_header_id|>user<|end_header_id|>
"""

PROMPT_WITHOUT_EXAMPLES = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nRewrite the input text into a simpler and easier to understand ouput text. This output text is meant for people with learning and cognitive disabilities. Please do so by:

- Each sentence expresses only one idea.
- Do not enumerate sentences or paragraphs.
- The subject of each sentence must be explicit (full name). Do not use pronouns as subjects (no I, you, he , she or they).
- Use short sentences and simple vocabulary. Be repetitive if necessary.
- Do not use negations.
- Do not use too many numbers or mathematical denominations. If there is no choice but to insert a number, always use digits.
- Do not use confusing metaphors or complex comparisons.
- Be clear, concise, direct and coherent.
- Do not use technical terms, abbreviations and initials.
- Avoid unnecessary ideas, words, sentences or phrases.
"""

PROMPT_END = """<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""

PROMPT_ONLY_EXAMPLES = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nRewrite the input text into a simpler and easier to understand ouput text. This output text is meant for people with learning and cognitive disabilities. 
 
Follow these two examples:
 
Original input text: The capybara or greater capybara (Hydrochoerus hydrochaeris) is a giant cavy rodent native to South America. It is the largest living rodent and a member of the genus Hydrochoerus. The only other extant member is the lesser capybara (Hydrochoerus isthmius). Its close relatives include guinea pigs and rock cavies, and it is more distantly related to the agouti, the chinchilla, and the nutria. The capybara inhabits savannas and dense forests, and lives near bodies of water. It is a highly social species and can be found in groups as large as 100 individuals, but usually live in groups of 10–20 individuals. The capybara is hunted for its meat and hide and also for grease from its thick fatty skin.
Simpler output text: The capybara is a big rodent.\n The capybara lives in South America.\n The capybara is the biggest rodent alive.\n The capybara lives in South America.\n Capybaras are part of the Hydrochoerus family.\n Other similar animals are: guinea pigs, rock cavies, chinchillas and otters.\n The capybara lives in savannas and rainforests.\n The capybara lives near places with water.\n The capybara is a social animal.\n The capybara lives in groups.\n Humans hunt capybaras because of their meat and their fat."
 
Original input text: The requirements for the front line of air traffic control are a poor match for AI’s capabilities. People expect air traffic to continue to be the safest complex, high-technology system ever. It achieves this standard by adhering to procedures when practical, which is something AI can do, and by adapting and exercising good judgment whenever something unplanned occurs or a new operation is implemented – a notable weakness of today’s AI. Indeed, it is when conditions are the worst – when controllers figure out how to handle aircraft with severe problems, airport crises or widespread airspace closures due to security concerns or infrastructure failures – that controllers’ contributions to safety are the greatest.
Simpler output text: Air traffic control needs skills that Artificial Intelligence does not have.\n Air traffic systems are difficult technology systems.\n People think air traffic systems are very safe systems.\n Air traffic systems can take good decisions in unexpected situations.\n Air traffic systems adapt to changes.\n Artificial Intelligence adapts worse than air traffic systems.\n Air controllers help mantain security and safety specially when there are problems.<|eot_id|><|start_header_id|>user<|end_header_id|>
"""

PROMPT_EXAMPLES_ONE_INSTRUCTION = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nRewrite the input text into a simpler and easier to understand ouput text. This output text is meant for people with learning and cognitive disabilities. Do so by:
 
- The subject of each sentence must be explicit (full name), do not use pronouns as subjects (no use I, you, he ,she or they).
- Use short sentences and simple vocabulary. Be repetitive if necessary.
- Do not use negations.
 
Follow these two examples:
 
Original input text: The capybara or greater capybara (Hydrochoerus hydrochaeris) is a giant cavy rodent native to South America. It is the largest living rodent and a member of the genus Hydrochoerus. The only other extant member is the lesser capybara (Hydrochoerus isthmius). Its close relatives include guinea pigs and rock cavies, and it is more distantly related to the agouti, the chinchilla, and the nutria. The capybara inhabits savannas and dense forests, and lives near bodies of water. It is a highly social species and can be found in groups as large as 100 individuals, but usually live in groups of 10–20 individuals. The capybara is hunted for its meat and hide and also for grease from its thick fatty skin.
Simpler output text: The capybara is a big rodent.\n The capybara lives in South America.\n The capybara is the biggest rodent alive.\n The capybara lives in South America.\n Capybaras are part of the Hydrochoerus family.\n Other similar animals are: guinea pigs, rock cavies, chinchillas and otters.\n The capybara lives in savannas and rainforests.\n The capybara lives near places with water.\n The capybara is a social animal.\n The capybara lives in groups.\n Humans hunt capybaras because of their meat and their fat."
 
Original input text: The requirements for the front line of air traffic control are a poor match for AI’s capabilities. People expect air traffic to continue to be the safest complex, high-technology system ever. It achieves this standard by adhering to procedures when practical, which is something AI can do, and by adapting and exercising good judgment whenever something unplanned occurs or a new operation is implemented – a notable weakness of today’s AI. Indeed, it is when conditions are the worst – when controllers figure out how to handle aircraft with severe problems, airport crises or widespread airspace closures due to security concerns or infrastructure failures – that controllers’ contributions to safety are the greatest.
Simpler output text: Air traffic control needs skills that Artificial Intelligence does not have.\n Air traffic systems are difficult technology systems.\n People think air traffic systems are very safe systems.\n Air traffic systems can take good decisions in unexpected situations.\n Air traffic systems adapt to changes.\n Artificial Intelligence adapts worse than air traffic systems.\n Air controllers help mantain security and safety specially when there are problems.<|eot_id|><|start_header_id|>user<|end_header_id|>
"""

SIMPLE_PROMPT = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nRewrite the input text into a simpler and easier to understand ouput text. This output text is meant for people with learning and cognitive disabilities. 
You must follow these instructions:
- Do not use pronouns to start sentences.
- Do not use they, she, it, he.<|eot_id|><|start_header_id|>user<|end_header_id|>"""


SIMPLE_CONCEPT_PROMPT= """<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nDefine the input concept taking into account the given input context. Define it in simpler and easier to understand way. This definition is meant for people with learning and cognitive disabilities. Follow these two examples:
 
Input concept: Savanna
Simple definition: \nThe Savanna is a type of ecosystem.\nThe Savanna is found in tropical regions.\nThere is grass and some trees in the Savanna.\nSavannas typically have warm temperatures.\nSavannas have both wet and dry seasons.\nLots of animals live in the Savannas.\nAnimales like zebras and lions live in the Savanna.
 
Input concept: Air Controller
Simple definition: \nAn air controller is a person.\nAn air controller helps guide airplanes safely.\nThey give instructions to airplanes in the sky and at airports.\nAir controllers make sure: planes take off and planes land.\nThey make sure planes fly in the right direction without bumping into each other.<|eot_id|><|start_header_id|>user<|end_header_id|>
"""