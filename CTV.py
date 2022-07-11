import pyttsx3

engine = pyttsx3.init()


answer = input(">>> ")
engine.say(answer)
engine.save_to_file(answer, "CTV.mp3")
engine.runAndWait()
