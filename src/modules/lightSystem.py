import tinytuya
from dotenv import load_dotenv
import os

class LightSystem:
    def __init__(self):
        load_dotenv()
    
    def getDevice(self, deviceName):
        match deviceName:
            case "BedroomLampshade":
                device = tinytuya.BulbDevice(os.environ.get("BULB_ID"), os.environ.get("BULB_IP"), os.environ.get("BULB_KEY"))
                device.set_version(3.5)
                return device

    def turnOnLight(self):
        device = self.getDevice("BedroomLampshade")
        device.turn_on()

    def turnOffLight(self):
        device = self.getDevice("BedroomLampshade")
        device.turn_off()

l = LightSystem()
l.turnOffLight()

