import json
from src.languageModel import LanguageModel
from src.commandHandler import CommandHandler
from src.console.console import console
from src.voiceOutput import voiceOutput

class VoiceCommandInterpreter:
    model: LanguageModel = LanguageModel()
    commandHandler: CommandHandler = CommandHandler()
    
    def __init__(self):
        pass

    def handleInstruction(self, instruction: str):
        with self.model:
            console.sendMessage(f"Instruction: {instruction}")
            response = self.model.handleInstructions(instruction)
            dt = self.getResponseAsDict(response)
            
            res = dt["Response"]
            com = dt["Commands"]

            voiceOutput.say(res)
            console.sendMessage(f"Response: {res}")
            console.sendMessage(f"Commands: {com}")
            self.commandHandler.executeStack(com)
    
    def getResponseAsDict(self, response: str) -> dict:
        try:
            treatedResponse = response.split("{")[1]
            treatedResponse = treatedResponse.split("}")[0]
            treatedResponse = "{" + treatedResponse + "}"

            dt = json.loads(treatedResponse)

            return dt

        except:
            console.sendMessage(f'Ocorreu um erro ao lidar com a requisição "{response}".', "red")
            return {"Response": "", "Commands": []}
