// npm install readline-sync
console.clear()
const readline = require('readline-sync')
let a = readline.questionInt("Digite o primeiro numero: ")
console.log("")
let b = readline.questionInt("Digite o segundo numero: ")
console.log("")
let c = readline.questionInt("Digite o terceiro numero: ")
console.clear()

function soma(x,y,z){
    return x+y+z
}

somatoria=soma(a,b, c)

function mediana(){
    return somatoria/3
}
media=mediana()

console.log("soma: "+ somatoria)
console.log("")
console.log("media aritmetica: "+ media)

