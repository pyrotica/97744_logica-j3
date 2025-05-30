console.clear()

const readline = require('readline-sync')
console.log("")
let num = readline.questionInt("Digite um numero: ")
console.log("")


console.clear()
if (num % 2 ==0){
    console.log(num +" é um numero par")
}else{
    console.log(num +" é um numero impar")
}

