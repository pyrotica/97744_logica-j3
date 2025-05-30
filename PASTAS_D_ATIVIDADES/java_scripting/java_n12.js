// npm install readline-sync
console.clear()
const readline = require('readline-sync')

function verificar(){
    
    if (num<0){
        console.log("Numero negativo")
        }else{
        console.log("numero positivo")
        }
        
}

let num = readline.questionInt("Digite um numero: ")
console.log("")
verificar(num)

