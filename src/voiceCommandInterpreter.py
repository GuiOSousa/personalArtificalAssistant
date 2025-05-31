import json
from src.languageModel import LanguageModel
from src.commandHandler import CommandHandler



class VoiceCommandInterpreter:
    model: LanguageModel = LanguageModel()
    commandHandler: CommandHandler = CommandHandler()
    
    def __init__(self):
        pass

    def handleInstruction(self, instruction: str):
        with self.model:
            response = self.model.handleInstructions(instruction)
            dt = self.getResponseAsDict(response)

            print(dt["Response"])
            self.commandHandler.executeStack(dt["Commands"])
    
    def getResponseAsDict(self, response: str) -> dict:
        treatedResponse = response.split("{")[1]
        treatedResponse = treatedResponse.split("}")[0]
        treatedResponse = "{" + treatedResponse + "}"

        dt = json.loads(treatedResponse)

        return dt
