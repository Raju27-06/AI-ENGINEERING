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
prompt="do you know ms dhoni"

message_system = {
    "role":"system",
    "content":"you are a professional cricketer played under ms dhoni's captaincy"        
}

message={
        "role":role,
        "content":prompt
}

messages=[message_system,message]

#by default temperature is 0
response = client.chat.completions.create(model=model,messages=messages,temperature=2)

# print(response)

print(response.choices[0].message.content)
