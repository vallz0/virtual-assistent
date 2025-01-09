import speech_recognition as sr
import pyttsx3
from time import sleep as delay

class Speech:
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.speak_enabled = True

    def speak(self, text: str) -> None:
        """Converts text to speech and prints the text."""
        if self.speak_enabled:
            self.engine.say(text)
            print(text)
            self.engine.runAndWait()

    def listen(self) -> str:
        """Listens for a command and returns the transcribed text."""
        command = ""
        try:
            with sr.Microphone() as source:
                self.speak("Ouvindo..")
                delay(1)
                voice = self.recognizer.listen(source)
                command = self.recognizer.recognize_google(voice, language="pt-br").lower()
        except Exception:
            print("Microfone não identificado..")
        return command

    def toggle_speak(self, enable: bool) -> None:
        """Toggles the speaking functionality."""
        self.speak_enabled = enable
