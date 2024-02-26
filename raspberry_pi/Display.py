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
            print("Using "+str(os.path.dirname(__file__))+"/Comfortaa.ttf font file...")
            self.font = ImageFont.truetype(str(os.path.dirname(__file__))+"/Comfortaa.ttf", fontSize)
        except:
            print("Using default font file...")
            self.font = ImageFont.load_default(fontSize)
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
        print("Displaying Loading...")
        self.clearDisplay(displayColor)
        self.displayText("Connecting", 5, HEIGHT/4*1, (255, 255, 255))
        self.displayText("to", 5, HEIGHT/4*2, (255, 255, 255))
        self.displayText("database!...", 5, HEIGHT/4*3, (255, 255, 255))
        self.render()

    def greeter(self):
        print("Displaying Greeter...")
        self.clearDisplay(displayColor)
        self.displayText("Hi", 50, HEIGHT/4*1, (255, 255, 255))
        self.displayText("Place Your", 10, HEIGHT/4*2, (255, 255, 255))
        self.displayText(" card", 30, HEIGHT/4*3, (255, 255, 255))
        self.render()

    def attendanceDone(self, name):
        print("Displaying Attendance Done...")
        self.displayText("Hi ", 5, HEIGHT/6*1, (255, 255, 255))
        self.displayText(str(name).split(" ")[0], 5, HEIGHT/6*2, (255, 255, 255))
        self.displayText("Your", 5, HEIGHT/6*3, (255, 255, 255))
        self.displayText("Attendance", 5, HEIGHT/6*4, (255, 255, 255))
        self.displayText("Marked!", 5, HEIGHT/6*5, (255, 255, 255))

    def InvalidCard(self):
        print("Displaying Card Not Found...")
        self.displayText("Invalid", 5, HEIGHT/3*1, (255, 255, 255))
        self.displayText("Card !", 5, HEIGHT/3*2, (255, 255, 255))

    def attendanceAlready(self):
        print("Displaying Card Already...")
        self.displayText("Attendance", 5, HEIGHT/4*1, (255, 255, 255))
        self.displayText("Already", 5, HEIGHT/4*2, (255, 255, 255))
        self.displayText("Marked!", 5, HEIGHT/4*3, (255, 255, 255))