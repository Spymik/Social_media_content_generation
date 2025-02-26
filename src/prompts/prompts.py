    

# -------- Done By Manu --------------
def llm_prompt(platform:str, topic:str, company_name:str, lang:str = 'English', word_lim:int = 250) -> str :
    LLM_PROMPT = f"""Generate a high-quality, engaging and professional social media post for a {company_name} in a descriptive format. Follow the example structure and ensure clarity, creativity, context awareness, and audience engagement.
    Context:
    - Platform: {platform}  
    - Topic: {topic}
    - Language: {lang}  
    - Word Limit: {word_lim}

    Requirements:
    - Craft a compelling opening that grabs attention.  
    - Highlight key details about the business or occasion.  
    - Maintain a consistent and engaging tone throughout.  
    - Tone should be determined by the platform.
    - Use persuasive language and storytelling where applicable.  
    - Include a strong call to action (CTA) to encourage engagement.  


    Now, generate a social media post using the provided context."""

    return LLM_PROMPT

def llm_finetuning_prep(data_dict: dict) -> str :
    
    # parsing dictionary for formatting
    company_name = 'Itobuz'
    platform = data_dict.get('platform')
    heading = data_dict.get('post_heading')
    content = data_dict.get('post_contents')
    hashtags = data_dict.get('hashtags')
    emojis = data_dict.get('emoji')
    emojis = ", ".join(emojis) if len(data_dict.get('emoji'))>0 else "No emoji needed"
    hashtags = ", ".join(hashtags)
    raw_post_content = data_dict.get('raw_post_content')
    
    
    # genrating data format from the finetuning
    DATA_FORMAT = f""" 
    - Company Name : {company_name}
    - Platform: {platform}
    - Heading : {heading} 
    - Content : {content}
    - emojis : {emojis}
    - hashtags : {hashtags}
    - Response: {raw_post_content}"""

    return DATA_FORMAT
# -------------------------------------