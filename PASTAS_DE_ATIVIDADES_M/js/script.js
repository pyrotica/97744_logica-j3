// Alunos: Cauã Costa Sena e Kauan Gabriel 

//  ----------------- Dom ---------------------
const Troca = document.querySelector('#Troca')
const filme1 = document.querySelector('#bt_01')
const filme2 = document.querySelector('#bt_02')
const filme3 = document.querySelector('#bt_03')
const filme4 = document.querySelector('#bt_04')
const filme5 = document.querySelector('#bt_05')
// ---------------------------------------------

filme1.addEventListener('click', trocaf1)
filme2.addEventListener('click', trocaf2)
filme3.addEventListener('click', trocaf3)
filme4.addEventListener('click', trocaf4)
filme5.addEventListener('click', trocaf5)

function trocaf1(){
    Troca.src="images/John Wick 4 - Poster.jpg"
}

function trocaf2(){
    Troca.src="images/Creed 3 - Poster.webp"
}

function trocaf3(){
    Troca.src="images/Aranha-verso - Poster.webp"
}

function trocaf4(){
    Troca.src="images/poster-venom-d-033069a1.jpg"
}
function trocaf5(){
    Troca.src="images/MV5BY2I4ZGQzZjgtMjU0Yi00MjRmLWI1NjMtZjBjN2NjNmY4NGRmXkEyXkFqcGc@._V1_.jpg"
}

