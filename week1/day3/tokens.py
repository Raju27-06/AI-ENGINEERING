import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq


load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
        raise ValueError("API KEY NOT FOUND!")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-20b"
role="user"

#prompts
prompt1 = "Hi"
prompt2 = "explain big bang theory in details"
prompt3 = "write an essay on persevernce of culture in 1000 words"

prompts =[prompt1,prompt2,prompt3]

for prompt in prompts:
        message={
        "role":role,
        "content":prompt
        }
        messages = [message]
        response = client.chat.completions.create(model=model,messages=messages,max_tokens=50)
        usage = response.usage
        print(f"Prompt: {prompt} --> my_tokens: {usage.prompt_tokens} completion_token: {usage.completion_tokens} finish_reason: {response.choices[0].finish_reason}")
        

# prompt="do you know ms dhoni"

# message_system = {
#     "role":"system",
#     "content":"you are a professional cricketer played under ms dhoni's captaincy"        
# }

# message={
#         "role":role,
#         "content":prompt
# }

# messages=[message_system,message]

# #by default temperature is 0
# response = client.chat.completions.create(model=model,messages=messages,temperature=2)

# print(response)

print(response.choices[0].message.content)
