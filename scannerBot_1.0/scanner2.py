import customtkinter as ctk
from PIL import Image
import csv
import random

scanner = ctk.CTk()
scanner.geometry('900x800')
scanner.title('Scanner')
scanner.configure(fg_color="#181825")


frame = ctk.CTkFrame(scanner, fg_color="#2F304A")
frame.grid(row=0, column=0, padx=(40, 0))
frame2 = ctk.CTkFrame(scanner)
frame2.grid(row=0, column=1)


scannerBoyt = ctk.CTkImage(
    dark_image = Image.open("scanner.png"),
    size=(600,800)
)
imagem = ctk.CTkLabel(
    frame2,
    image=scannerBoyt,
    text="",
    fg_color="#181825"
)
imagem.grid(row=0, column=2)

textoNomes = ctk.CTkLabel(
    frame,
    text="Seu nome",
    font=('Arial', 20),
    text_color='White'
)
textoNomes.grid(row=0, column=0, padx=5, pady=5)

entradaNomes = ctk.CTkEntry(frame)
entradaNomes.grid(row=0, column=1, padx=5, pady=5)



def scannear():
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

    def gravar():
        with open("dados.csv", "a", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([entradaNomes.get(), tamanho ])
    def ordenar():
        with open("dados.csv", "r", encoding = "utf-8") as arquivo:
            leitor = csv.reader(arquivo)

            dados = list(leitor)

            i = 0
            while i < len(dados) - 1:
                if float(dados[i][1]) < float(dados[i+1][1]):
                    dados[i], dados[i+1] = dados[i+1], dados[i]
                    i = 0
                else:
                    i = i+1

        with open("dados.csv", "w", newline="", encoding = "utf-8") as arquivo:
            leitor = csv.writer(arquivo)

            leitor.writerows(dados)

        print(dados)

    def atualizar_tabela():
        for widget in tabelaRank.winfo_children():
            widget.destroy()


        with open("dados.csv", "r", encoding="utf-8") as arquivo:
            dados = csv.reader(arquivo)

            for linha, dados_linha in enumerate(dados):
                ctk.CTkLabel(
                    tabelaRank,
                    text=dados_linha[0]
                ).grid(row=linha, column=0, padx=20, pady=5)

                ctk.CTkLabel(
                    tabelaRank,
                    text=dados_linha[1] + " cm"
                ).grid(row=linha, column=1, padx=20, pady=5)

    gravar()
    ordenar()
    atualizar_tabela()
    print(frase)
    textoFrase.configure(text=frase)
    entradaNomes.delete(0, "end")


botaoScannear = ctk.CTkButton(
    frame,
    text="Scannear",
    command=scannear,
    fg_color="#6C7086",
    hover_color="#C042AF"
)
botaoScannear.grid(row=2, column=0, columnspan=2)


textoFrase = ctk.CTkLabel(
    frame,
    text="",
    font=('Arial', 24),
    text_color="#E161B0"
) 
textoFrase.grid(row=3, column=0, columnspan=2, pady=10)

textoRank = ctk.CTkLabel(
    frame,
    text="Rank Global",
    font=('Arial', 15),
    text_color='White'
)
textoRank.grid(row=5, column=0, columnspan=2)

tabelaRank = ctk.CTkScrollableFrame(
    frame,
    width = 300,
    height = 400,
    fg_color="#45475A",
)
tabelaRank.grid(row=6, column=0, columnspan=2, padx=15)

with open("dados.csv", "r", encoding="utf-8") as arquivo:
    dados = csv.reader(arquivo)

    for linha, dados_linha in enumerate(dados):
        ctk.CTkLabel(
            tabelaRank,
            text=dados_linha[0]
        ).grid(row=linha, column=0, padx=20, pady=5)

        ctk.CTkLabel(
            tabelaRank,
            text=dados_linha[1] + " cm"
        ).grid(row=linha, column=1, padx=20, pady=5)

scanner.mainloop()