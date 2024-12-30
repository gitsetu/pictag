import time
from pathlib import Path


PREFIX="picam_"
TIMESTAMP = int(time.time())
SEPARATOR="_"
JPG_EXT=".jpg"

def move_tagged_image(tag):
    IMAGE_DIR="images/"
    IMAGE_PATH="images/sensehat_image.jpg"
    TAGGED_IMAGE_DIR="tagged_images/"
    TAGGED_IMAGE_FILENAME=f"{PREFIX}{TIMESTAMP}{SEPARATOR}{tag}{JPG_EXT}"
    TAGGED_IMAGE_COMPLETE_PATH=f"{TAGGED_IMAGE_DIR}{TAGGED_IMAGE_FILENAME}"

    # Rename / move current file to destination
    print("Moving and renaming image")
    Path(IMAGE_PATH).rename(TAGGED_IMAGE_COMPLETE_PATH)