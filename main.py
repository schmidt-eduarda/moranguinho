from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<cor>')
def personagem(cor):
    cores = ['azul', 'vermelho', 'laranja', 'amarelo', 'roxo', 'preto', 'rosa', 'verde', 'branco', 'marrom']

    personagens = ['Amorinha', 'Moranguinho', 'Laranjinha', 'Gotinha de Limão',
                  'Ameixinha', 'Cerejinha', 'Cachinho de framboesa',
                  'Rocambole', 'Pudim', 'Torta de Mirtilo']
    for i in cores:
        if i == cor:
            opcao = personagens[cores.index(i)]

    return jsonify({'personagem': opcao})


app.run(host='0.0.0.0')