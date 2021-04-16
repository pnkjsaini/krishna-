from asr_engine import speech_recog as sr
from response import response  as rsr
import os
from tts_engine import text_to_speech as tts

def greeting():
	print("Function for wishing you greetng ")
tts("Sir,How can i help you")
text=sr()
tts(rsr(text))
text_r=sr()
tts(rsr(text_r))
