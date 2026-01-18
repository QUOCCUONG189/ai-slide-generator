import streamlit as st
from gemini_engine import generate_slide_data
from image_fetcher import fetch_image
from ppt_engine import create_ppt

st.set_page_config(page_title="AI PPT Generator", layout="centered")
st.title("🎯 AI Tạo Slide Tự Động")

topic = st.text_input("Nhập chủ đề (tiếng Việt)")
style = st.selectbox("Mục đích", ["Ôn thi", "Thuyết trình", "Báo cáo"])
color = st.text_input("Màu chủ đạo (hex, optional)")

if st.button("🚀 Tạo PowerPoint"):
    with st.spinner("Đang dùng AI..."):
        data = generate_slide_data(topic, style, color)

        image_paths = []
        for idx, slide in enumerate(data["slides"]):
            path = fetch_image(slide["image_query"], idx)
            image_paths.append(path)

        create_ppt(data, image_paths)

    st.success("Xong rồi!")
    with open("generated_slides.pptx", "rb") as f:
        st.download_button("⬇️ Tải PowerPoint", f, file_name="AI_Slides.pptx")