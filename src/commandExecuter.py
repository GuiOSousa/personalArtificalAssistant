import subprocess

class CommandExecuter:
    def __init__(self):
        pass
    
    def functionExample(self):
        print("Novas funções podem ser facilmente adicionadas.")

    def openNotepad(self):
        subprocess.Popen("notepad.exe")
    
    def openGoogleChrome(self):
        subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")

    def openGame(self, game: str):
        match game:
            case "ultrakill":
                subprocess.Popen("C:\\Program Files (x86)\\Steam\\steamapps\\common\\ultrakill\\ultrakill.exe")
            case "subnautica":
                subprocess.Popen("C:\Program Files (x86)\Steam\steamapps\common\Subnautica\Subnautica.exe")