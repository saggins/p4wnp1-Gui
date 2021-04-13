from PIL.Image import Image
from PIL.ImageDraw import Draw
from adafruit_ssd1306 import SSD1306_I2C
from digitalio import DigitalInOut
from pydantic.main import BaseModel

class Machine( BaseModel):
    button_A: DigitalInOut
    button_B: DigitalInOut
    button_L: DigitalInOut
    button_R: DigitalInOut
    button_U: DigitalInOut
    button_D: DigitalInOut
    button_C: DigitalInOut

    disp: SSD1306_I2C
    draw: Draw
    image: Image