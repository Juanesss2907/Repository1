var vidaActual = 300;

var limitesVida = [];
for (var i = 0; i <= 300; i++) {
    limitesVida[i] = i;
}

function ataque(valor) {
    vidaActual = limitesVida[(vidaActual - valor) * ((vidaActual - valor) >= 0) + 0 * ((vidaActual - valor) < 0)];
    actualizarVida();
}

function curarVida(valor) {
    vidaActual = limitesVida[(vidaActual + valor) * ((vidaActual + valor) <= 300) + 300 * ((vidaActual + valor) > 300)];
    actualizarVida();
}

function actualizarVida() {
    var barra = document.getElementById("vida");
    var numero = document.getElementById("vida-numero");
    barra.style.width = vidaActual + "px";
    numero.innerHTML = vidaActual;
}

