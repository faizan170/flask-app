from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 21 * 1024 * 1024
@app.route("/")
def home():
    return render_template("index.html")



@app.route("/upload", methods=["POST"])
def upload_request():
    try:
        fileData = request.files["file"]
        filename = secure_filename(fileData.filename)
        fileData.save("static/images/" + filename)
        return "File Upload Successfully"
    except Exception as ex:
        return str(ex)


@app.route("/images")
def images():
    return render_template("images.html", images = os.listdir("./static/images"), url = request.url_root)


if __name__ == "__main__":
    app.run(debug=True)