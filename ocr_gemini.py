# ocr_gemini.py
from google import genai
from google.genai import types
from PIL import Image
import json

def ocr_with_gemini(image_path, api_key):
    image = Image.open(image_path)
    client = genai.Client(api_key=api_key)
    prompt = (
        "Detect all text segments in the image and output their text, "
        "along with a bounding box for each segment. "
        "Bounding boxes should use [ymin, xmin, ymax, xmax], normalized to 0–1000. "
        "Output a JSON array. Each item should have keys: 'text' and 'box_2d'."
    )
    config = types.GenerateContentConfig(response_mime_type="application/json")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[image, prompt],
        config=config
    )
    segments = json.loads(response.text)
    width, height = image.size
    results = []
    for seg in segments:
        ymin, xmin, ymax, xmax = seg["box_2d"]
        abs_ymin = int(ymin / 1000 * height)
        abs_xmin = int(xmin / 1000 * width)
        abs_ymax = int(ymax / 1000 * height)
        abs_xmax = int(xmax / 1000 * width)
        results.append({
            "text": seg["text"],
            "bounding_box": {
                "left": abs_xmin,
                "top": abs_ymin,
                "width": abs_xmax - abs_xmin,
                "height": abs_ymax - abs_ymin
            }
        })
    return results, width, height
