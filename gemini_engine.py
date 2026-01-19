import os
import json
from google import genai

def generate_slide_data(topic, style, color_override=None):
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    prompt = f"""
Bạn là AI chuyên tạo nội dung PowerPoint CHUYÊN NGHIỆP.

YÊU CẦU:
- Ngôn ngữ: TIẾNG VIỆT
- Phong cách: {style}
- Màu chủ đạo: {color_override if color_override else "tự chọn theo xu hướng mới"}
- Chỉ trả về JSON hợp lệ
- Không markdown, không giải thích

FORMAT:
{{
  "title": "...",
  "slides": [
    {{
      "title": "...",
      "bullets": ["...", "...", "..."],
      "image_query": "từ khóa ảnh"
    }}
  ]
}}

CHỦ ĐỀ:
{topic}
"""

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    start = text.find("{")
    end = text.rfind("}") + 1
    json_text = text[start:end]

    return json.loads(json_text)
