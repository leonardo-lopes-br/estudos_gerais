let num = document.querySelector('input#fnum')
let lista = document.querySelector('select#flista')
let res = document.querySelector('div#res')
let valores = []

function isNumero(n){
    if (Number(n) >= 1 && Number(n) <= 100){
        return true
    }else{
        return false
    }
}

function inLista(n,l){
    if(l.indexOf(Number(n)) != -1){
        return true
    }else{
        return false
    }
}


function adicionar(){
    if(isNumero(num.value) && !inLista(num.value, valores)){ // se isNumero for true, ou seja, o numero está entre 1 e 100, E, ALEM DISSO, se !inLista (ou seja se inLista for falso, ou seja, se o elemento não está na lista ainda, faça:)
        valores.push(Number(num.value)) // adiciona o numero digitado no vetor valores
        let item = document.createElement('option') // criando as opções do select
        item.text = `Valor ${num.value} adicionado` // colocando um texto na opção colocada
        lista.appendChild(item) // adicionando os itens na lista
        res.innerHTML = ''

    }else{
        window.alert('Valor inválido ou já encontrado na lista')
    }
    num.value = '' //deixando o espaço para digitar numero vazio após a digitação de um numero, para que o usuário não tenha que ficar apagando o número
    num.focus() // método que serve para deixar o foco do mouse onde adiciona os numeros (o cursos piscando ali como se ja estivesse clicado)
}

function finalizar(){
    if (valores.length == 0){
        window.alert('Adicione valores antes de finalizar!') //caso não tenha nenhum valor adicionado
    }else{
        let tot = valores.length
        let maior = valores[0]
        let menor = valores[0]
        let soma = 0
        let media = 0
        for (let pos in valores){
            soma += valores[pos]
            if (valores[pos] > maior)
                maior = valores[pos]
            if (valores[pos] < menor)
                menor = valores[pos]
        }
        media = soma/tot
        res.innerHTML = ''
        res.innerHTML += `<p> Ao todo temos ${tot} números cadastrados</p>`
        res.innerHTML += `<p>O maior valor informado foi ${maior} </p>`
        res.innerHTML += `<p>O menor valor informado foi ${menor} </p>`
        res.innerHTML += `<p> A soma dos valores é ${soma}</p>`
        res.innerHTML += `<p> A média dos valores é ${media}</p>`
    }
}