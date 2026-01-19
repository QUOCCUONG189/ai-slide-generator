from pptx import Presentation
from pptx.util import Inches

def create_ppt(slide_data, output_path="slides.pptx"):
    prs = Presentation()

    # Slide tiêu đề
    title_slide = prs.slides.add_slide(prs.slide_layouts[0])
    title_slide.shapes.title.text = slide_data["title"]

    for slide in slide_data["slides"]:
        s = prs.slides.add_slide(prs.slide_layouts[1])
        s.shapes.title.text = slide["title"]

        body = s.shapes.placeholders[1]
        tf = body.text_frame
        tf.clear()

        for bullet in slide["bullets"]:
            p = tf.add_paragraph()
            p.text = bullet
            p.level = 1

    prs.save(output_path)
    return output_path
