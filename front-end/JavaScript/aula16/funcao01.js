function parimpar(n){
    if (n%2 == 0){
        return 'Par!'
    }else{
        return 'Impar!'
    }
}
let num = 13
let res = parimpar(num)
console.log(`O número ${num} é um número ${res}`)