#!/usr/bin/python3.9
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

                    # Add the attendance and check if it was successful
                    if mdb.addAttendance(card):

                        # Display the attendance done
                        disp.attendanceDone(name)
                    else:

                        # Display the attendance already done
                        disp.cardAlready()
                except Exception as e:
                    print(e)
            else:

                # Display the invalid card
                disp.InvalidCard()
            
            # render the display
            disp.render()
            sleep(2)
        except KeyboardInterrupt:
            running = False
            disp.clearDisplay(displayColor)
            print("Exiting...")

disp.clearDisplay(displayColor)