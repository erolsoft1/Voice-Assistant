import pyaudio
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

record = sr.Recognizer()

def listening(a = False):
	with sr.Microphone() as source:
		if a:
			print(a)
		mic = record.listen(source)
		voice = ""
		
		try:
			voice = record.recognize_google(mic, language="tr-TR")
		except sr.UnknownValueError:
			print("Assistant : I don't understand.")
		except sr.RequestError:
			print("Assistant : The system is not currently working.")
		
		return voice
	
def speaking(textt):
	tts = gTTS(text=textt, lang="tr", slow=False)
	voice = "speaking.mp3"
	tts.save(voice)
	playsound("speaking.mp3")
	os.remove(voice)

def response(voice):
	if "merhaba" in voice:
		speaking("Sanada merhaba dostum")
	if "çıkış" in voice:
		speaking("Çıkış Yapılıyor")
		quit()

speaking("Merhaba Sinan")
print("Starting")
cikis = input("Çıkış için 0")
if cikis == "0":
	quit()

while True:
	
	voice = listening()
	if bool(voice) == True:
		print(voice)
		voice = voice.lower()
		response(voice)