import os
import webbrowser
import datetime

class Commands:
    def __init__(self, speech) -> None:
        self.speech = speech

    def execute(self, prompt: str) -> bool:
        """Executes the command based on the voice prompt."""
        if 'que horas são?' in prompt:
            self._tell_time()

        elif 'abrir calculadora' in prompt:
            self._open_calculator()

        elif 'abrir prompt de comando' in prompt:
            self._open_cmd()

        elif 'abrir google' in prompt:
            self._open_google()

        elif 'criar lista de tarefas' in prompt:
            self._create_todo_list()

        elif 'pesquisar na internet' in prompt:
            self._search_web()

        elif 'definir lembrete' in prompt:
            self._set_reminder()

        elif 'tchau' in prompt:
            self._say_goodbye()
            return False

        elif "pare de falar" in prompt:
            self.speech.toggle_speak(False)

        elif "volte a falar" in prompt:
            self.speech.toggle_speak(True)

        return True

    def _tell_time(self) -> None:
        """Tells the current time."""
        now = datetime.datetime.now()
        hour_format = now.strftime("%I:%M %p").replace("AM", "da manhã").replace("PM", "da tarde")
        self.speech.speak(f'Agora são {hour_format}')

    def _open_calculator(self) -> None:
        """Opens the calculator application."""
        self.speech.speak("Abrindo a Calculadora")
        os.startfile(r"C:\\Windows\\System32\\calc.exe")

    def _open_cmd(self) -> None:
        """Opens the command prompt."""
        self.speech.speak("Abrindo o prompt de comandos")
        os.startfile(r"C:\\Windows\\System32\\cmd.exe")

    def _open_google(self) -> None:
        """Opens Google in a web browser."""
        self.speech.speak("Abrindo o Google")
        webbrowser.open("google.com")

    def _say_goodbye(self) -> None:
        """Says goodbye and ends the program."""
        self.speech.speak("Tchau, até mais!")

    def _create_todo_list(self) -> None:
        """Creates a to-do list by adding tasks."""
        self.speech.speak("O que você quer adicionar à sua lista de tarefas?")
        task = self.speech.recognize_speech()

        with open('todo.txt', 'a') as f:
            f.write(f"{datetime.datetime.now()} - {task}\n")
        self.speech.speak("Tarefa adicionada")

    def _search_web(self) -> None:
        """Searches the web based on user input."""
        self.speech.speak("O que você gostaria de pesquisar?")
        query = self.speech.recognize_speech()
        url = f"https://www.google.com/search?q={query}"

        webbrowser.open(url)
        self.speech.speak(f"Aqui estão os resultados para {query}")

    def _set_reminder(self) -> None:
        """Sets a reminder based on user input."""
        self.speech.speak("O que eu devo lembrá-lo?")
        task = self.speech.recognize_speech()
        self.speech.speak("Em quantos minutos?")
        mins = self.speech.recognize_speech()
        mins = int(mins)
        reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=mins)

        with open('reminders.txt', 'a') as f:
            f.write(f"{reminder_time} - {task}\n")
        self.speech.speak(f"Lembrete definido para daqui a {mins} minutos")
