import google.generativeai as genai
from dotenv import load_dotenv
import pyaudio
import wave
import speech_recognition as sr
from gtts import gTTS
import os

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
OUTPUT_FILENAME = 'audio.wav'

load_dotenv()
g_api_key = os.getenv('GOOGLE_API_KEY')


audio = pyaudio.PyAudio()
recognizer = sr.Recognizer()

genai.configure(api_key=g_api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

# opening audio flow
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
print("Recording...")
frames = []

# recording datas in frames
for _ in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
   data = stream.read(CHUNK)
   frames.append(data)

print("Stop recording...")
# stop and close audio flow
stream.stop_stream()
stream.close()
audio.terminate()

# saving audio in file .wav
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
   wf.setnchannels(CHANNELS)
   wf.setsampwidth(audio.get_sample_size(FORMAT))
   wf.setframerate(RATE)
   wf.writeframes(b''.join(frames))

print(f"Save file with name {OUTPUT_FILENAME}")

# reading .wav file
with sr.AudioFile("audio.wav") as source:
   print("Processando o áudio...")
   audio_data = recognizer.record(source)

# recognizing text using Google Speech Recognition
try:
   text = recognizer.recognize_google(audio_data, language="pt-BR") 
   print("Texto transcrito:")
   print(text)
except sr.UnknownValueError:
   print("O áudio não pôde ser reconhecido.")
except sr.RequestError as e:
   print(f"Erro ao se conectar ao serviço de reconhecimento: {e}")

# deleting .wav file from dir
if os.path.exists('audio.wav'):
   os.remove('audio.wav')

# sending text to gemini model
response = model.generate_content(text)
print(response.text)

tts = gTTS(text=response.text, lang='pt')
tts.save("tts.mp3")
print("Gemini response to audio generated!")