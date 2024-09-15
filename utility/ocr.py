import easyocr

def ocr(image_path: str):
    reader = easyocr.Reader(['ch_sim','en','hi'])
    result = reader.readtext(image_path,detail=0)

    return result