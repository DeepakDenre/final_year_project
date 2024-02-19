from Setting import *
from time import sleep
import NFC
import Display
import MongoDB

mdb = MongoDB.MongoDB(dbHost, "Attendance", "Attendance")
nfc = NFC.NFC()
disp = Display.Display()

if __name__ == "__main__":
    while running:
        try:
            disp.greeter()
            card = nfc.uidListToStr(nfc.readCard())
            print(card)
            disp.clearDisplay(displayColor)
            
            if card in str(cardDatabase.keys()):
                print("Hi "+cardDatabase.get(card))
                disp.attendanceDone(card)

            disp.render()
            sleep(1)
        except KeyboardInterrupt:
            running = False
            disp.clearDisplay(displayColor)
            print("Exiting...")

disp.clearDisplay(displayColor)