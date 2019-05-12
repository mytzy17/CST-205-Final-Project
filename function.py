from PIL import Image
from google.cloud import translate
import pyttsx3
import pytesseract

translate_client = translate.Client()
result = translate_client.translate(
    text, target_language=target)

engine = pyttsx3.init()
text = pytesseract.image_to_string(Image.open(path))

class ImageToText:
    def speech(text, path):
        #client = translate.Client()
       # client.get_languages()
        text = text.replace('\n', ' ')
        engine.say(text)
        engine.runAndWait()

    def translate(text, target):
        print(u'Text: {}'.format(result['input']))
        print(u'Translation: {}'.format(result['translatedText']))
        print(u'Detected source language: {}'.format(result['detectedSourceLanguage']))



