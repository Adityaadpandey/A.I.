import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import wikipedia
import time
from datetime import date
import pyjokes
import requests
from GoogleNews import GoogleNews
import subprocess
from pywinauto.application import Application
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

i = 0
j = 0
i1 = 0
sex = 'male'
dic = {"hello": "hello sir ,How are you", "hy": "hello sir ,How are you", "hayy": "Im fine sir "}
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
# print(voices) this is used to see the voices that how much voices do your pc have
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)  # thisis used to use the voices of the computer


def my():
    with open("ss", "r") as e:
        s = e.readlines()

        spacek(s)
        e.close()


def spacek(audio):
    engine.say(audio)

    engine.runAndWait()


def me():
    s = "hello sir Im jarvise 2. point o " \
        "Created by aditya "

    spacek(s)

    spacek("how can i help you !")


def wishme(s):
    hour = int(datetime.datetime.now().hour)

    if (hour >= 0 and hour < 12):
        spacek(f"Good Monring {s}!")

    elif hour >= 12 and hour < 18:
        spacek(f"Good After Noon {s}!")

    else:
        spacek(f"Good Evening{s}!")

    spacek(f"Hello {s} How can i help you !")


def opendetiles():
    spacek("you want to only see the user deties or i should speack")

    s = takecommend()

    if (s == "see"):
        with open("data of user.text", "r") as e:
            e.readlines()
            print(e)
            e.close()
    else:
        with open("data of user.text", "r") as e:
            s = e.readlines()
            print(s)
            spacek(s)
            e.close()


def username(s1):
    try:
        spacek(f"what i should to call you{s1}")
        s = takecommend()
        s = s.replace("call me", '')
        spacek(f"helle{s1} ")
        spacek(s)
        with open("data of user.text", "a") as e:
            st = datetime.datetime.now()
            st1 = date.today()
            e.write(f"{s} use me on {st1}at{st} \n ")
            e.close()
            spacek(f"how can i help you {s1}")
    except Exception as e:
        spacek(f"{s1} i dont understant sir what did you say ")

        username(s1)


def takecommend():
    """this takes maicorphone input from the user and returns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing......")
        r.pause_threshold = 1
        audio = r.listen(source)  # to see everything about this please press control and click on the line
    try:
        print("Recozinagition..........")
        query = r.recognize_google(audio, language='en-in')
        print("You said", query)
    except Exception as e:
        print(e)
        print("said it again please")

        # if e=="recognition connection failed: [Errno 11001] getaddrinfo failed":
        #  spacek("There are some suggetion please cheak your internet connection or reapet what did you say")
        return None
    return query


def stoplisting():
    spacek("for how much seconed  you want to stop jarvise  from listening commands")
    try:
        a = int(takecommend())
        spacek("going to sleep for")
        spacek(a)
        time.sleep(a)
    except Exception as e:
        spacek(" I could not understand what did you say could not got to sleep")
        stoplisting()


def walkupme():
    strftime = datetime.datetime.now().strftime("%H:""%M:""%S")
    spacek(f"it is{strftime} you have to walkup")


def news(str):
    global i
    if i == 0:
        spacek(f"ofcures {str} which news  you want to listen")
    else:
        spacek(f"which news you want to listen{str}")

    try:
        s = takecommend().lower()
        s = s.replace('about', "")
        spacek("which page you want ot listen")

        s2 = int(takecommend())
        googlenews = GoogleNews()
        googlenews = GoogleNews('en', "2")
        # here you can use d which is denoted for how much linw you want to lesiten
        googlenews.search(s)
        googlenews.getpage(s2)
        googlenews.result()
        spacek(f" {str} here is news about ")
        spacek(s)
        print(googlenews.gettext())
        spacek(googlenews.gettext())
    except Exception as s:
        spacek(f"could not understand {str} what did  you say  say it again")
        i = 1
        news(str)


def me1():
    with open("gg", "r") as e:
        s = e.readlines()
        spacek(s)
        e.close()


def jarvis():
    global j
    if j == 0:
        spacek("")
    else:
        spacek("jarvis in a sleep mode sir")
    try:

        s = takecommend().lower()
        print(s)
        if 'sleep' in s:
            spacek("ok sir")
            jarvis()
            j += 1
        elif 'woke up' in s:
            spacek("ok sir it will take some time to get connection to network")
            main()
        else:
            jarvis()
    except Exception as e1:
        jarvis()


def into():
    global i1
    global sex
    while (1):
        if i1 > 0:
            spacek("who are you sir")

        try:

            s1 = takecommend().lower()
            s1 = s1.replace('im', '')
            if 'akhilesh' in s1:
                sex = 'sir'

            else:
                spacek("plesae identifai your self Are you a male of female  !")
                spacek("or girl or boy")
                s1 = takecommend().lower()
                if 'male' in s1 or 'boy' in s1:
                    sex = 'sir'
                elif 'female' in s1 or 'girl' in s1:
                    sex = 'meam'
                else:
                    into()
                    i1 = +1

            if 'akhilesh' not in s1:
                username(sex)
                print(sex)
                wishme(sex)
                break
            else:
                print(sex)
                wishme(sex)
                break
        except Exception as e:
            i1 = +1
            into()


def main():
    into()
    while (1):
        clear = lambda: os.system('cls')
        clear()
        try:
            queuery = takecommend().lower()

            if 'wikipedia' in queuery:
                spacek("seraching .......")
                queuery = queuery.replace("wikipedia", "")
                result = wikipedia.summary(queuery, sentences=2)
                spacek("Accroding to wikipedia")
                spacek(result)

            elif 'open youtube' in queuery:
                spacek("about what you want to search on youtube")
                s = takecommend()
                webbrowser.open("www.youtube.com/results?search_query=" + s + "")

                spacek(f"opening youtube {sex}!")
            elif 'open google' in queuery:
                webbrowser.open("google.com")
                spacek(f"opening google{sex} !")

            elif 'the time' in queuery:
                strtime = datetime.datetime.now().strftime("%H:""%M:""%S")
                spacek(f"{sex} the time is{strtime}")

            elif 'open code' in queuery:

                codepath = "C:\\Users\\Akhilesh Goswami\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
                spacek(f"opening vs code {sex}!")
                spacek(
                    f"you opened vs code {sex} would like to stop me from listing if yes please said stop listening or dont listen")

            elif 'open dev' in queuery:
                codepath = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
                spacek(f"opening Dev ++ {sex}!")
                os.startfile(codepath)
                spacek(
                    "you opened another programe sir would like to stop me from listing if yes please said stop listening or dont listen")

            elif 'open facebook' in queuery:
                webbrowser.open("facebook.com")
                spacek(f"opening Facebook {sex}!")
                spacek(
                    f"you opened anthore programe {sex}would like to stop me from listing if yes please said stop listening or dont listen")

            elif 'search' in queuery:
                s = webbrowser.open(queuery)

                spacek(s)
                spacek(
                    f"you opened anthore programe{sex} would like to stop me from listing if yes please said stop listening or dont listen")

            elif 'who is' in queuery:
                webbrowser.open(queuery)

            elif 'hello' in queuery:
                me()
                spacek(f"hello {sex} ! How are you")

            elif 'good' in queuery or 'well' in queuery:
                spacek(f'great to that you are well {sex}')

            elif 'who are you' in queuery:
                me()
            elif "will you be my gf" in queuery or "will you be my bf" in queuery:
                spacek("I'm not sure about, may be you should give me some time")

            elif "how are you" in queuery:
                spacek("I'm fine, glad you me that")

            elif "i love you" in queuery:
                spacek("It's hard to understand")

            elif 'today' in queuery:
                spacek("It is")
                spacek(date.today())
                spacek("today")

            elif "don't listen" in queuery or "stop listening" in queuery:
                spacek("ok sir")
                jarvis()

            elif 'change my name' in queuery or 'change name' in queuery:
                s = takecommend()
                spacek("Now your name is ")
                spacek(s)

            elif 'user detiless' in queuery:
                opendetiles()

            elif 'about me' in queuery or 'do you know me' in queuery:
                spacek("what is your name")
                s = takecommend().lower()
                if 'akhilesh' in s:
                    my()
                else:
                    spacek("i dont have your data")

            elif 'exit' in queuery:
                spacek("Thanks for giving me your time")
                exit()

            elif "who made you" in queuery or "who created you" in queuery:
                spacek("I have been created by Akhilesh.")

            elif 'joke' in queuery:
                s = pyjokes.get_joke(language='en', category='all')
                spacek(s)

            elif "where is" in queuery:
                queuery = queuery.replace("where is", "")
                location = queuery
                spacek("User asked to Locate")
                spacek(location)
                spacek(
                    "you opened anthore programe sir would like to stop me from listing if yes please said stop listening or dont listen")
                webbrowser.open("https://www.google.com/maps/place/" + location + "")

            elif "weather" in queuery:
                spacek(" City name ")
                print("City name : ")
                city_name = takecommend()
                webbrowser.open("https://www.accuweather.com/en/in/" + city_name + "/189231/weather-forecast/189231")
                spacek("opening wether for")
                spacek(city_name)

            elif "news" in queuery:
                news(sex)
            elif 'shutdown' in queuery or 'sleep my' in queuery:
                spacek(f"souting down {sex}")
                os.system("shutdown /h")

            elif "restart" in queuery:
                os.system('shutdown /r')

            elif 'help me' in queuery:
                spacek(f"ofcurse {sex} ! how can i help yous {sex}")
                spacek(f'question {sex}!')
                s = takecommend()
                print(s)
                spacek(
                    "There are 3 thing that i can do for you sir i can search for it on google or youtube or wikipedia")
                spacek(f"where i should to serach {sex}")
                s1 = takecommend().lower()
                if s1 == 'google':
                    spacek(f"opening  google {sex}!")
                    webbrowser.open(
                        "www.bing.com/search?q=" + s + "=9d02b0a92caa4bc895c28ea9269d27e6&FORM=ANAB01&PC=ASTS")

                elif s1 == 'youtube' in queuery:
                    spacek(f"opening youtube{sex}!")
                    webbrowser.open("www.youtube.com/results?search_query=" + s + "")

                elif s1 == 'wikipedia' in queuery:
                    spacek("Accroding to wikipedia")
                    result = wikipedia.summary(s, sentences=2)

            elif 'play music' in queuery or "play song" in queuery:
                spacek("Here you go with music")
                # music_dir = "G:\\Song"
                spacek("you open another programe would you like to sleep mor exit from the program")
                music_dir = "C:\\Users\\Akhilesh Goswami\\Desktop\\my"
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[1]))

            elif 'wrok' in queuery:
                spacek(f"sorry {sex} because of me you face some problem "
                       "sir some time i dont work properly there are some few resone that are low internet connection or some noiese "
                       "that i anble to understand im working on that i will take care you will not face this problem again")

            elif "meet" in queuery:
                spacek(f"hello {sex} !what is your friends name ")
                s = takecommend().lower()
                spacek(f"nice to meet you {s} ! have a good day!")

            elif "know akhilesh" in queuery:
                spacek(
                    f"yes{sex} i know him becuase of him im able to talk to you he is a very nice person would you like to know more about mister akhilesh goswami")
                s = takecommend().lower()
                if s == "yes":
                    me1()
                else:
                    spacek(f"ok !{sex} thank you for give me time sir")



            elif 'girl' in queuery:
                spacek("wow why did you not tell me before that hy babe how are you will you be my gf")


            elif 'open calculator' in queuery:
                spacek("open the calculator")
                subprocess.Popen("C:\\Windows\\System32\\calc.exe")
            elif " want to wirte a note" in queuery:
                dd()
            elif 'close' in queuery:
                spacek("closing the window")
                pyautogui.hotkey('alt', 'f4')

            elif 'minimise the windows ' in queuery or 'minimise the window' in queuery:
                spacek("minimize the window")
                pyautogui.hotkey('Win', 'd')

            elif 'maximize the windows' in queuery or 'maximize the window' in queuery:

                spacek("maximizeing windows")
                pyautogui.hotkey('Win', 'd')

            elif 'new tab' in queuery:
                pyautogui.hotkey('ctrl', 't')

            elif 'new file' in queuery:
                pyautogui.hotkey('ctrl', 'n')

            elif 'switch the windows' in queuery or 'switch the tab' in queuery:
                pyautogui.hotkey('ctrl', 'shift', 'tab')

            elif 'volume up' in queuery:
                spacek('valume up sir')
                pyautogui.hotkey('volumeup')

            elif 'push' in queuery or 'play' in queuery:
                spacek('ok')
                pyautogui.press('Space')

            elif 'open chrome' in queuery:
                spacek("opening broswer sir")
                p = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(p)
                time.sleep(6)
            elif 'i want to search' in queuery or 'write' in queuery:

                spacek("ok sir please say what you want to write or search sir")
                s = takecommend()
                pyautogui.write(s)
                time.sleep(3)
                pyautogui.press('enter')

            elif 'up' in queuery:
                pyautogui.press('up')

            elif 'down' in queuery:
                pyautogui.press('down')

            elif 'left' in queuery:
                pyautogui.press('left')

            elif 'right' in queuery:
                pyautogui.press('right')

            elif 'enter' in queuery:
                pyautogui.press('enter')

            elif 'open python' in queuery:
                spacek("opening python")

            elif 'click' in queuery:
                pyautogui.click()

            elif 'jarvis' in queuery:
                spacek(f"jarvise 2 point 0 in your service {sex}")
            elif 'open python' in queuery:

                p = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
                os.startfile(p)
                time.sleep(15)
        except Exception as s:
            print(s)
            spacek(f" i dont understand sir please give me some other commend {sex}")


def dd():
    while True:
        try:
            spacek("what you want to write in a note")
            s = takecommend().lower()
            app = Application().start("notepad.exe")
            app.UntitledNotepad.menu_select("Help->About Notepad")
            app.aboutNotepad.OK.click()
            app.UntitledNotepad.Edit.type_keys(s, with_spaces=True)
            spacek("would you like to write more or want to save the file")
            s2 = takecommend().lower()
            if 'yes' in s2:
                s3 = takecommend()
                app.UntitledNotepad.Edit.type_keys(s3, pyautogui.hotkey('enter'), with_spaces=True)
                spacek("would you like to save this")
                se = takecommend().lower()

                if 'yes' in se:
                    app.UntitledNotepad.menu_select("File->save->save")
                    spacek("please give a name to file")
                    time.sleep(5)
                    pyautogui.hotkey('ctrl', 's')
                    spacek("file has been saved")
                    break
            elif 'save' in s2:
                app.UntitledNotepad.menu_select("File->save->save")
                spacek("please give a name to file")
                time.sleep(5)
                pyautogui.hotkey('ctrl', 's')
                spacek("file has been saved")
                break
            spacek("would you like to close the windows")
            s1 = takecommend().lowwer()
            if 'yes' in s1:
                spacek("ok sir")
                app.UntitledNotepad.menu_select("File->Exit")
                app.Exit.OK.click()
                pyautogui.hotkey('alt', 'f4')
            elif 'no' in s1:
                break

        except Exception as e:
            spacek("i could not understand sir plesase speack again")


if __name__ == "__main__":
    # jarvis()
    main()
