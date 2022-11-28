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
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Atalhos Para as Contas</title>
    <!-- <link rel="stylesheet" href="./css/main.css"> -->
    <style>*{margin:0;padding:0;box-sizing:border-box}#wrap{width:100vw;display:flex;flex-direction:column}#wrap .btn{background-color:#5f9ea0;color:#fff;border-radius:5px;font-size:20px;margin:5px;padding:5px}#wrap label{margin-left:10px;font-size:20px}#wrap .wrap_input{width:100vw;position:relative;align-items:center;justify-content:center;padding:10px}#wrap .wrap_input input{width:calc(100% - 10px);font-size:20px;border-radius:5px;padding:10px}#wrap .wrap_input textarea{width:calc(100% - 10px);border-radius:5px;padding:5px}</style>
</head>

<body>
    <div id="wrap">
        <div class="wrap_input">
            <label for="wordInput">Retorno:</label>
            <input disabled type="text" id="wordInput" name="wordInput">
        </div>
        <hr>
        <div class="btn" onclick="sendWord('Donativos - Obra Mundial')">Donativos - Obra Mundial</div>
        <div class="btn" onclick="sendWord('Donativos - Despesas da Congregacao')">Donativos - Despesas da Congregacao
        </div>
        <div class="btn" onclick="sendWord('Donativos - Construcao da Filial')">Donativos - Construcao da Filial</div>
        <div class="btn" onclick="sendWord('Reajuste Monetario - BACEN')">Reajuste Monetario - BACEN</div>
        <div class="btn" onclick="sendWord('Juros')">Juros</div>
        <hr>
        <div class="wrap_input">
            <label for="custon_text">Texto Customizado:</label>
            <textarea name="custon_text" id="custon_text" rows="10">Texto customizado</textarea>
        </div>
        <button onclick="sendCustonText()" class="btn">ENVIAR</button>
    </div>

    <script>
        const wordInput = document.getElementById('wordInput');
        const custon_text = document.getElementById('custon_text');
        function sendWord(word) {
            console.log(window.location)
            let url = `${window.location}typewrite?word=${word}`;
            console.log(url);
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
        function sendCustonText() {
            sendWord(custon_text.innerHTML);
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

app.run(host="0.0.0.0", port=3000, debug=False)
