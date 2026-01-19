import streamlit as st
from gemini_engine import generate_slide_data
from ppt_engine import create_ppt
from docx_reader import read_docx

st.set_page_config(
    page_title="AI Slide Generator",
    layout="centered"
)

st.title("🎨 AI Slide Generator (Gemini)")

# ====== TÙY CHỌN STYLE ======
style = st.selectbox(
    "Phong cách slide",
    [
        "Thuyết trình học thuật",
        "Startup Pitch Deck",
        "Marketing",
        "Minimal hiện đại"
    ]
)

color = st.text_input(
    "Màu chủ đạo (không bắt buộc)",
    placeholder="Ví dụ: xanh dương, tím gradient"
)

# ====== NHẬP NỘI DUNG ======
st.subheader("📥 Nhập nội dung")

text_input = st.text_area(
    "Nhập nội dung / ý tưởng",
    height=200
)

uploaded_file = st.file_uploader(
    "Hoặc upload file Word (.docx)",
    type=["docx"]
)

# ====== XÁC ĐỊNH NGUỒN NỘI DUNG ======
if uploaded_file is not None:
    content_source = read_docx(uploaded_file)
else:
    content_source = text_input

# ====== BUTTON TẠO SLIDE ======
if st.button("🚀 Tạo PowerPoint"):
    if not content_source.strip():
        st.warning("❗ Vui lòng nhập nội dung hoặc upload file Word")
    else:
        with st.spinner("🤖 Gemini đang tạo nội dung..."):
            slide_data = generate_slide_data(
                topic=content_source,
                style=style,
                color_override=color if color else None
            )

            ppt_path = create_ppt(slide_data)

        st.success("✅ Tạo slide thành công!")

        with open(ppt_path, "rb") as f:
            st.download_button(
                label="⬇️ Tải PowerPoint",
                data=f,
                file_name="ai_slides.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )
