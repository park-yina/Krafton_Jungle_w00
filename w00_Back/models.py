# models.py
import PIL.Image
import base64
from io import BytesIO
import google.generativeai as genai

imgModel = genai.GenerativeModel("gemini-pro-vision")


def imgToStoryData(path):
    img = PIL.Image.open(path)
    response = imgModel.generate_content(
        [
            "해당 그림을 바탕으로 한국어로 된 한 문장의 짧고 재미있는 스토리 만들어줘.",
            img,
        ]
    )
    response.resolve()
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return {"img_src": img_str, "text": response.text}
