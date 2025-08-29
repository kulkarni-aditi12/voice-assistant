Voice Assistant

This project is a Python-based voice assistant that processes voice commands and performs basic tasks such as opening commonly used websites.

Features:
Captures voice input using a microphone.
Converts speech to text with Google Speech Recognition.
Provides spoken feedback through pyttsx3.
Executes the following commands:
    Open YouTube,
    Open Netflix,
    Open Google,
    Exit/Stop the assistant.

Requirements:
Python 3

Packages:
speechrecognition,
pyttsx3,
pyaudio

Install the required dependencies with:
pip install speechrecognition pyttsx3 pyaudio

Usage:
Run the program using:
python voice.py

After execution, the assistant will prompt for a voice command. Supported commands include opening websites (YouTube, Netflix, Google) and terminating the program.
