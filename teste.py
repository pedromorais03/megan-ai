import pyaudio
import wave
import speech_recognition as sr
import os

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
OUTPUT_FILENAME = 'audio.wav'

audio = pyaudio.PyAudio()
recognizer = sr.Recognizer()

stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("Recording...")

frames = []

for _ in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
   data = stream.read(CHUNK)
   frames.append(data)

print("Stop recording...")

stream.stop_stream()
stream.close()
audio.terminate()

with wave.open(OUTPUT_FILENAME, 'wb') as wf:
   wf.setnchannels(CHANNELS)
   wf.setsampwidth(audio.get_sample_size(FORMAT))
   wf.setframerate(RATE)
   wf.writeframes(b''.join(frames))

print(f"Save file with name {OUTPUT_FILENAME}")

with sr.AudioFile("audio.wav") as source:
   print("Processando o áudio...")
   audio_data = recognizer.record(source)

try:
   text = recognizer.recognize_google(audio_data, language="pt-BR") 
   print("Texto transcrito:")
   print(text)
except sr.UnknownValueError:
   print("O áudio não pôde ser reconhecido.")
except sr.RequestError as e:
   print(f"Erro ao se conectar ao serviço de reconhecimento: {e}")

if os.path.exists('audio.wav'):
   os.remove('audio.wav')