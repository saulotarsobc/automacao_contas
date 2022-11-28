from flask import Flask, request, render_template
from pyautogui import typewrite
from time import sleep
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

@app.route("/")
def home():
    return render_template('index.html')
    # return """"""

@app.route("/typewrite")
def hello_world():
    word = request.args.get('word')
    typewrite(word)
    return {
        "word": word
    }

app.run(host="0.0.0.0", port=3000, debug=True)
