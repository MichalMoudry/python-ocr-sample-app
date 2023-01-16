"""
Python OCR app sample.
"""

import easyocr

if __name__ == "__main__":
    reader = easyocr.Reader(["en"])
    result = reader.readtext("./test_images/img01.png")
    print("Result:", result)
