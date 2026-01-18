import streamlit as st
import os

from gemini_engine import generate_slide_data
from image_fetcher import fetch_image
from ppt_engine import create_ppt
from docx_reader import read_docx

# =====================
# CONFIG
# =====================
st.set_page_config(page_title="AI PPT Generator", layout="centered")
st.title("🎯 AI Tạo Slide Tự Động (Text + Word)")

# =====================
# SESSION STATE
# =====================
if "ppt_ready" not in st.session_state:
    st.session_state.ppt_ready = False

# =====================
# INPUT UI
# =====================
topic = st.text_area(
    "Nhập nội dung (có thể bỏ trống nếu upload Word)",
    height=150
)

uploaded_file = st.file_uploader(
    "Hoặc upload file Word (.docx)",
    type=["docx"]
)

style = st.selectbox(
    "Mục đích",
    ["Ôn thi", "Thuyết trình", "Báo cáo"]
)

color = st.text_input(
    "Màu chủ đạo (hex, optional)",
    placeholder="#0B3C5D"
)

# =====================
# MAIN ACTION
# =====================
if st.button("🚀 Tạo PowerPoint"):
    with st.spinner("Đang xử lý bằng AI..."):
        # 1. Xác định nguồn nội dung
        if uploaded_file is not None:
            content_source = read_docx(uploaded_file)
        elif topic.strip():
            content_source = topic
        else:
            st.warning("⚠️ Hãy nhập nội dung hoặc upload file Word")
            st.stop()

        # 2. Gọi Gemini
        data = generate_slide_data(
            topic=content_source,
            style=style,
            color_override=color if color else None
        )

        # 3. Lấy ảnh
        image_paths = []
        for idx, slide in enumerate(data["slides"]):
            path = fetch_image(slide["image_query"], idx)
            image_paths.append(path)

        # 4. Tạo PPT
        create_ppt(data, image_paths)

        st.session_state.ppt_ready = True

# =====================
# DOWNLOAD SECTION
# =====================
if st.session_state.ppt_ready and os.path.exists("generated_slides.pptx"):
    st.success("✅ Tạo slide thành công!")
    with open("generated_slides.pptx", "rb") as f:
        st.download_button(
            label="⬇️ Tải PowerPoint",
            data=f,
            file_name="AI_Slides.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )
