# Jarvis Voice Assistant

A small Russian-language voice assistant for Windows. It listens for the wake word **«Джарвис»**, speaks responses aloud, opens selected apps and websites, and handles simple arithmetic.

## Features

- Recognizes Russian speech through the Google Speech Recognition service.
- Replies in Russian using Google Text-to-Speech (gTTS).
- Opens Roblox, Discord, Spotify, Steam, Counter-Strike 2, Minecraft Launcher, YouTube, and Google.
- Can open YouTube and Roblox and position their windows on a two-monitor setup.
- Evaluates simple arithmetic expressions.
- Stops when it hears a command containing «выход», «стоп», «пока», or «выключись».

## Requirements

- Windows
- Python 3
- A working microphone and speakers
- An internet connection for speech recognition and speech synthesis
- Any apps you want Jarvis to launch must already be installed

## Setup

Open PowerShell in the project folder and run:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install SpeechRecognition gTTS pygame PyGetWindow PyAudio
```

If PowerShell blocks virtual-environment activation, you can install the packages with `python -m pip install ...` without activating it, or use Command Prompt and run `.venv\Scripts\activate.bat`.

## Run

```powershell
python jarvis.py
```

Allow microphone access if Windows asks. Say «Джарвис» followed by a command, for example:

- «Джарвис, открой YouTube»
- «Джарвис, запусти Discord»
- «Джарвис, сколько будет 12 плюс 7»
- «Джарвис, стоп»

For the two-monitor layout, say «Джарвис, два монитора». The current implementation places the second window at a fixed horizontal position of 1920 pixels, so the layout assumes a 1920-pixel-wide primary display.

## Notes

- Speech recognition and gTTS send audio or text to online Google services; this project does not work fully offline.
- The assistant is an early prototype. It listens in repeated intervals and ignores phrases it cannot recognize.
- Microphone support depends on PyAudio being available for your Python installation. If installing PyAudio fails, install a compatible PyAudio build for your Python version and Windows environment, then rerun the install command.