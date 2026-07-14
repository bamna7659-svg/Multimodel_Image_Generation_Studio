import requests
from PIL import Image
from io import BytesIO
from urllib.parse import quote


def generate_image(prompt):

    prompt = quote(prompt)

    url = f"https://image.pollinations.ai/prompt/{prompt}"

    response = requests.get(url)

    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        raise Exception("Image generation failed.")