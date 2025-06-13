import cv2
import google.generativeai as genai
from PIL import Image, PngImagePlugin
from dotenv import load_dotenv
import io
import os

class ImageSystem():
    def __init__(self):
        self.capturePath = "src/savedFiles/"
        self.cam = cv2.VideoCapture(0)
        
        load_dotenv()

        genai.configure(api_key=os.environ.get("GOOGLE_AI_KEY"))

    def capture(self):
        if not self.cam.isOpened():
            exit()

        ret, frame = self.cam.read()
        self.cam.release()

        if not ret:
            print("Erro ao capturar imagem da webcam")
            exit()
        
        return frame
    
    def captureAndSave(self):
        frame = self.capture()
        cv2.imwrite(self.capturePath + "image.jpg", frame)

        cv2.imshow("Image", frame)
        cv2.waitKey(0)
    
    def captureAndDescribe(self, prompt):
        frame = self.capture()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame_rgb)

        model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")
        response = model.generate_content([prompt, image])

        print(response.text)
