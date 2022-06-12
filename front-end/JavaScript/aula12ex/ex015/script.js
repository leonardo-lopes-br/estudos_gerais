function verificar(){
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.getElementById('res')
    if (fano.value.lenght == 0 || fano.value > ano){
        window.alert('Verifique os dados e tente novamente')
    }else{
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id','foto')
        if (fsex[0].checked){
            genero = 'Homem'
            if (idade >= 0 && idade < 10){
                img.setAttribute('src', 'foto-bebe-m.png')
                //criança
            }else if(idade < 21){
                img.setAttribute('src', 'foto-jovem-m.png')
                //jovem
            }else if(idade < 50){
                img.setAttribute('src', 'foto-adulto-m.png')
                //adulto
            }else{
                img.setAttribute('src', 'foto-velho-m.png')
                //velho
            }
        }else if(fsex[1].checked){
            genero = 'Mulher'
            if (idade >= 0 && idade < 10){
                img.setAttribute('src', 'foto-bebe-f.png')
                //criança
            }else if(idade < 21){
                img.setAttribute('src', 'foto-jovem-f.png')
                //jovem
            }else if(idade < 50){
                img.setAttribute('src', 'foto-adulto-f.png')
                //adulto
            }else{
                img.setAttribute('src', 'foto-velho-f.png')
                //velho
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectados gênero ${genero} com ${idade} anos`
        res.appendChild(img)
    }
}