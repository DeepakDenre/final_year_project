import ST7735 as TFT
import Adafruit_GPIO.SPI as SPI
from PIL import ImageFont
from Setting import *


class Display:

    # Initialize the display
    def __init__(self):
        self.disp = TFT.ST7735(
            dc=DC,
            height=HEIGHT,
            width=WIDTH,
            spi=SPI.SpiDev(
                SPI_PORT,
                SPI_DEVICE,
                max_speed_hz=SPEED_HZ
            )
        )
        self.disp.begin()
        self.draw = self.disp.draw()
        try:
            self.font = ImageFont.truetype("Comfortaa.ttf", fontSize)
        except:
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

    def greeter(self):
        self.clearDisplay(displayColor)
        self.displayText("Hi ", 50, 30, (255, 255, 255))
        self.displayText("Place Your", 10, 60, (255, 255, 255))
        self.displayText(" card", 30, 90, (255, 255, 255))
        self.render()

    def attendanceDone(self, card):
        self.displayText("Hi ", 5, 128/5*0, (255, 255, 255))
        self.displayText(cardDatabase.get(card), 5, 128/5*1, (255, 255, 255))
        self.displayText("Your", 5, 128/5*2, (255, 255, 255))
        self.displayText("Attendance", 5, 128/5*3, (255, 255, 255))
        self.displayText("Done!", 5, 128/5*4, (255, 255, 255))
        