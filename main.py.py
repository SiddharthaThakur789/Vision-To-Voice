from PIL import Image
import pytesseract
import pyttsx3
import speech_recognition as sr
engine=pyttsx3.init()
try:
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    img=Image.open(r"C:\Users\Siddhartha\Desktop\Lets Practice\input\eng22.jpeg")

    grey_img=img.convert("L")

    threshold=128
    wf_img=grey_img.point(lambda x:1 if x<threshold else 255)

    custom_config="oem 3 psm 6"
    extracted_img=pytesseract.image_to_string(wf_img,lang="eng",config=custom_config)

    print("Extracted Image:-\n")

    print(extracted_img)
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source,timeout=5,phrase_time_limit=50)
        word=r.recognize_google(audio)
        print(word)
        if word=="Mahadev":
            engine.say(extracted_img)
            engine.runAndWait()



except(OSError,FileNotFoundError):
    print("File Not Found Check The Path Properly")



