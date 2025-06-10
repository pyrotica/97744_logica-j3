//Criando um vetor com numeros
const listadenumeros = [1,2,6]
const tamanho=listadenumeros.length
console.log(tamanho)
console.log(listadenumeros)
console.clear()
let soma =0;
listadenumeros.forEach(num  =>{
        soma+=num;
        media=soma/tamanho
});

console.log("A soma dos numeros é:", soma)
console.log()
console.log("A media dos numeros é:", media)
