console.clear()

const readline = require('readline-sync')
console.log("== CALENDARIO ==")
console.log("")
console.log("1-\tdomingo")
console.log("2-\tsegunda")
console.log("3-\tterça")
console.log("4-\tquarta")
console.log("5-\tquinta")
console.log("6-\tsexta")
console.log("7-\tsabado")
console.log("")
let num = readline.questionInt("Digite um numero de 1 a 7: ")
console.log("")



if (num ==1){
    console.log("Domingo \nfinal de semana ")
}else if (num == 2){
    console.log("Segunda \ndia util")

}else if (num == 3){
    console.log("terça \ndia util")

}else if (num == 4){
    console.log("quarta \ndia util")

}else if (num == 5){
    console.log("quinta \ndia util")

}else if (num == 6){
    console.log("sexta \ndia util")

}else if (num == 7){
    console.log("sabado \nfinla de semana")

}else{
    console.log("Valor invalido")
}
