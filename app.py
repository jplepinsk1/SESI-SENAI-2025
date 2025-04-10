from flask import Flask, render_template

alunos = [
    {'nome':'Ana Beatriz Magalhães Bicudo',
     'cards':'https://anabeatriz-mb.github.io/automatic-adventure/'},
    {'nome':'Ana Clara Mendes Proença',
      'cards':'https://anaclaramendes399.github.io/Projeto-Certo'},
    {'nome':'Beatriz Sousa de Andrade',
      'cards':'https://beatriz-sousa-andrade.github.io/filmes-de-terror-classicos'},
    {'nome':'Daniel Pupo de Morais Santos',
     'cards':'https://danielpupo.github.io/Cards-Futsal'},
    {'nome':'Emannoel Henrique Soares de Oliveira',
     'cards':'https://emannoel-henrique.github.io/Projetos-DS'},
    {'nome':'Felipe Barros Souza',
     'cards':'https://barros-sz.github.io/Cards-Sobre-V-F'},
    {'nome':'Felix Fonseca Nogueira',
     'cards':'https://fonseca-felix.github.io/felix.card'},
    {'nome':'Guilherme da Costa Silva',
     'cards':'https://glcost.github.io/Trabalho-de-Cards'},
    {'nome':'Isabelly Ferreira de Lima',
     'cards':'https://isabelly-ferreira.github.io/Projeto-Cards/'},
    {'nome':'Isadora Jucá de Lima',
     'cards':'https://isajuca.github.io/card-dogs'},
    {'nome':'João Guilherme Barros Arruda',
     'cards':'https://jgarrudaa.github.io/Card-de-Filmes/'},
    {'nome':'João Pedro Stadler Roza Santos',
     'cards':'https://jpsantosx.github.io/card-de-jogos'},
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
     'cards':'https://lorena-rinaldo.github.io/cards-pokemon/'},
    {'nome':'Lucas Assis Andrela',
     'cards':'https://lucasandrela.github.io/Cards'},
    {'nome':'Luiz Felipe de Lima Barros',
     'cards':'https://luizfelipebarros.github.io/Project-cards'},
    {'nome':'Maria Júllia Schimidt Ott Prestes',
     'cards':'https://mariajschimidt.github.io/flores-tipos'},
    {'nome':'Mauro José da Silva Junior',
     'cards':'https://omaurojunior.github.io/Estruturando-site'},
    {'nome':'Mayara Alves de Oliveira',
     'cards':'https://mayaa-lves.github.io/books.cards.b'},
    {'nome':'Nicolly Oliveira dos Santos',
     'cards':'https://nicollyoliveiras.github.io/Cards.oth'},
    {'nome':'Pablo Gomes da Silva',
     'cards':'https://pablo-gomes.github.io/Cards-carros-de-luxo'},
    {'nome':'Pedro Henrique Francisconi Ferreira',
     'cards':'https://pedrofrancisconi.github.io/PokeNBa'},
    {'nome':'Pedro Henrique Vasconcelos Matilde',
     'cards':'https://pedrohenriquevm.github.io/Projetos'},
    {'nome':'Pedro Vitor Barros de Morais',
     'cards':'https://pedromorais15.github.io/pedro-page'},
    {'nome':'Pietro Rodrigues Torresani Mantuan',
     'cards':'https://mantuanpietro.github.io/CARDS'},
    {'nome':'Rebeca Diniz Gonçalves',
     'cards':'https://rebecadiniz.github.io/estudo-da-filosofia/'},
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