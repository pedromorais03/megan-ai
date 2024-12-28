# import google.generativeai as genai
# from dotenv import load_dotenv
# import pyaudio
# import wave
# import speech_recognition as sr
# from gtts import gTTS
# from playsound import playsound
# import os

# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 44100
# CHUNK = 1024
# RECORD_SECONDS = 5
# OUTPUT_FILENAME = 'audio.wav'

# load_dotenv()
# g_api_key = os.getenv('GOOGLE_API_KEY')


# def generate():
#    audio = pyaudio.PyAudio()
#    recognizer = sr.Recognizer()

#    genai.configure(api_key=g_api_key)

#    model = genai.GenerativeModel("gemini-1.5-flash")

#    # opening audio flow
#    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
#    print("Recording...")
#    frames = []

#    # recording datas in frames
#    for _ in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
#       data = stream.read(CHUNK)
#       frames.append(data)

#    print("Stop recording...")
#    # stop and close audio flow
#    stream.stop_stream()
#    stream.close()
#    audio.terminate()

#    # saving audio in file .wav
#    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
#       wf.setnchannels(CHANNELS)
#       wf.setsampwidth(audio.get_sample_size(FORMAT))
#       wf.setframerate(RATE)
#       wf.writeframes(b''.join(frames))

#    print(f"Save file with name {OUTPUT_FILENAME}")

#    # reading .wav file
#    with sr.AudioFile("audio.wav") as source:
#       print("Processing audio...")
#       audio_data = recognizer.record(source)

#    # recognizing text using Google Speech Recognition
#    try:
#       text = recognizer.recognize_google(audio_data, language="pt-BR") 
#       print("Transcribed text:")
#       print(text)
#    except sr.UnknownValueError:
#       print("Audio could not be recognized")
#    except sr.RequestError as e:
#       print(f"Error: {e}")

#    # deleting .wav file from dir
#    if os.path.exists('audio.wav'):
#       os.remove('audio.wav')
#       print("Removed .wav file")

#    # sending text to gemini model
#    response = model.generate_content(text)
#    response_text = response.text
#    response_text = response_text.replace("*", "")
#    print(response_text)

#    # generating TTs
#    tts = gTTS(text=response_text, lang='pt')
#    tts.save("tts.mp3")
#    print("Gemini response to audio generated!")

#    # playing audio
#    playsound("./tts.mp3")
#    print("Playing audio")

#    if os.path.exists('tts.mp3'):
#       os.remove('tts.mp3')
#       print("Removed .mp3 file")