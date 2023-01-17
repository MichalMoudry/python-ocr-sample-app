"""
Python OCR app sample.
"""

from datetime import datetime
#import easyocr
from flask import Flask
from flask import render_template
app = Flask(__name__)
#reader = easyocr.Reader(["en", "cs"])

@app.route("/")
def index():
    return f"Index page | Current date: {datetime.now()}"

@app.route("/ocr/<enable_dowload>")
def easyocr_sample(enable_dowload: bool):
    """
    result = (
        reader.readtext("./test_images/img01.png"),
        reader.readtext("./test_images/img02.png")
    )
    """
    return f"Enabled download: {enable_dowload}"

if __name__ == "__main__":
    app.run()
