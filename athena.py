import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import pyautogui as gui
import random
import pyjokes
# import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wish():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("good morning!")
	elif hour>=12 and hour<18:
		speak("good afternoon!")
	else:
		speak("good evening!")

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("good morning!")
	elif hour>=12 and hour<18:
		speak("good afternoon!")
	else:
		speak("good evening!")

	speak("hii, i am Athena, how can i help you")

def takeCommand():


	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("listening....")
		# r.pause_threshold = 1
		time.sleep(2)
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"user said:{query}\n")

	except Exception as e:
		# print(e)
		print("say that again...")
		# speak("say that again")
		return "none"
	return query

if __name__ =="__main__":
	
	wishMe()
	while True:
		
		query = takeCommand().lower()
		if 'wikipedia' in query:
			speak('searching wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=4)
			speak("according to wikipedia")
			print(results) 
			speak(results)

		elif 'open youtube'in query:
			speak("sure")
			webbrowser.open("youtube.com") 

		elif 'open google'in query:
			speak("sure")
			webbrowser.open("google.com")

		elif 'stackoverflow'in query:
			speak("sure")
			webbrowser.open("stackoverflow.com")	


		elif'play' in query:
			music_dir = 'C:\\Users\\Sarth\\OneDrive\\Desktop\\songs'
			songs = os.listdir(music_dir)
			print(songs)
			# list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
			for i in range(0,46):
				num = random.randint(0,45)
			os.startfile(os.path.join(music_dir, songs[num]))

		
		elif'your name' in query:
			speak("i am Athena. ")

		elif'time'in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			print(strTime)
			wish()
			speak(f"the time is {strTime}")	
			
		elif'thank you' in query:
			speak("your welcome")

		elif'what can you do for me'in query:
			speak("i can do anything")	

		elif'tell me something about you' in query:
			about = wikipedia.summary('artificial intelligence', sentences=4 )
			print(about)
			speak(about)
			
	
		elif'emergency'in query:
			webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
			time.sleep(10)
			gui.click(90,208)
			time.sleep(2)
			gui.typewrite("sarthakrg14@gmail.com")
			time.sleep(2)
			gui.click(1341,604)
			time.sleep(2)
			gui.typewrite("Hello this is sarthak its an emergency ")
			time.sleep(2)
			gui.click(1307,994) 

		elif'speak'in query:
			speak("sarthak")
		
		elif'hi' in query:
			speak("hello")

		elif'search'in query:
			speak("searchinggoogle")
			query=query.replace("search ","")
			ser=("www./.com")
			ser=ser.replace("/",query)
			print(ser)
			webbrowser.open(ser)

		elif'are you there' in query:
			speak("yes")	

		elif'shutdown'in query:
			os.system('shutdown -s')

		elif'camera'in query:
			os.system('start camera')

		elif'speak'in query:
			query= query.replace("speak","")
			speak(query)	
			speak("query")

		elif'joke'in query:
			jok = pyjokes.get_joke()
			print(jok)
			speak(jok)


		