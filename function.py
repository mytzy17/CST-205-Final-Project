from PIL import Image
#from google.cloud import translate
import pyttsx3
import pytesseract
def trans():
    engine = pyttsx3.init()

    text = pytesseract.image_to_string(Image.open('images/testImg1.png'))
    #client = translate.Client()
   # client.get_languages()
    text = text.replace('\n', ' ')
    engine.say(text)
    engine.runAndWait()
trans()
