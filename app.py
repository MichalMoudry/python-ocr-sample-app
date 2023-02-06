"""
Python OCR app sample.
"""

from datetime import datetime
from flask import Flask, request
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    #return f"Index page | Current date: {datetime.now()}"
    return render_template("index.html")

@app.route("/processing", methods = ["POST"])
def file_upload():
    if request.method == "POST":
        files = request.files["file"]
        return ("Files were added to processing queue.", 200)
    return ("Wrong request.", 400)

if __name__ == "__main__":
    app.run()
