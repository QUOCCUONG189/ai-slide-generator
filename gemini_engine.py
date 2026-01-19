import os, json
from google import genai

def generate_slide_data(topic, style, slide_count, color):
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    prompt = f"""
Bạn là AI chuyên tạo slide PowerPoint CHUYÊN NGHIỆP.

YÊU CẦU:
- Ngôn ngữ: TIẾNG VIỆT
- Phong cách: {style}
- Màu chủ đạo: {color}
- Số slide: {slide_count}
- Mỗi slide có 3–5 bullet
- Trả về JSON hợp lệ
- Không markdown, không giải thích

FORMAT:
{{
  "title": "...",
  "slides": [
    {{
      "title": "...",
      "bullets": ["...", "..."],
      "image_query": "từ khóa ảnh"
    }}
  ]
}}

CHỦ ĐỀ:
{topic}
"""

    res = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    text = res.text
    return json.loads(text[text.find("{"):])
