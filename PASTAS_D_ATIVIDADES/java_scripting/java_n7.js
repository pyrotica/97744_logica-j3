console.clear()

const readline = require('readline-sync')
console.log("")
let A = readline.questionInt("Digite um numero para o A: ")
console.log("")
let B = readline.questionInt("Digite um numero para o B: ")
console.log("")
let C = readline.questionInt("Digite um numero para o C: ")
console.log("")

AB= A+B
console.clear()

if (AB >C){
    console.log("A+B é maior que C " + "\nA+B: " + AB +" C: " + C)
}else if (AB<C){
    console.log("A+B é menor que C " + "\nA+B: " + AB +" C: " + C)
}else{
    console.log("A+B é igual a C")
}

