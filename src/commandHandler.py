from src.commandExecuter import CommandExecuter 

class CommandHandler:
    commandExecuter = CommandExecuter()

    def __init__(self):
        pass
    
    @staticmethod
    def getCommandList():
        commandList = [
        "openGoogleChrome", "openNotepad"
        ]
        return commandList

    def execute(self, commandTitle: str):
        match commandTitle:
            case "functionExample":
                self.commandExecuter.functionExample()
            case "openNotepad":
                self.commandExecuter.openNotepad()
            case "openGoogleChrome":
                self.commandExecuter.openGoogleChrome()
    
    def executeStack(self, commands: list):
        for command in commands:
            self.execute(command)
