import speech_recognition  as sr
def speech_recog():
	dummy = sr.Recognizer()
	with sr.Microphone() as source:
		print(">")
		audio=dummy.listen(source)
		try:
			text = dummy.recognize_google(audio)
			print("you said: {}".format(text))
		except:
			print("couldn't recognie your voice ")
	return  text.lower() 
# Working correctly
