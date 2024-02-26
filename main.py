from Setting import *
from time import sleep
import NFC
import Display
import MongoDB

mdb = MongoDB.MongoDB(dbHost, "Attendance", "attendance", "student")

nfc = NFC.NFC()
disp = Display.Display()

if __name__ == "__main__":
    while running:
        try:
            # Display the greeter
            disp.greeter()
            # Read the card
            card = nfc.uidListToStr(nfc.readCard())
            print(card)

            # Clear the display
            disp.clearDisplay(displayColor)

            # Check if the student is in the database
            if mdb.validateCard(card):
                # Get the name of the student
                name = mdb.getName(card)
                try:
                    if mdb.addAttendance(card):
                        disp.attendanceDone(name)
                    else:
                        disp.cardAlready()
                except Exception as e:
                    print(e)
            else:
                disp.InvalidCard()
            disp.render()
            sleep(1)
        except KeyboardInterrupt:
            running = False
            disp.clearDisplay(displayColor)
            print("Exiting...")

disp.clearDisplay(displayColor)