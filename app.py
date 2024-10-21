import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

g_api_key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=g_api_key)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Hello model!")
print(response.text)