import pn532 as pn

class NFC:
    def __init__(self) -> None:
        self.nfc = pn.PN532()
        self.nfc.setup()

    def readCard(self):
        uid = self.nfc.read()
        return uid
    
    def uidListToStr(self, uidList):
        strUid = ""
        for i in uidList:
            if i != uidList[-1]:
                strUid += str(i)+"_"
            else:
                strUid += str(i)

        return strUid