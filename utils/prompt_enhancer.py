def enhance_prompt(prompt, style):

    style_prompts = {
        "Realistic": "ultra realistic, highly detailed, cinematic lighting, 8K",
        "Anime": "anime style, vibrant colors, masterpiece, highly detailed",
        "Cartoon": "cartoon style, colorful, cute, high quality",
        "Oil Painting": "oil painting, artistic, detailed brush strokes",
        "Sketch": "pencil sketch, black and white, detailed drawing",
        "Fantasy": "fantasy art, magical, epic lighting",
        "3D Render": "3D render, octane render, ultra detailed"
    }

    return f"{prompt}, {style_prompts.get(style, '')}"