import sqlite3

conexao = sqlite3.connect("scanner.db")
cursor = conexao.cursor()

cursor.execute(
        "SELECT nome, tamanho FROM scanner"
    )

dados = cursor.fetchall()

print(dados)