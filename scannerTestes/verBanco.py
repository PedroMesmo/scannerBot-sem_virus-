import sqlite3

conexao = sqlite3.connect("scanner.db")
cursor = conexao.cursor()

cursor.execute(
    "SELECT * FROM scanner"
)
dados = cursor.fetchall()

for dado in dados:
    print(dado)

conexao.close()