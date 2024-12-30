from capture_image import capture_image
from sense_hat import SenseHat
from upload_image import upload_image
from time import sleep
from led import *

sense = SenseHat()
sense.low_light = True

IMAGE_PATH="../images/sensehat_image.jpg"

def button_presssed(event):
    if event.action == "pressed":
        sense.clear(red)
        sleep(1)
        sense.clear(white)
        capture_image(IMAGE_PATH)
        upload_image(IMAGE_PATH)
        sense.clear()
        sense.clear(blue)

sense.stick.direction_middle = button_presssed
print("Press the middle button on the SenseHAT to capture an image.")
while True:
    pass  # Keep the script running to detect button presses