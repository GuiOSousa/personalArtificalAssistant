import speech_recognition as sr
from googletrans import Translator
from src.voiceCommandInterpreter import VoiceCommandInterpreter
from src.console.console import console

class VoiceHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.translator = Translator()
        self.interpreter = VoiceCommandInterpreter()
        self.microphone_index = 1
        self.stop_listening = None

    def getAllAudioSources(self):
        console.sendMessage("Dispositivos de áudio disponíveis:")
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            console.sendMessage(f"- {index}: {name}")

    def getCurrentAudioSource(self):
        return self.microphone_index

    def startListening(self):
        console.sendMessage("Iniciando configuração do Listener...", "yellow")
        self.recognizer.pause_threshold = 1.8
        self.recognizer.energy_threshold = 300
        self.recognizer.non_speaking_duration = 0.5
        mic = sr.Microphone(device_index=self.microphone_index)

        with mic as source:
            console.sendMessage("Ajustando para ruído ambiente...", "yellow")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
        
        # Inicia escuta em background com a função callback
        self.stop_listening = self.recognizer.listen_in_background(
            mic, self.audioCallback, phrase_time_limit=8
        )

        console.sendMessage("Listener configurado!", "green")

    def stopListening(self):
        if self.stop_listening:
            self.stop_listening(wait_for_stop=False)

    def audioCallback(self, recognizer, audio):
        try:
            text = recognizer.recognize_google(audio, language='pt-BR')
            console.sendMessage(f"Listener: {text}")
            self.handleCommand(text)
        except sr.UnknownValueError:
            pass
            #print("❌ Não entendi o que você disse.")
        except sr.RequestError as e:
            pass
            #print(f"❌ Erro na solicitação: {e}")

    def handleCommand(self, text: str):
        self.interpreter.handleInstruction(text)

    def inputCommand(self):
        while True:
            text = input("Digite o comando: ")
            self.handleCommand(text)
