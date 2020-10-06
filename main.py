from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/upload", methods=["POST"])
def upload_request():
    try:
        fileData = request.files["file"]
        filename = secure_filename(fileData.filename)
        fileData.save("images/" + filename)
        return "File Upload Successfully"
    except Exception as ex:
        return str(ex)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)