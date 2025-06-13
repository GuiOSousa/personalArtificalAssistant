import subprocess

from src.modules.lightSystem import LightSystem
from src.modules.spotify import Spotify
from src.modules.imageSystem import ImageSystem

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
    
    def turnOnLight(self):
        l = LightSystem()
        l.turnOnLight()
    
    def turnOffLight(self):
        l = LightSystem()
        l.turnOffLight()
    
    def playSong(self, songTitle: str):
        s = Spotify()
        s.playSong(songTitle)
    
    def addSongToQueue(self, songTitle: str):
        s = Spotify()
        s.addSongToQueue(songTitle)
    
    def captureAndSaveImage(self):
        i = ImageSystem()
        i.captureAndSave()
    
    def captureAndDescribeImage(self, prompt):
        i = ImageSystem()
        i.captureAndDescribe(prompt)