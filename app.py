"""
Python OCR app sample.
"""

from datetime import datetime
from flask import Flask, request
from flask import render_template
app = Flask(__name__)

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

@app.route("/processing", methods = ["POST"])
def file_upload():
    if request.method == "POST":
        files = request.files["file"]
        return ("Files were added to processing queue.", 200)
    return ("Wrong request.", 400)

if __name__ == "__main__":
    app.run()
