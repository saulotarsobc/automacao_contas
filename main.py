from flask import Flask, request
from pyautogui import write, typewrite
from time import sleep
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/typewrite")
def hello_world():
    word = request.args.get('word')
    typewrite(word)
    return {
        "word": word
    }


app.run(host="192.168.3.21", port=3000, debug=True,)
