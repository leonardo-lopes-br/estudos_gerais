function fatorial(n){
    let mult = 1
    for (n; n!=1; n--){
        mult *= n
    }
    return mult
}
console.log(fatorial(6))