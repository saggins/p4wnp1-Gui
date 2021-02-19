from asyncio.base_events import BaseEventLoop
from asyncio.events import AbstractEventLoop, get_event_loop
from app.client import Client
from app.gui.gui import Gui
from PIL import Image, ImageDraw
from digitalio import DigitalInOut, Direction, Pull
import asyncio
class BonnetButtons (Gui):
    def __init__(self, client : Client):
        super().__init__()
        self.client = client

    @Client.event
    async def onButton (button : DigitalInOut, client : Client) :
        draw = client.getBaseDraw()
        if (button.bID == "U"):
            draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=1)  # Up filled
        if (button.bID == "L"):
            draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=1)  # left filled
        if (button.bID == "R"):
            draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=1)  # right filled
        if (button.bID == "D"):
            draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=1)  # down filled
        if (button.bID == "C"):
            draw.rectangle((20, 22, 40, 40), outline=255, fill=1)  # center filled
        if (button.bID == "A"):
            draw.ellipse((70, 40, 90, 60), outline=255, fill=1)  # A button filled
        if (button.bID == "B"):
            draw.ellipse((100, 20, 120, 40), outline=255, fill=1)  # B button filled
        client.draw()
    @Client.event
    async def offButton(button : DigitalInOut, client : Client) :
        draw = client.getBaseDraw()
        if (button.bID == "U"):
            draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=0)  # Up        if (button.bID == "L"):
        if (button.bID == "L"):
            draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=0)  # left
        if (button.bID == "R"):
            draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=0)  # right
        if (button.bID == "D"):
            draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=0)  # downs
        if (button.bID == "C"):
            draw.rectangle((20, 22, 40, 40), outline=255, fill=0)  # center
        if (button.bID == "A"):
            draw.ellipse((70, 40, 90, 60), outline=255, fill=0)  # A button
        if (button.bID == "B"):
            draw.ellipse((100, 20, 120, 40), outline=255, fill=0)  # B button
        client.draw()
    def start( loop : AbstractEventLoop, image):
        super().start()