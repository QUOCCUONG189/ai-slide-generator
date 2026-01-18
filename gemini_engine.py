import google-generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are a presentation architect.

Rules:
- Write ALL content in VIETNAMESE
- Output STRICT JSON ONLY
- No explanations

JSON format:
{
  "theme": {
    "primary": "#0B3C5D",
    "secondary": "#FFFFFF",
    "accent": "#F4B41A"
  },
  "slides": [
    {
      "title": "",
      "key_message": "",
      "bullets": [],
      "image_query": ""
    }
  ]
}
"""

def generate_slide_data(topic, style, color_override=None):
    prompt = f"""
Chủ đề: {topic}
Mục đích: {style}

Nếu có màu chủ đạo người dùng yêu cầu thì ưu tiên.
Tạo 8–10 slide.
"""

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        system_instruction=SYSTEM_PROMPT
    )

    response = model.generate_content(prompt)
    text = response.text.strip()

    return json.loads(text)
