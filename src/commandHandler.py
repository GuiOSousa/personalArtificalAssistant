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
        {"openGame": {"game": ["ultrakill", "subnautica"]}},
        "turnOnLight",
        "turnOffLight",
        {"playSong": {"songTitle": "DYNAMIC"}},
        {"addSongToQueue": {"songTitle": "DYNAMIC"}},
        "pauseSong",
        "resumeSong",
        "captureAndSaveImage",
        {"captureAndDescribeImage": {"prompt": "DYNAMIC"}},
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
            case "turnOnLight":
                self.commandExecuter.turnOnLight()
            case "turnOffLight":
                self.commandExecuter.turnOffLight()
            case "pauseSong":
                self.commandExecuter.pauseSong()
            case "resumeSong":
                self.commandExecuter.resumeSong()
            case "captureAndSaveImage":
                self.commandExecuter.captureAndSaveImage()
            
        
        if commandTitle.find("openGame") != -1:
            args = commandTitle.split("(")[1]
            args = args.split(")")[0]

            self.commandExecuter.openGame(args)
        
        elif self.isCommand(commandTitle, "playSong"):
            self.commandExecuter.playSong(self.getCommandArgs(commandTitle))
        
        elif self.isCommand(commandTitle, "addSongToQueue"):
            self.commandExecuter.addSongToQueue(self.getCommandArgs(commandTitle))
        
        elif self.isCommand(commandTitle, "captureAndDescribeImage"):
            self.commandExecuter.captureAndDescribeImage(self.getCommandArgs(commandTitle))

    def isCommand(self, string: str, target: str):
        return string.find(target) != -1

    def getCommandArgs(self, command: str):
        args = command.split("(")[1]
        args = args.split(")")[0]
        return args

    def executeStack(self, commands: list):
        for command in commands:
            self.execute(command)