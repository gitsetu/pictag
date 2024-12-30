import time
import os
from pathlib import Path


IMAGE_DIR="images/"
IMAGE_PATH="images/sensehat_image.jpg"
TAGGED_IMAGE_DIR="images_tagged/"



def move_tagged_image(tag):
    PREFIX="picam_"
    TIMESTAMP = int(time.time())
    SEPARATOR="_"
    EXT=".jpg"

    TAGGED_IMAGE_FILENAME=f"{PREFIX}{TIMESTAMP}{SEPARATOR}{tag}{EXT}"
    TAGGED_IMAGE_COMPLETE_PATH=f"{TAGGED_IMAGE_DIR}{TAGGED_IMAGE_FILENAME}"

    # Rename / move current file to destination
    print("Moving and renaming image")
    Path(IMAGE_PATH).rename(TAGGED_IMAGE_COMPLETE_PATH)


def delete_image(IMAGE_PATH):
    if os.path.isfile(IMAGE_PATH):
        os.remove(IMAGE_PATH)
