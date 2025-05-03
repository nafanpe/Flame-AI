from AppOpener import close, open as appopen
from webbrowser import open as webopen
from pywhatkit import search, playonyt
from dotenv import dotenv_values
from bs4 import BeautifulSoup
from groq import Groq
import webbrowser
import subprocess
import requests
import keyboard
import asyncio
import os

env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey")

classes = ["zCubwf", "hgKElc", "LTKOO sY7ric", "Z0LcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", 
           "tw-Data-text tw-text-small tw-ta", "IZ6rdc", "O5uR6d LTKOO", "vlzY6d", 
           "webanswers-webanswers_table__webanswers-table", "dDoNo jkb4Bb gsrt", "sXLa0e", "LWkfKe", 
           "VQF4g", "qv3Wpe", "kno-rdesc", "SPZz6b"]

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWenKit/537.36 (KHTML, Like Gecko) Chrome/100.0.4896.75 Safari/537.36'

client = Groq(api_key=GroqAPIKey)

professional_response = [
    "Your satisfaction is my priority. feel free to reach out if there's anything else I can help you with.",
    "I'm at your service for any additional questions or support you may need-don't hesitate to ask.",
]

messages = []

SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ['Username']}, You're a content writer. You have to write content like letters, codes, applications, essays, notes, songs, poems etc."}]

def GoogleSearch(Topic):
    search(Topic)
    return True

def Content(Topic):
    def OpenNotepad(File):
        default_text_editor = 'notepad.exe'
        subprocess.Popen([default_text_editor, File])

    def ContentWriterAI(prompt):
        messages.append({"role": "user", "content": f"{prompt}"})

        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=SystemChatBot + messages,
            max_tokens=2048,
            temperature=0.7,
            top_p=0.1,
            stream=True,
            stop=None
        )

        Answer = ""

        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content

        Answer = Answer.replace("</ s>", "")
        messages.append({"role": "assistant", "content": Answer})
        return Answer

    Topic: str = Topic.replace("Content ", "")
    ContentByAI = ContentWriterAI(Topic)
    
    with open(rf"Data\{Topic.lower().replace(' ', '')}.txt", "w", encoding="utf-8") as file:
        file.write(ContentByAI)
        file.close()
    print("Content generation complete.")
    OpenNotepad(rf"Data\{Topic.lower().replace(' ', '')}.txt")

def YoutubeSearch(Topic):
    Url4Search = f"https://www.youtube.com/results?search_query={Topic}"
    webbrowser.open(Url4Search)
    return True

def PlayYoutube(query):
    playonyt(query)
    return True

def OpenApp(app):
    try:
        appopen(app, match_closest=True, output=True, throw_error=True)
    except Exception as e:
        print(f"Couldn't open app directly: {e}")
        
        common_urls = {
            "instagram": "https://www.instagram.com/",
            "facebook": "https://www.facebook.com/",
            "twitter": "https://twitter.com/",
            "x": "https://twitter.com/",
            "youtube": "https://www.youtube.com/",
            "spotify": "https://open.spotify.com/",
            "netflix": "https://www.netflix.com/",
            "amazon": "https://www.amazon.com/",
            "gmail": "https://mail.google.com/",
            "mail": "https://mail.google.com/",
            "google": "https://www.google.com/",
            "discord": "https://discord.com/app",
            "whatsapp": "https://web.whatsapp.com/",
            "reddit": "https://www.reddit.com/",
            "linkedin": "https://www.linkedin.com/",
            "pinterest": "https://www.pinterest.com/",
            "tiktok": "https://www.tiktok.com/",
            "github": "https://github.com/",
            "twitch": "https://www.twitch.tv/",
        }
        
        app_lower = app.lower()
        if app_lower in common_urls:
            url = common_urls[app_lower]
            print(f"Opening {app} in default browser at {url}")
            webbrowser.open(url)
        else:
            try:
                print(f"Searching for {app} online")
                url = f"https://www.google.com/search?q={app}"
                webbrowser.open(url)
                
                """
                search_url = f"https://www.google.com/search?q={app}"
                html = urlopen(search_url).read().decode()
                links = extra_links(html)
                if links and len(links) > 0:
                    link = links[0]
                    webbrowser.open(link)
                else:
                    # If no links found, just open the search page
                    webbrowser.open(search_url)
                """
            except Exception as e2:
                print(f"Error opening {app} in browser: {e2}")
                webbrowser.open(f"https://www.google.com/search?q={app}")


def CloseApp(app):
    if "chrome" in app:
        pass
    else:
        try:
            close(app, match_closest=True, output=True, throw_error=True)
            return True
        except:
            return False
            print("Task Failed!")

def System(command):
    def mute():
        keyboard.press_and_release('volume mute')
    
    def unmute():
        keyboard.press_and_release('volume mute') 

    def volume_up():
        keyboard.press_and_release('volume up')

    def volume_down():
        keyboard.press_and_release('volume down')

    if command == "mute":
        mute()
    elif command == "unmute":
        unmute()
    elif command == "volume up":
        volume_up()
    elif command == "volume down":  
        volume_down()

    return True

async def TranslateAndExecute(commands : list[str]):
    
    funcs = []

    for command in commands:
        if command.startswith("open "):
            if "open it" in command:
                pass
            if "open file" == command:
                pass
            else:
                fun = asyncio.to_thread(OpenApp, command.removeprefix("open "))
                funcs.append(fun)

        elif command.startswith("general "):
            pass
        elif command.startswith("realtime "):
            pass
        elif command.startswith("close "):
            fun = asyncio.to_thread(CloseApp, command.removeprefix("close "))
            funcs.append(fun)
        elif command.startswith("play "):
            fun = asyncio.to_thread(PlayYoutube, command.removeprefix("play "))
            funcs.append(fun)
        elif command.startswith("content "):
            fun = asyncio.to_thread(Content, command.removeprefix("content "))
            funcs.append(fun)
        elif command.startswith("google search "):
            fun = asyncio.to_thread(GoogleSearch, command.removeprefix("google search "))
            funcs.append(fun)
        elif command.startswith("youtube search "):
            fun = asyncio.to_thread(YoutubeSearch, command.removeprefix("youtube search "))
            funcs.append(fun)
        elif command.startswith("system "):
            fun = asyncio.to_thread(System, command.removeprefix("system "))
            funcs.append(fun)
        else:
            print(f"No Function Found For {command}")
    
    results = await asyncio.gather(*funcs)

    for result in results:
        if isinstance(result, str):
            yield result
        else:
            yield result

async def Automation(commands: list[str]):
    async for result in TranslateAndExecute(commands):
        pass
    return True