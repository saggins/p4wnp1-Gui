from basemodel import Machine
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from PIL import Image, ImageDraw
import adafruit_ssd1306
from programs import joystick

class Client :
    def __init__(self) -> None:
        # Create the I2C interface.
        i2c = busio.I2C(board.SCL, board.SDA)
        # Create the SSD1306 OLED class.
        disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
        
        
        # Input pins:
        button_A = DigitalInOut(board.D5)
        button_A.direction = Direction.INPUT
        button_A.pull = Pull.UP
        
        button_B = DigitalInOut(board.D6)
        button_B.direction = Direction.INPUT
        button_B.pull = Pull.UP
        
        button_L = DigitalInOut(board.D27)
        button_L.direction = Direction.INPUT
        button_L.pull = Pull.UP
        
        button_R = DigitalInOut(board.D23)
        button_R.direction = Direction.INPUT
        button_R.pull = Pull.UP
        
        button_U = DigitalInOut(board.D17)
        button_U.direction = Direction.INPUT
        button_U.pull = Pull.UP
        
        button_D = DigitalInOut(board.D22)
        button_D.direction = Direction.INPUT
        button_D.pull = Pull.UP
        
        button_C = DigitalInOut(board.D4)
        button_C.direction = Direction.INPUT
        button_C.pull = Pull.UP
        
        
        # Clear display.
        disp.fill(0)
        disp.show()
        
        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        width = disp.width
        height = disp.height
        image = Image.new("1", (width, height))
        
        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)
        
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        
        self.machine : Machine = Machine(
            button_A = button_A,
            button_B = button_B,
            button_L = button_L, 
            button_R = button_R,
            button_U = button_U,
            button_D = button_D,
            button_C = button_C,

            disp = disp,
            draw = draw,
            image = image
        )
    def start(self) :
        while True:
            joystick.execute(self.machine)
