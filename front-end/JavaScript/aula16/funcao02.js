function soma(n1=0,n2=0){ // para o caso do usuario não digitar um dos parametros, pois se digitasse apenas um, por exemplo, seria numero + undefined que daria NaN (not a number)
    return n1+n2
}
console.log(soma(345,213))