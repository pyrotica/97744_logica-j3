//Criando um vetor com numeros
const listadenumeros = [1,2,3,4,5,9]
let pareso=0
let imperoso=0
console.log(`lisando todos os numeros da lista`)
console.log(listadenumeros)
console.clear()
// console.log(`\n= multiplicando valors por 2 =`)
// const dobrados = listadenumeros.map (numero => numero * 2)
// console.log(dobrados)

listadenumeros.forEach(num =>{
    if(num % 2 ==0){
        pareso+=1;
    }else{
    
     imperoso+=1;
    }
});
console.log("a quantidade de pares é:", pareso, "\ne a quantidade de impares é", imperoso)

