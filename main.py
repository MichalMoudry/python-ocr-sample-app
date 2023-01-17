"""
Python OCR app sample.
"""

import easyocr

if __name__ == "__main__":
    reader = easyocr.Reader(["en", "cs"])
    result = (
        reader.readtext("./test_images/img01.png"),
        reader.readtext("./test_images/img02.png")
    )
    print("Result:", result)
