from flask import Flask, render_template

alunos = [
    {'nome':'Ana Beatriz Magalhães Bicudo',
     'cards':'https://anabeatriz-mb.github.io/automatic-adventure/'}
]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', alunos=alunos)


if __name__ == '__main__':
    app.run(debug=True)