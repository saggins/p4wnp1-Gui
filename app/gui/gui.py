import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from PIL import Image, ImageDraw
import adafruit_ssd1306

class Gui:

    def start () :
        Gui.disp.show()
        
    def clearDisplay():
        Gui.disp.fill(0)
        Gui.disp.show()
        print ("cleared display!")

    def __init__(self):
        self.clearDisplay()
        self.start()
