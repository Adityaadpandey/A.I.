"""import requests
from bs4 import BeautifulSoup

search = "weather today"
url = f"http://www.google.com/search?q={search}"

req = requests.get(url)
sav = BeautifulSoup(req.text, "html.parser")
update = sav.find("div", class_ = "BNeawe").text
print(update)"""

import pyttsx3
from requests_html import HTMLSession

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def news():
    session = HTMLSession()
    url = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"
    r = session.get(url)
    r.html.render(sleep=1, scrolldown=0)

    article = r.html.find('article')

    for item in article:
        try:
            newsitem = item.find('h3', first=True)
            title = newsitem.text
            print(title)
            speak(title)
        except:
            pass

