import pyttsx3
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io

class VoiceOutput():
    def __init__(self):
        self.engine = pyttsx3.init()
    
    def say(self, text):
        if text == "":
            return
        
        tts = gTTS(text, lang='pt-br')
        fp = io.BytesIO()
        tts.write_to_fp(fp)

        fp.seek(0)
        audio = AudioSegment.from_file(fp, format="mp3")

        play(audio)
    
    def sayWithPyttsx3(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

voiceOutput = VoiceOutput()


