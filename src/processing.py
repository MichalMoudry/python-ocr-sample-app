"""
Module for file processing.
"""

import easyocr
reader = easyocr.Reader(["en", "cs"], gpu=False)

"""
result = (
    reader.readtext("./test_images/img01.png"),
    reader.readtext("./test_images/img02.png")
)
"""
