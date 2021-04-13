from PIL.Image import Image
from basemodel import Machine

def execute (machine: Machine):
    global pistuff
    pistuff = machine
    draw = pistuff.draw

    if pistuff.button_U.value:  # button is released
        draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=0)  # Up
    else:  # button is pressed:
        draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=1)  # Up filled
 
    if pistuff.button_L.value:  # button is released
        draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=0)  # left
    else:  # button is pressed:
        draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=1)  # left filled
 
    if pistuff.button_R.value:  # button is released
        draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=0)  # right
    else:  # button is pressed:
        draw.polygon(
            [(60, 30), (42, 21), (42, 41)], outline=255, fill=1
        )  # right filled
 
    if pistuff.button_D.value:  # button is released
        draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=0)  # down
    else:  # button is pressed:
        draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=1)  # down filled
 
    if pistuff.button_C.value:  # button is released
        draw.rectangle((20, 22, 40, 40), outline=255, fill=0)  # center
    else:  # button is pressed:
        draw.rectangle((20, 22, 40, 40), outline=255, fill=1)  # center filled
 
    if pistuff.button_A.value:  # button is released
        draw.ellipse((70, 40, 90, 60), outline=255, fill=0)  # A button
    else:  # button is pressed:
        draw.ellipse((70, 40, 90, 60), outline=255, fill=1)  # A button filled
 
    if pistuff.button_B.value:  # button is released
        draw.ellipse((100, 20, 120, 40), outline=255, fill=0)  # B button
    else:  # button is pressed:
        draw.ellipse((100, 20, 120, 40), outline=255, fill=1)  # B button filled
 
    if not pistuff.button_A.value and not pistuff.button_B.value and not pistuff.button_C.value:
        catImage = Image.open("happycat_oled_64.ppm").convert("1")
        pistuff.disp.image(catImage)
    else:
        # Display image.
        pistuff.disp.image(pistuff.image)
 
    pistuff.disp.show()