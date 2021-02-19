import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from PIL import Image, ImageDraw
import adafruit_ssd1306
import asyncio

class Client:
    def __init__(self):
        # Create the I2C interface.
        self.i2c = busio.I2C(board.SCL, board.SDA)
        # Create the SSD1306 OLED class.
        self.disp = adafruit_ssd1306.SSD1306_I2C(128, 64, self.i2c)
        
        self.boardID = {"D5" : "A", "D6" : "B", "D27" : "L", "D23" : "R", "D17" : "U", "D22" : "D", "D4" : "C"}
        """
        Itteratoring through dictionary to intialize buttons :D
            button_A = DigitalInOut(board.D5)
            button_A.direction = Direction.INPUT
            button_A.pull = Pull.UP
            self.button_A = button_A
        """
        for bID in self.boardID :
            setattr(self, "button_" + bID, DigitalInOut("board" + self.boardID[ bID ]) )
            newButton = getattr(self, "button_" + bID)
            newButton.direction = Direction.INPUT
            newButton.pull = Pull.UP
            newButton.bid = bID

        self.loop = asyncio.get_event_loop()
        self.listener = []

    def start(self) :
        # Clear display.
        self.disp.fill(0)
        self.disp.show()
        self.loop.run_forever(self.checkInput)

    def runProgram(self):
        pass
    def getBaseDraw (self) :
        width = self.disp.width
        height = self.disp.height
        self.image = Image.new("1", (width, height))
        # Get drawing object to draw on image.
        self.draw = ImageDraw.Draw(self.image)
        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, width, height), outline=0, fill=0)
    def setBaseDraw(self, draw):
        self.draw = draw
    def draw(self):
        self.disp.image(self.image)
        self.disp.show()

        

    def event (self, coro):
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError('event registered must be a coroutine function')
        setattr(self, coro.__name__, coro)

    def notify(self, name, *args, **kwargs) :
        getattr(self, "coro" + name) (*args, **kwargs)
    
    async def checkInput (self) :
        for bID in self.boardID:
            button = self.boardID[bID]
            if (button.value):
                self.notify("offButton", button, self)
            else :
                self.notify("onButton", button, self)

                

