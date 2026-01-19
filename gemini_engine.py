import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
Bạn là chuyên gia thiết kế slide PowerPoint.

YÊU CẦU BẮT BUỘC:
- Viết TOÀN BỘ bằng tiếng Việt
- Nội dung ngắn gọn, dễ thuyết trình
- Chia 8–10 slide
- Trả về JSON THUẦN, KHÔNG giải thích

ĐỊNH DẠNG JSON:
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
    # Giới hạn độ dài để tránh InvalidArgument
    topic = topic[:8000]

    prompt = f"""
{SYSTEM_PROMPT}

MỤC ĐÍCH: {style}

NỘI DUNG ĐẦU VÀO:
{topic}

Nếu người dùng cung cấp màu chủ đạo thì ưu tiên.
"""

    model = genai.GenerativeModel("models/gemini-1.5-flash")

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.6,
            "max_output_tokens": 2048
        }
    )

    text = response.text.strip()

    # Phòng Gemini trả thêm ```json
    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)
