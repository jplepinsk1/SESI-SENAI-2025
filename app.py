from flask import Flask, render_template

alunos = [
    {'nome':'Ana Beatriz Magalhães Bicudo',
     'cards':'https://anabeatriz-mb.github.io/automatic-adventure/'},
    {'nome':'Ana Clara Mendes Proença',
      'cards':'https://anaclaramendes399.github.io/Projeto-Certo'},
    {'nome':'Beatriz Sousa de Andrade',
      'cards':'https://beatriz-sousa-andrade.github.io/filmes-de-terror-classicos'},
    {'nome':'Daniel Pupo de Morais Santos',
     'cards':''},
    {'nome':'Emannoel Henrique Soares de Oliveira',
     'cards':''},
    {'nome':'Felipe Barros Souza',
     'cards':''},
    {'nome':'Felix Fonseca Nogueira',
     'cards':''},
    {'nome':'Guilherme da Costa Silva',
     'cards':''},
    {'nome':'Isabelly Ferreira de Lima',
     'cards':'https://isabelly-ferreira.github.io/Projeto-Cards/'},
    {'nome':'Isadora Jucá de Lima',
     'cards':''},
    {'nome':'João Guilherme Barros Arruda',
     'cards':'https://jgarrudaa.github.io/Card-de-Filmes/'},
    {'nome':'João Pedro Stadler Roza Santos',
     'cards':''},
    {'nome':'João Victor Marcondes M. Barbosa de Queiroz',
     'cards':'https://jvictormarcon.github.io/Cards/'},
    {'nome':'Joaquim Antonio dos Santos Neto',
     'cards':'https://joaquimneto17.github.io/Elenco-Santos'},
    {'nome':'John Cristopher de Sousa',
     'cards':'https://john-cristopher.github.io/card_carros'},
    {'nome':'Julio Aurélio Souza',
     'cards':'https://julio-aurelio.github.io/SENAI'},
    {'nome':'Livia Domingues Matos',
     'cards':'https://liviadmatos.github.io/upgraded-telegram'},
    {'nome':'Lorena Rinaldo Moreira',
     'cards':''},
    {'nome':'Lucas Assis Andrela',
     'cards':''},
    {'nome':'Luiz Felipe de Lima Barros',
     'cards':''},
    {'nome':'Maria Júllia Schimidt Ott Prestes',
     'cards':''},
    {'nome':'Mauro José da Silva Junior',
     'cards':''},
    {'nome':'Mayara Alves de Oliveira',
     'cards':'https://mayaa-lves.github.io/books.cards2'},
    {'nome':'Nicolly Oliveira dos Santos',
     'cards':'https://nicollyoliveiras.github.io/Cards.oth'},
    {'nome':'Pablo Gomes da Silva',
     'cards':''},
    {'nome':'Pedro Henrique Francisconi Ferreira',
     'cards':''},
    {'nome':'Pedro Henrique Vasconcelos Matilde',
     'cards':'https://pedrohenriquevm.github.io/Projetos'},
    {'nome':'Pedro Vitor Barros de Morais',
     'cards':''},
    {'nome':'Pietro Rodrigues Torresani Mantuan',
     'cards':''},
    {'nome':'Rebeca Diniz Gonçalves',
     'cards':''},
    {'nome':'Vinicius Mariozi Oliveira',
     'cards':'https://viniciusmariozioliveira.github.io/cards'},
    {'nome':'Yan Matheus Proença Camargo',
     'cards':'https://yan-proenca.github.io/card-sombras-cicatrizes'}
    
]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', alunos=alunos)


if __name__ == '__main__':
    app.run(debug=True)