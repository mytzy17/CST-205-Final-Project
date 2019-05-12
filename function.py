from PIL import Image
from google.cloud import translate
import pyttsx3
import pytesseract



class ImageToText():
    engine = pyttsx3.init()

    def getText(fname):
        text = pytesseract.image_to_string(Image.open(fname))
        return text
    def speech(text, path):
        text = text.replace('\n', ' ')
        engine.say(text)
        engine.runAndWait()

    def translate(text, target):
        print(u'Text: {}'.format(result['input']))
        print(u'Translation: {}'.format(result['translatedText']))
        print(u'Detected source language: {}'.format(result['detectedSourceLanguage']))



