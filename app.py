from flask import Flask, render_template, request, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import os
from ocr_gemini import ocr_with_gemini

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.config["GEMINI_API_KEY"] = os.environ["GEMINI_API_KEY"]

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return "No file part", 400
        file = request.files["image"]
        if file.filename == "":
            return "No selected file", 400
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(image_path)
        results, width, height = ocr_with_gemini(image_path, app.config["GEMINI_API_KEY"])
        print("results", results)
        print("width", width)
        print("height", height)
        return render_template(
            "index.html",
            image_file=filename,
            results=results,
            image_width=width,
            image_height=height
        )
    return render_template("index.html")

@app.route("/static/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)
