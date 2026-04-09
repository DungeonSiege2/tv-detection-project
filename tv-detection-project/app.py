from flask import Flask, render_template, request, send_file
import os
from model import detect_tv
from utils.save_stats import save_result
from utils.export_excel import generate_excel

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            count, result_path = detect_tv(filepath)

            save_result(file.filename, count)

            return render_template(
    "index.html",
    count=count,
    image="static/uploads/" + os.path.basename(result_path)
)

    return render_template("index.html", count=None)

@app.route("/download_excel")
def download_excel():
    generate_excel()
    return send_file("report.xlsx", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
