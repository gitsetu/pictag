from capture_image import capture_image
from sense_hat import SenseHat
from upload_image import upload_image
from time import sleep

sense = SenseHat()
sense.low_light = True
# Define colours
LEVEL = 10
GREEN = (0, LEVEL, 0)  # RGB for green
RED = (LEVEL, 0, 0)    # RGB for red
WHITE = (LEVEL, LEVEL, LEVEL)    # RGB for white

IMAGE_PATH="../images/sensehat_image.jpg"
def button_presssed(event):
    if event.action == "pressed":
        sense.clear(WHITE)
        sleep(1)
        sense.clear(RED)
        capture_image(IMAGE_PATH)
        upload_image(IMAGE_PATH)

sense.stick.direction_middle = button_presssed
print("Press the middle button on the SenseHAT to capture an image.")
while True:
    pass  # Keep the script running to detect button presses