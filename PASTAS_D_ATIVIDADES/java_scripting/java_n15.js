//Criando um vetor com numeros
const listadenumeros = [1,2,3,4,5]

console.log(`lisando todos os numeros da lista`)
console.log(listadenumeros)

console.log(`\n= multiplicando valors por 2 =`)
const dobrados = listadenumeros.map (numero => numero * 2)
console.log(dobrados)

console.log(`= filtrando numeros pares =`)
const pares = listadenumeros.filter(numero => numero % 2 === 0)
console.log(pares)

console.log(`= somando todos os numeros =`)
const soma = listadenumeros.reduce = ((soma, atual) => soma + atual, 0)
console.log(soma)
