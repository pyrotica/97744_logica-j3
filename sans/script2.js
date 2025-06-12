const battleText = document.getElementById('battle-text');
const startBtn = document.getElementById('start-btn');

const frasesSans = [
    "Sans: você vai ter um tempo difícil...",
    "Sans: é um trabalho sujo, mas alguém tem que fazer.",
    "Sans: você realmente quer fazer isso?",
    "Sans: prepare-se para o pior.",
    "* Sans sorri de forma estranha.",
    "* Você sente que sua determinação está sendo testada..."
];

startBtn.addEventListener('click', () => {
    // Escolhe uma frase aleatória do Sans
    const frase = frasesSans[Math.floor(Math.random() * frasesSans.length)];
    battleText.textContent = frase;
    startBtn.textContent = "Atacar!";
    startBtn.disabled = true;

    setTimeout(() => {
        battleText.textContent = "* A luta começou! Prepare-se!";
        startBtn.style.display = 'none';
    }, 2000);
});