const entradaNome = document.getElementById("nome");
const botaoScannear = document.getElementById("botaoScannear");
const textoFrase = document.getElementById("frase");
const tabelaRank = document.getElementById("tabelaRank");


const frases = {

    anomalia: [
        "Meu deus do céu,\nisso é uma anomalia espacial?",
        "O que você comeu na infância?\nMenos uma maçãs?",
        "Uma boceta?"
    ],

    nada: [
        "Nada?",
        "Não tem nada!",
        "O vazio dentro da sua cueca"
    ],

    pequeno: [
        "Um grãozinho",
        "Raspa que cresce",
        "Tão pequenino",
        "Fofo",
        "É nos menores frascos\nque estão os melhores perfumes"
    ],

    medio: [
        "Normie",
        "Nada mal,\nmas também nada demais",
        "Meh",
        "Medíocre"
    ],

    grande: [
        "Nossa,\nque grandinho",
        "O que é isso?\nUma vara de catar manga?",
        "Com mais uma perna\nvocê vira uma cadeira",
        "Talvez eu devesse analizar\nmais de perto",
        "Nossa, posso é..\nanalizar melhor? Digo...\ncom a boca"
    ],

    enorme: [
        "WOW",
        "Mais um pouco de massa\ne isso colapsaria em uma singularidade",
        "Nem preciso me aproximar para dizer,\no campo gravitacional já basta",
        "A curvatura do espaço tempo está muito acentuada!"
    ]

};


function escolhaAleatoria(lista) {

    const indice = Math.floor(Math.random() * lista.length);

    return lista[indice];
}


function numeroAleatorio(min, max) {

    return Math.floor(
        Math.random() * (max - min + 1)
    ) + min;
}


function scannear() {

    const nome = entradaNome.value.trim();

    if (nome === "") {

        alert("Digite seu nome!");

        return;
    }


    const d20 = numeroAleatorio(1, 20);

    let tamanho;
    let frase;


    if (d20 === 1) {

        tamanho = numeroAleatorio(-200, -1) / 10;

        frase = escolhaAleatoria(
            frases.anomalia
        );
    }


    else if (d20 === 2) {

        tamanho = 0;

        frase = escolhaAleatoria(
            frases.nada
        );
    }


    else if (d20 > 2 && d20 <= 10) {

        tamanho = numeroAleatorio(1, 149) / 10;

        frase = escolhaAleatoria(
            frases.pequeno
        );
    }


    else if (d20 > 10 && d20 <= 15) {

        tamanho = numeroAleatorio(150, 189) / 10;

        frase = escolhaAleatoria(
            frases.medio
        );
    }


    else if (d20 > 15 && d20 <= 19) {

        tamanho = numeroAleatorio(190, 249) / 10;

        frase = escolhaAleatoria(
            frases.grande
        );
    }


    else {

        tamanho = numeroAleatorio(250, 600) / 10;

        frase = escolhaAleatoria(
            frases.enorme
        );
    }

    textoFrase.textContent = frase;

    salvarResultado(nome, tamanho);

    atualizarTabela();

    entradaNome.value = "";
}


function pegarDados() {

    const dados = localStorage.getItem("ranking");

    if (!dados) {
        return [];
    }

    return JSON.parse(dados);
}


function salvarResultado(nome, tamanho) {

    const dados = pegarDados();

    dados.push({
        nome: nome,
        tamanho: tamanho
    });


    localStorage.setItem(
        "ranking",
        JSON.stringify(dados)
    );
}


function ordenarRanking() {

    const dados = pegarDados();


    dados.sort(function(a, b) {

        return b.tamanho - a.tamanho;

    });


    localStorage.setItem(
        "ranking",
        JSON.stringify(dados)
    );
}


function atualizarTabela() {

    ordenarRanking();


    const dados = pegarDados();


    tabelaRank.innerHTML = "";


    dados.forEach(function(item) {

        const linha = document.createElement("div");

        linha.classList.add(
            "ranking-linha"
        );


        const nome = document.createElement("span");

        nome.textContent = item.nome;


        const tamanho = document.createElement("span");

        tamanho.textContent =
            item.tamanho + " cm";


        linha.appendChild(nome);

        linha.appendChild(tamanho);


        tabelaRank.appendChild(linha);

    });
}


botaoScannear.addEventListener(
    "click",
    scannear
);


atualizarTabela();