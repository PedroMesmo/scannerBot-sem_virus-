import sqlite3, random
from flask import Flask, request, render_template

scanner = Flask(__name__)

def criarbanco():
    conexao = sqlite3.connect("scanner.db")

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS scanner (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tamanho TEXT NOT NULL
        )
    """)

    conexao.close()


@scanner.route("/")
def inicio():

    conexao = sqlite3.connect("scanner.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT nome, tamanho FROM scanner")
    dados = cursor.fetchall()

    conexao.close()
    i=0
    while i < len(dados) - 1:
        if dados[i][1] < dados[i+1][1]:
            dados[i], dados[i+1] = dados[i+1], dados[i]
            i = 0
        else:
            i = i+1

    return render_template("scanner.html", dados=dados)
    


@scanner.route("/scannear", methods=["POST"])
def scannear():
    nome = request.form["nome"].strip()


    frase=""
    d20 = random.randint(1, 20)
    if d20 == 1:
        tamanho = float(random.randint(-200, -1))/10
        frase = random.choice(["Meu deus do céu,\nisso é uma anomalia espacial?",
                               "O que você comeu na infância?\nMenos uma maças?",
                               "Uma boceta?"])
    elif d20 == 2:
        tamanho = float(0)
        frase = random.choice(["Nada?",
                               "Não tem nada!"
                               "O vazio dentro da sua cueca"])
    elif 2 < d20 <= 10:
        tamanho = float(random.randint(1, 149))/10
        frase = random.choice(["Um grãozinho",
                               "Raspa que cresce",
                               "Tão pequenino",
                               "Fofo",
                               "É nos menores frascos\nque estão os melhores perfumes"])

    elif 10 < d20 <= 15:
        tamanho = float(random.randint(150, 189))/10
        frase = random.choice(["Normie", 
                               "Nada mal,\nmas também nada demais",
                               "Meh",
                               "Medíocre"])

    elif 15 < d20 <= 19:
        tamanho = float(random.randint(190, 249))/10
        frase = random.choice(["Nossa,\nque grandinho",
                               "O que é isso?\nUma vara de catar manga?",
                               "Com mais uma perna\nvocê vira uma cadeira",
                               "Talvez eu devesse analizar\nmais de perto",
                               "Nossa, posso é..\nanalizar melhor? Digo...\ncom a boca"])

    elif d20 == 20:
        tamanho = float(random.randint(250, 600))/10
        frase = random.choice(["WOW",
                               "Mais um pouco de massa\ne isso colapsaria em uma singularidade",
                               "Nem preciso me aproximar para dizer,\no campo gravitacional já basta",
                               "A curvatura do espaço tempo está muito acentuada!"])

    if not nome or not tamanho:
        return "Preencha todos os campos", 400

    conexao = sqlite3.connect("scanner.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO scanner (nome, tamanho) VALUES (?, ?)",
        (nome, tamanho)
    )

    conexao.commit()

    cursor.execute("SELECT nome, tamanho FROM scanner")
    dados = cursor.fetchall()

    conexao.close()

    i=0
    while i < len(dados) - 1:
        if dados[i][1] < dados[i+1][1]:
            dados[i], dados[i+1] = dados[i+1], dados[i]
            i = 0
        else:
            i = i+1

    return render_template("scanner.html", dados=dados, frase=frase)


if __name__ == "__main__":
    criarbanco()
    scanner.run(debug=True)