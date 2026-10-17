import os
import time
import random
import webbrowser
import tempfile
import speech_recognition as sr
from gtts import gTTS
import pygame
import pygetwindow as gw

# Инициализируем звук
pygame.mixer.init()

def speak(text):
    """Озвучка gTTS через временную папку"""
    print(f"\n🤖 Джарвис: {text}")
    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        time.sleep(0.1)
        
        temp_dir = tempfile.gettempdir()
        filename = os.path.join(temp_dir, f"jarvis_{random.randint(1000, 99999)}.mp3")
        
        tts = gTTS(text=text, lang='ru', slow=False)
        tts.save(filename)
        
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
            
    except Exception as e:
        print(f"Ошибка озвучки: {e}")

def listen_continuously():
    """Слушает микрофон в фоновом режиме"""
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.dynamic_energy_threshold = True
    
    with sr.Microphone() as source:
        print("\n👂 [ФОН] Жду фразу с именем «Джарвис»...")
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=7)
            query = r.recognize_google(audio, language="ru-RU").lower()
            print(f"🎤 Услышал: «{query}»")
            return query
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except Exception as e:
            return ""

def process_command(command):
    """Обрабатывает команды, игры и математику"""
    cmd = command.lower()
    
    # Команды выхода
    if any(word in cmd for word in ["выход", "стоп", "пока", "выключись"]):
        speak("Отключаюсь. До встречи!")
        return "exit"
        
    # Математика
    elif any(op in cmd for op in ["плюс", "минус", "умножить", "делить", "+", "-", "*", "/"]):
        try:
            clean_math = cmd.replace("сколько будет", "").replace("плюс", "+").replace("минус", "-").replace("умножить на", "*").replace("умножить", "*").replace("делить на", "/").replace("разделить на", "/")
            allowed_chars = "0123456789+-*/. "
            expression = "".join([c for c in clean_math if c in allowed_chars])
            result = eval(expression)
            speak(f"Результат: {result}")
        except:
            speak("Не смог посчитать этот пример.")
            
    # Запуск игр и мониторов
    elif any(word in cmd for word in ["роблокс", "roblox", "дискорд", "discord", "спотифай", "spotify", "стим", "steam", "кс", "cs2", "майнкрафт", "minecraft", "ютуб", "youtube", "ютюб", "гугл", "google", "монитор", "экраны", "открой", "включи"]):
        open_apps(cmd)
        
    elif "привет" in cmd:
        speak("Привет! Какую игру запускаем?")
        
    else:
        speak("Я услышал тебя, но пока умею запускать игры, открывать приложения и считать примеры.")
    
    return "continue"

def arrange_monitors():
    """Открывает YouTube и Roblox на разных мониторах"""
    speak("Выполняю! Настраиваю рабочие экраны.")
    webbrowser.open("https://www.youtube.com")
    time.sleep(1)
    try:
        os.system("start roblox-player:")
    except:
        webbrowser.open("https://www.roblox.com")
        
    time.sleep(3)
    
    try:
        windows = gw.getWindowsWithTitle('YouTube')
        roblox_windows = gw.getWindowsWithTitle('Roblox')
        
        if windows:
            yt_win = windows[0]
            if yt_win.isMinimized:
                yt_win.restore()
            yt_win.moveTo(0, 0)
            
        if roblox_windows:
            rbx_win = roblox_windows[0]
            if rbx_win.isMinimized:
                rbx_win.restore()
            rbx_win.moveTo(1920, 0)
            
        print("✅ Окна распределены по экранам!")
    except Exception as e:
        print(f"Ошибка выравнивания окон: {e}")

def open_apps(command):
    """Запускает программы и игры"""
    if any(word in command for word in ["монитор", "экраны", "два монитора", "пара"]):
        arrange_monitors()

    elif any(word in command for word in ["роблокс", "roblox"]):
        speak("Запускаю Роблокс.")
        try:
            os.system("start roblox-player:")
        except:
            webbrowser.open("https://www.roblox.com")

    elif any(word in command for word in ["дискорд", "discord"]):
        speak("Включаю Дискорд.")
        try:
            discord_path = os.path.expanduser("~\\AppData\\Local\\Discord")
            if os.path.exists(discord_path):
                for folder in os.listdir(discord_path):
                    if folder.startswith("app-"):
                        exe = os.path.join(discord_path, folder, "Discord.exe")
                        if os.path.exists(exe):
                            os.startfile(exe)
                            return
            os.system("start discord:")
        except Exception as e:
            print(f"Ошибка Discord: {e}")

    elif any(word in command for word in ["спотифай", "spotify", "музык"]):
        speak("Включаю Спотифай.")
        try:
            spotify_path = os.path.expanduser("~\\AppData\\Roaming\\Spotify\\Spotify.exe")
            if os.path.exists(spotify_path):
                os.startfile(spotify_path)
            else:
                os.system("start spotify:")
        except Exception as e:
            print(f"Ошибка Spotify: {e}")

    elif any(word in command for word in ["стим", "steam"]):
        speak("Запускаю Стим.")
        try:
            os.system("start steam://")
        except Exception as e:
            print(f"Ошибка Steam: {e}")

    elif any(word in command for word in ["кс", "кэски", "cs2", "cs 2"]):
        speak("Запускаю КС 2.")
        try:
            os.system("start steam://run/730")
        except Exception as e:
            print(f"Ошибка КС2: {e}")

    elif any(word in command for word in ["майнкрафт", "minecraft", "майн"]):
        speak("Запускаю Майнкрафт.")
        try:
            os.system("start minecraft-launcher:")
        except Exception as e:
            print(f"Ошибка Minecraft: {e}")

    elif any(word in command for word in ["ютуб", "youtube", "ютюб"]):
        speak("Открываю Ютуб.")
        webbrowser.open("https://www.youtube.com")

    elif any(word in command for word in ["гугл", "google"]):
        speak("Открываю Гугл.")
        webbrowser.open("https://www.google.com")

# Главный запуск
if __name__ == "__main__":
    print("=" * 40)
    print(" СИСТЕМА ДЖАРВИС АКТИВНА ")
    print("=" * 40)
    
    speak("Система активна.")
    
    while True:
        speech = listen_continuously()
        
        if not speech:
            continue
            
        # Если в услышанной фразе есть слово "джарвис"
        if "джарвис" in speech:
            # Сразу очищаем фразу от имени, оставляя то, что ты сказал вместе с ним
            command = speech.replace("джарвис", "").strip()
            
            if not command:
                speak("Да, слушаю!")
                continue
                
            action = process_command(command)
            if action == "exit":
                break