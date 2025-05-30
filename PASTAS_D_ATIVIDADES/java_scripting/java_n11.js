// npm install readline-sync

const readline = require('readline-sync')
function par_impar(){


    console.log("")
    for (let i =40; i<50; i++){
    
    
        console.log(i);
        if (i % 2 ==0){
        par=par_impar()
        }else{
        impar=par_impar()
        }
    
    }
} 
console.log("pares: " + par)
console.log("impares: " + impar)