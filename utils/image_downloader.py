import os
from datetime import datetime

SAVE_FOLDER = "generated_images"


def save_image(image):

    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)

    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"

    filepath = os.path.join(SAVE_FOLDER, filename)

    image.save(filepath)

    return filepath