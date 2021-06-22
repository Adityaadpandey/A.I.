import requests
from bs4 import BeautifulSoup
import pyttsx3

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def temprature():
    search = "weather today"
    url = f"http://www.google.com/search?q={search}"

    req = requests.get(url)
    sav = BeautifulSoup(req.text, "html.parser")
    update = sav.find("div", class_="BNeawe").text
    speak(update)
    print(update)
