from gtts import gTTS as tts
import os 
def text_to_speech(text_string):
	text_to_speech= tts(text_string)
	text_to_speech.save('voice.mp3')
	os.system('mpg123 voice.mp3')
#checked
