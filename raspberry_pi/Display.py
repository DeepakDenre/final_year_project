import ST7735 as TFT
import Adafruit_GPIO.SPI as SPI
from PIL import ImageFont
from Setting import *
import os

class Display:

    # Initialize the display
    def __init__(self):
        self.disp = TFT.ST7735(
            dc=DC,
            height=HEIGHT,
            width=WIDTH,
            rst=RST,
            spi=SPI.SpiDev(
                SPI_PORT,
                SPI_DEVICE,
                max_speed_hz=SPEED_HZ
            )
        )
        self.disp.begin()
        self.draw = self.disp.draw()
        try:
            print("Using "+str(os.path.dirname(__file__))+"/MOR.ttf font file...\n")
            self.font = ImageFont.truetype(str(os.path.dirname(__file__))+"/MOR.ttf", fontSize)
        except:
            print("Using default font file...\n")
            self.font = ImageFont.load_default()
        self.clearDisplay(displayColor)

    # Clear the display
    def clearDisplay(self, color=(0,0,0)):
        self.disp.clear(color)
        self.render()

    # Display text on the screen
    def displayText(self, text, x=0, y=0, color=(255,255,255)):
        self.draw.text((x, y), text, font=self.font, fill=color)

    # Render the display
    def render(self):
        self.disp.display()

    def lodingScreen(self):
        print("Displaying Loading...\n")
        self.clearDisplay(color["blue"])
        self.displayText("Connecting", 5, HEIGHT/3*0, color["black"])
        self.displayText("to", 5, HEIGHT/3*1,  color["black"])
        self.displayText("database!...", 5, HEIGHT/3*2, color["black"])
        self.render()

    def greeter(self):
        print("Displaying Greeter...\n")
        self.clearDisplay(color["blue"])
        self.displayText("Hi", 50, HEIGHT/3*0,  color["black"])
        self.displayText("Place Your", 10, HEIGHT/3*1,  color["black"])
        self.displayText(" card", 30, HEIGHT/3*2,  color["black"])
        self.render()

    def attendanceDone(self, name):
        print("Displaying Attendance Done...\n")
        self.clearDisplay(color["green"])
        self.displayText("Hi ", 5, HEIGHT/5*0,  color["black"])
        self.displayText(str(name).split(" ")[0], 5, HEIGHT/5*1,  color["black"])
        self.displayText("Your", 5, HEIGHT/5*2,  color["black"])
        self.displayText("Attendance", 5, HEIGHT/5*3,  color["black"])
        self.displayText("Marked!", 5, HEIGHT/5*4,  color["black"])

    def InvalidCard(self):
        print("Displaying Card Not Found...\n")
        self.clearDisplay(color["red"])
        self.displayText("Invalid", 5, HEIGHT/4*1,  color["black"])
        self.displayText("Card !", 5, HEIGHT/4*2,  color["black"])

    def attendanceAlready(self,name):
        print("Displaying Card Already...\n")
        self.clearDisplay(color["red"])
        self.displayText((str(name).split(" ")[0])+"'s", 5, HEIGHT/4*0, color["black"])
        self.displayText("Attendance", 5, HEIGHT/4*1, color["black"])
        self.displayText("Already", 5, HEIGHT/4*2,  color["black"])
        self.displayText("Marked!", 5, HEIGHT/4*3, color["black"])

    def connectionError(self):
        print("Displaying Connection Error...\n")
        self.clearDisplay(color["red"])
        self.displayText("Connection", 5, HEIGHT/3*0,  color["black"])
        self.displayText("Error!", 5, HEIGHT/3*1,  color["black"])
        self.displayText("Retrying...", 5, HEIGHT/3*2, color["black"])
        self.render()