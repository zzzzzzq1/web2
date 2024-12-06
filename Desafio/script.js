
function escreverNumeros() {
    
    var n = parseInt(prompt("Digite o número até onde você quer contar:"))
    
    if (isNaN(n) || n <= 0) {
        alert("Por favor, insira um número válido maior que 0.");
        return;
    }

    var numeros = "";
    for (var i = 1; i <= n; i++) {
        numeros += i + " "; // Concatena os números
    }

    document.getElementById("numerosDiv").innerText = numeros;
}
