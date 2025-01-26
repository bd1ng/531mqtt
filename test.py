import requests
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path=dotenv_path)

key = os.getenv("KEY")

genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-1.5-flash')

chat = model.start_chat(history=[])
response = chat.send_message("Write a poem about how MQTT works.")

print(response.text)