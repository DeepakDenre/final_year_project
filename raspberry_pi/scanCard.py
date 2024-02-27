import NFC

nfc = NFC.NFC()

file = open("card.txt", "w")
cardList=[]

scanning= True

while scanning:
    try:
        print("Scanning Card!...")
        card = nfc.uidListToStr(nfc.readCard())
        if card != "0225_22_00000000":
            cardList.append(card)
        print(cardList)
    except KeyboardInterrupt:
        scanning = False

for card in cardList:
    file.write(card + "\n")
file.close()

print("Card Scanned and Saved!")