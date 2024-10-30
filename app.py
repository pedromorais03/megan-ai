import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

g_api_key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=g_api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

input_text = str(input("Faça sua pergunta: "))
response = model.generate_content(input_text)
print(response.text)