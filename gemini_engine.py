import os
import google.generativeai as genai
import json

def generate_slide_data(topic, style, color_override=None):
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-1.0-pro")

    prompt = f"""
Bạn là AI chuyên tạo slide PowerPoint CHUYÊN NGHIỆP.

YÊU CẦU:
- Ngôn ngữ: TIẾNG VIỆT
- Phong cách: {style}
- Màu chủ đạo: {color_override if color_override else "tự chọn theo xu hướng mới"}
- Trả về JSON hợp lệ, KHÔNG markdown, KHÔNG giải thích.

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

    response = model.generate_content(prompt)

    text = response.text.strip()

    # Cắt JSON an toàn
    start = text.find("{")
    end = text.rfind("}") + 1
    json_text = text[start:end]

    return json.loads(json_text)
