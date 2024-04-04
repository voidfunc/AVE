import google.generativeai as genai
import os
def gen(words,type,mode,input="",api=False,longmethod=False):
    GOOGLE_API_KEY=''
    if api:
        GOOGLE_API_KEY = api
    else:
        GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    if mode == '文章续写':
        preprompt = open("preprompt3.txt", "r", encoding="utf-8")
        pass
    else:
        preprompt = open("preprompt.txt", "r", encoding="utf-8") if mode == "背诵文章" else open("preprompt2.txt", "r",encoding="utf-8")
    preprompt = preprompt.read()
    preprompt = preprompt.replace("[type]", type)
    if longmethod:
        preprompt=preprompt.replace("[length]","250")
    else:
        preprompt=preprompt.replace("[length]","150")
    prompt:str=''
    for i in words.split(' '):
        if len(prompt) == 0:
            prompt=f'{i}'
        else:
            prompt+=','+f'{i}'
    if mode=="文章续写":
        prompt+=f"{input}"
    messages = [
        {'role':'user',
         'parts': [preprompt]},
        {'role':'model',
         'parts':["ok"]},
        {'role':'user',
         'parts': [f"{prompt}"]}
    ]
    response = model.generate_content(messages)
    return response.text
    pass
