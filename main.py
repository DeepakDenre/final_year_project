from Setting import *
from time import sleep
import NFC
import Display


nfc = NFC.NFC()
disp = Display.Display()

if __name__ == "__main__":
    while running:
        try:
            disp.greeter()
            card = nfc.uidListToStr(nfc.readCard())
            print(card)
            disp.clearDisplay(displayColor)
            disp.attendanceDone(card)
            disp.render()
            sleep(1)
        except KeyboardInterrupt:
            running = False
            disp.clearDisplay(displayColor)
            print("Exiting...")

disp.clearDisplay(displayColor)