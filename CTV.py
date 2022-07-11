import pyttsx3
import os

engine = pyttsx3.init()

os.system('clear')

print("Enter your Text")
answer = input(">>> ")

engine.setProperty("rate", 120)
engine.say(answer)
engine.save_to_file(answer, "CTV.mp3")
engine.runAndWait()
