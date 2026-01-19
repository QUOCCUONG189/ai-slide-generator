import streamlit as st
from gemini_engine import generate_slide_data
from ppt_engine import create_ppt
from docx_reader import read_docx

st.set_page_config("AI Slide Generator PRO", layout="centered")

st.title("🚀 AI Slide Generator PRO")

style = st.selectbox(
    "Phong cách",
    ["Học thuật", "Startup Pitch", "Marketing", "Minimal"]
)

color = st.text_input("Màu chủ đạo", "xanh dương gradient")
slide_count = st.slider("Số slide", 5, 15, 8)

text = st.text_area("Nhập nội dung")

file = st.file_uploader("Hoặc upload Word", type=["docx"])

content = read_docx(file) if file else text

if st.button("✨ Tạo PowerPoint"):
    if not content.strip():
        st.warning("Chưa có nội dung")
    else:
        with st.spinner("Gemini đang làm việc..."):
            data = generate_slide_data(
                content, style, slide_count, color
            )
            ppt = create_ppt(data)

        with open(ppt, "rb") as f:
            st.success("Hoàn tất!")
            st.download_button(
                "⬇️ Tải PPT",
                f,
                file_name="AI_Slides_PRO.pptx"
            )
