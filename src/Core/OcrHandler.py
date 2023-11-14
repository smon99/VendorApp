import pytesseract


class OcrHandler:

    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    @staticmethod
    def perform_ocr(cap):
        text = pytesseract.image_to_string(cap)
        remove_spaces = ''.join(text.split())  # remove spaces
        return remove_spaces
