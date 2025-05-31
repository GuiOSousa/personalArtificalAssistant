import speech_recognition as sr
from googletrans import Translator

from src.voiceCommandInterpreter import VoiceCommandInterpreter

class VoiceHandler:
    recognizer = sr.Recognizer()
    translator = Translator()
    interpreter = VoiceCommandInterpreter()

    def __init__(self):
        pass

    def getAllAudioSources(self):
        print("Dispositivos de entrada de áudio disponíveis:")
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print(f"{index}: {name}")

    def getCurrentAudioSource(self):
        return 1

    def captureAudio(self):
        with sr.Microphone(device_index=1) as source:
            recognizer = sr.Recognizer()
            recognizer.pause_threshold = 1.5
            print("Ajustando para o ruído ambiente...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("O que você deseja?")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio, language='pt-BR')
                text = str(text)
                print(f"{text}")
                print("Aguarde...")
                self.handleCommand(text)

            except sr.UnknownValueError:
                print("Não entendi o que você disse.")
                self.captureAudio()
            except sr.RequestError as e:
                print(f"Erro na solicitação: {e}")
    
    def handleCommand(self, text: str):
        self.interpreter.handleInstruction(text)
