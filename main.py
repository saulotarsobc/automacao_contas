from flask import Flask, request, render_template
from pyautogui import typewrite
from time import sleep
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

@app.route("/")
def home():
    # return render_template('index.html')
    return """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>*{margin:0;padding:0;box-sizing:border-box}.btn{background-color:#5f9ea0;color:#fff;margin:10px;padding:10px;border-radius:5px;font-size:20px}label{margin-left:10px;font-size:20px}input{width:100%;margin:10px;padding:10px;font-size:20px;border-radius:5px;margin-bottom:30px}/*# sourceMappingURL=main.css.map */
    </style>
</head>

<body>

    <label for="wordInput">Host:</label>
    <input type="text" id="host" name="host" value="192.168.3.21">

    <label for="wordInput">Port:</label>
    <input type="number" id="port" name="port" value="3000">
    <hr>

    <label for="wordInput">O que foi escrito...</label>
    <input disabled type="text" id="wordInput" name="wordInput">

    <div class="btn" onclick="sendWord('Donativos - Obra Mundial')">Donativos - Obra Mundial</div>
    <div class="btn" onclick="sendWord('Donativos - Despesas da Congregacao')">Donativos - Despesas da Congregacao</div>
    <div class="btn" onclick="sendWord('Donativos - Construcao da Filial')">Donativos - Construcao da Filial</div>
    <div class="btn" onclick="sendWord('Reajuste Monetario - BACEN')">Reajuste Monetario - BACEN</div>
    <div class="btn" onclick="sendWord('Juros')">Juros</div>


    <script>

        const host = document.getElementById('host');
        const port = document.getElementById('port');
        const wordInput = document.getElementById('wordInput');

        function sendWord(word) {

            console.log(word)

            let url = `http://${host.value}:${port.value}/typewrite?word=${word}`;

            console.assert(url);

            fetch(url)
                .then((res) => {
                    return res.json();
                })
                .then((json) => {
                    wordInput.value = json.word;
                })
                .catch((e) => {
                    console.log('Deu ruin!')
                    console.error(e)
                });
        }

    </script>
</body>

</html>"""

@app.route("/typewrite")
def hello_world():
    word = request.args.get('word')
    typewrite(word)
    return {
        "word": word
    }

app.run(host="0.0.0.0", port=3000)
