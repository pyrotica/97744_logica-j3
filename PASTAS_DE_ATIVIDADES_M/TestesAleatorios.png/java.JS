function soma(a, b) {
    return a + b;
  }
  
  // Solicita ao usuário para digitar o primeiro número
  const numero1 = parseInt(prompt("Digite o primeiro número inteiro: "), 10);
  
  // Solicita ao usuário para digitar o segundo número
  const numero2 = parseInt(prompt("Digite o segundo número inteiro: "), 10);
  
  // Calcula a soma dos dois números
  const resultado = soma(numero1, numero2);
  
  // Exibe o resultado da soma
  console.log(`A soma dos dois números é: ${resultado}`);