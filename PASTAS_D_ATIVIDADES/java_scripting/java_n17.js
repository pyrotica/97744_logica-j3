//Criando um vetor com numeros
const listadenumeros = [1,2,-3,4,-5, 9, -9]
let negativismo=0
console.log(listadenumeros)
console.clear()
let soma =0;
listadenumeros.forEach(num  =>{
    if(num <0){
        negativismo+=1;

    }else if(num >0){
        soma+=num;
     
    }
});
console.log("a quantidade de negativos é:", negativismo)
console.log("A soma dos positivos é:", soma)
