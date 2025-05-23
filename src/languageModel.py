from gpt4all import GPT4All
from src.commandHandler import CommandHandler

class LanguageModel():
    model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf", model_path="src/models", allow_download=False)

    def __enter__(self):
        return
    
    def __exit__(self, arg, arg2, arg3):
        return

    def __init__(self):
        pass

    def handleInstructions(self, prompt: str) -> str:
         with self.model:
            with self.model.chat_session() as chat:
                commands = str(CommandHandler.getCommandList())
                systemPrompt = f"""
                Siga a risca o prompt a seguir.
                Para meus próximos prompts, vou te enviar uma entrada textual, pedindo ou perguntando algo. Quero que você me retorne a resposta em forma de dicionário, com os atributos "Response" e "Commands" (use aspas duplas).
                Response é uma possível resposta textual para o prompt.
                Commands é uma lista de possíveis comandos a serem executados baseados no prompt e julgados pelos seus títulos descritivos, dentre as opções: {commands}. Caso nenhum comando precise ser executado, deixe lista vazia; Caso mais de um comando precise ser executado, insira-os em ordem na lista;
                Sua resposta deve conter apenas o dicionário descrito."""

                chat.generate(systemPrompt)
                response = chat.generate(prompt)
                
                self.model.close()

                return response
