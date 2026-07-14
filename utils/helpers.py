import random
import json
import os
from datetime import datetime

# Random prompts
prompts = [
    "A futuristic cyberpunk city at sunset",
    "A magical forest with glowing mushrooms",
    "A cute baby panda eating bamboo",
    "A luxury modern bedroom interior",
    "A flying castle above the clouds",
    "A realistic lion wearing royal armor",
    "A beautiful Islamic mosque at sunrise",
    "A fantasy dragon flying over mountains"
]


def random_prompt():
    return random.choice(prompts)


# History file
HISTORY_FILE = "history/history.json"


def save_history(prompt, style, aspect_ratio, image_path):

    history = []

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)

    history.append({
        "prompt": prompt,
        "style": style,
        "aspect_ratio": aspect_ratio,
        "image_path": image_path,
        "date": datetime.now().strftime("%d-%m-%Y %H:%M")
    })

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def load_history():

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)

    return []