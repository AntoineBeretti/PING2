from rpi_ws281x import PixelStrip, Color
import time
from logFile import LogFile
log = LogFile()


####################################
# LED STRIP SETTINGS
####################################
GPIO_PIN = 10
NUMBER_OF_LEDS = 176
FREQUENCY = 800000
DMA_CHANNEL = 10
PLAYER_OFFSETS = {
    1: (132, 176),
    2: (88, 132),
    3: (44, 88),
    4: (0, 44)
} 

BRIGHTNESS = 100

class LedStrip:
    def __init__(self, GPIO_PIN, NUMBER_OF_LEDS, FREQUENCY, DMA_CHANNEL, BRIGHTNESS):
        """Init the LED strip."""        
        try:
            self.strip = PixelStrip(NUMBER_OF_LEDS, GPIO_PIN, FREQUENCY, DMA_CHANNEL, invert=False, brightness=BRIGHTNESS)
            self.strip.begin()
            log.write_in_log("INFO", "ledStrip", "__init__", "LED strip initialized")
        except Exception as e:
            log.write_in_log("ERROR", "ledStrip", "__init__", f"Failed to initialize LED strip: {e}")
     
    def setLedStrip(self, color, OFFSET_MIN, OFFSET_MAX):
        """Set the LED strip between OFFSET_MIN and OFFSET_MAX to a color."""
        if OFFSET_MIN < 0 or OFFSET_MAX > self.strip.numPixels() or OFFSET_MIN >= OFFSET_MAX:
            log.write_in_log("ERROR", "LedStrip", "setLedStrip", "Invalid offset")
            return
        if not isinstance(color, int) or color < 0:
            log.write_in_log("ERROR", "LedStrip", "setLedStrip", f"Invalid color value: {color}")
            return
       
        for i in range(OFFSET_MIN, OFFSET_MAX):
            self.strip.setPixelColor(i, color)
        self.strip.show()
    
    def clear(self):
        '''Clear the LED strip'''
        self.setLedStrip(Color(0, 0, 0), 0, self.strip.numPixels())

    def onLedStrip(self, color):
        """Turn on the LED strip."""
        self.setLedStrip(color, 0, self.strip.numPixels())


class PlayerLedStrip:    
    def __init__(self, ledStrip, minAndMax):
        """Init the player LED strip."""
        self.ledStrip = ledStrip
        self.min, self.max = minAndMax
        
    def onPlayer(self, color):
        """Turn on all the LEDs."""
        self.ledStrip.setLedStrip(color, self.min, self.max)
        
    def clearPlayer(self):
        """Clear all the LEDs."""
        self.onPlayer(Color(0, 0, 0))
    
        
'''
from led_strip import LedStrip, PlayerLedStrip
'''

''' 
# Création d'un objet LedStrip (pour un bandeau LED complet)
led_strip = LedStrip(GPIO_PIN, NUMBER_OF_LEDS, FREQUENCY, DMA_CHANNEL, BRIGHTNESS) 

player1led = PlayerLedStrip(led_strip, PLAYER_OFFSETS[1])

player1led.onPlayer(Color(255, 0, 0))
time.sleep(1)
player1led.clearPlayer()

'''