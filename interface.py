from terminal import Terminal
from speech import Speech
from commands import Commands
from time import sleep as delay

class Interface:
    def __init__(self) -> None:
        self.terminal = Terminal()
        self.speech = Speech()
        self.commands = Commands(self.speech)
        self.leave = False

    def start(self) -> None:
        """Starts the main interface and shows options."""
        self.terminal.resize(45, 30)
        self.terminal.clear()
        print("Assistente Virtual")
        print("O que deseja escolher hoje?")
        delay(1)
        print('\n[1] Modo por voz')
        print('[2] Modo por digitação')
        print('[3] ChatBot')
        print('[4] Sair')

    def run(self) -> None:
        """Runs the main loop to handle user input."""
        while not self.leave:
            self.start()
            choice = input('Qual sua escolha? \n User: ')
            delay(1)
            self.handle_choice(choice)

    def handle_choice(self, choice: str) -> None:
        """Handles user choice and navigates accordingly."""
        if choice == "4":
            print("Saindo...")
            delay(1)
            self.leave = True

        elif choice == "1":
            print('Modo de voz ativado!')
            self.run_voice_mode()

        elif choice == "2":
            print('Modo de digitação ativado!')

        elif choice == "3":
            print("Abrindo chatbot")

        else:
            print("Opção inválida '-")

    def run_voice_mode(self) -> None:
        """Runs voice command mode."""
        while True:
            prompt = self.speech.listen()
            if not self.commands.execute(prompt):
                break
