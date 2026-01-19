import streamlit as st
from gemini_engine import generate_slide_data
from ppt_engine import create_ppt
from docx import Document
import os

st.set_page_config(page_title="AI Slide Generator", layout="centered")

st.title("🎨 AI Slide Generator (Gemini)")

style = st.selectbox(
    "Phong cách slide",
    ["Thuyết trình học thuật", "Startup Pitch Deck", "Marketing", "Minimal hiện đại"]
)

color = st.text_input("Màu chủ đạo (tuỳ chọn)", placeholder="Ví dụ: xanh dương, tím gradient")

st.subheader("📥 Nhập nội dung")

content_source = ""

text_input = st.text_area("Nhập nội dung / ý tưởng", height=200)

uploaded_file = st.file_uploader("Hoặc upload file Word (.docx)", type=["docx"])

if uploaded_file:
    doc = Document(uploaded_file)
    content_source = "\n".join([p.text for p in doc.paragraphs])
else:
    content_source = text_input

if st.button("🚀 Tạo slide"):
    if not content_source.strip():
        st.warning("Chưa có nội dung!")
    else:
        with st.spinner("Gemini đang tạo nội dung..."):
            data = generate_slide_data(
                topic=content_source,
                style=style,
                color_override=color if color else None
            )

            ppt_path = create_ppt(data)

        with open(ppt_path, "rb") as f:
            st.success("Hoàn tất!")
            st.download_button(
                "⬇️ Tải PowerPoint",
                f,
                file_name="ai_slides.pptx"
            )
