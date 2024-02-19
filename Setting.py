WIDTH = 130
HEIGHT = 132
running = True

#Database Configuration
import urllib.parse
username = urllib.parse.quote_plus('denredeepak')
password = urllib.parse.quote_plus('Sanjayde12@')
dbHost = "mongodb+srv://denredeepak:Sanjayde12@@attendance.onmby2p.mongodb.net/?retryWrites=true&w=majority"

# Raspberry Pi configuration.
DC = 24
RST = 25
SPI_PORT = 0
SPI_DEVICE = 0
SPEED_HZ = 15

#Display Settings
fontSize = 18
displayColor = (0,0,0)

# Card Database
cardDatabase = {
    "1_04_8_4_147_8_154_252_157_0": "Deepak",
    "1_04_8_4_51_240_33_247_147_0": "Manish"
}