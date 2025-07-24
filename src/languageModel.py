from gpt4all import GPT4All
from src.console.console import console
from src.commandHandler import CommandHandler
from src.config.modelPrompt import getPrompt

class LanguageModel():
    modelName = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"  #"nous-hermes-llama2-13b.Q6_K.gguf" #"Meta-Llama-3-8B-Instruct.Q4_0.gguf"
    #model = GPT4All(model_name=modelName, model_path="src/models", allow_download=False)

    def __enter__(self):
        return
    
    def __exit__(self, arg, arg2, arg3):
        return

    def __init__(self):
        console.sendMessage("Carregando modelo...", "yellow")
        self.model = GPT4All(model_name=self.modelName, model_path="src/models", allow_download=False)
        console.sendMessage("Carregando chat...", "yellow")
        self.chat = self.model.chat_session()
        self.chat_model = self.chat.__enter__()

        console.sendMessage("Configurando modelo...", "yellow")
        
        commands = str(CommandHandler.getCommandList())
        systemPrompt = getPrompt("promptV1")
        console.sendMessage("- Enviando systemPrompt...", "yellow")
        self.chat_model.generate(systemPrompt)
        console.sendMessage("- systemPrompt enviado com sucesso!", "yellow")
        console.sendMessage("Modelo configurado.", "green")

    def handleInstructions(self, prompt: str) -> str:
        response = self.chat_model.generate(prompt)
        return response
