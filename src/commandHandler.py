from src.commandExecuter import CommandExecuter 

class CommandHandler:
    commandExecuter = CommandExecuter()

    def __init__(self):
        pass
    
    @staticmethod
    def getCommandList():
        commandList = [
        "openGoogleChrome",
        "openNotepad",
        {"openGame": {"game": ["ultrakill", "subnautica"]}}
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
        
        if commandTitle.find("openGame") != -1:
            args = commandTitle.split("(")[1]
            args = args.split(")")[0]

            self.commandExecuter.openGame(args)


    def executeStack(self, commands: list):
        for command in commands:
            self.execute(command)