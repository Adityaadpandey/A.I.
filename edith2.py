import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
import pywhatkit
import pyjokes
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):  # here audio is var which contain query
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir i am  edith how may i help you")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir i am  edith how may i help you")
    else:
        speak("good night sir i am  edith how may i help you")

    # now convert audio to query


#
def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising.")
        text = r.recognize_google(audio, language='en-IN')
        print(text)
    except Exception:  # For Error handling
        speak("error... speak aloud ")
        print("error... speak aloud")
        return "none"

    return text


# for main function
if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()

        if "wikipedia" in query:
            speak("searching details....Wait")
            query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            print(results)
            speak(results)
        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")

        elif 'open whatsapp' in query:
            webbrowser.open('https://web.whatsapp.com/')
            speak('opening whatsapp')
        elif 'new wallpaper' in query:
            webbroser.open('https://wallpapershome.com/')
            speak('getting some new wallpapers')
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")

        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail")

        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com")
            speak("opening snapdeal")

        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.in/")
            speak("opening amazon")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")
        elif 'open class' in query or 'classes' in query:
            webbrowser.open("https://assessment.padhoapp.com/#/liveClass/joinSession")
            speak("opening your school classes")
        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")

        elif 'music from pc' in query or "music" in query:
            speak("ok i am playing music")
            music_dir = './music'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, musics[0]))
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())


        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = './video'
            videos = os.listdir(music_dir)
            os.startfile(os.path.join(video_dir, videos[0]))
        elif 'good bye' in query:
            speak("good bye")
            exit()
        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy',
                      'i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
            ans_take_from_user_how_are_you = takecom()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')
        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information Aditya pandey Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am edith an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)
        elif "hello" in query or "hello edith" in query:
            hel = "Hello aditya  ! How May i Help you.."
            print(hel)
            speak(hel)
        elif 'get my phone access' in query or 'my phone storage' in query:
            webbrowser.open('ftp://192.168.1.33:2221')
            speak('here is the access')
        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! edith"
            print(na_me)
            speak(na_me)
        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you")

        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query:
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()
        elif "news" in query or "tell me some news" in query:
            session = HTMLSession()
            url = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"
            ok = session.get(url)
            ok.html.render(sleep=1, scrolldown=1)
            article = ok.html.find('article')
            for item in article:
                try:
                    newsitem = item.find('h3', first=True)
                    title = newsitem.text
                except:
                    print(title)
                    speak(title)
        elif 'wheather' in query or 'today weather':

            search = "weather today"
            n_url = f"http://www.google.com/search?q={search}"

            req = requests.get(n_url)
            sav = BeautifulSoup(req.text, "html.parser")
            update = sav.find("div", class_="BNeawe").text
            print(update)
            speak('temperature out side is' + update)
        else:
            temp = query.replace(' ', '+')
            g_url = "https://www.google.com/search?q="
            res_g = 'sorry! i cant understand but i search from internet to give your answer ! okay'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url + temp)
