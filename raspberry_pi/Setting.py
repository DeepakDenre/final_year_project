WIDTH = 130
HEIGHT = 132
running = True

#Database Configuration
import urllib.parse
username = urllib.parse.quote_plus('guptammanish04')
password = urllib.parse.quote_plus('Manish04')
dbHost = "mongodb+srv://%s:%s@cluster0.eje4awb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Raspberry Pi configuration.
DC = 24
RST = 25
SPI_PORT = 0
SPI_DEVICE = 0
SPEED_HZ = 15

#Display Settings
fontSize = 24
displayColor = (0,0,0)
color={
    "white":(255,255,255),
    "black":(0,0,0),
    "red":(255,0,0),
    "green":(0,255,0),
    "blue":(0,0,255)

}

# Card Database
cardDatabase = {
    "1_04_8_4_147_8_154_252_157_0": "Deepak",
    "1_04_8_4_51_240_33_247_147_0": "Manish"
}