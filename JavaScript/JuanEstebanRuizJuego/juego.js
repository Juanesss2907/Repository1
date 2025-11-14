vida = 300
maxVida = 300

function actualizarBarra() {
    ancho = vida

    excesoPositivo = (ancho - maxVida) * (ancho > maxVida)
    excesoNegativo = (0 - ancho) * (ancho < 0)

    ancho = ancho - excesoPositivo - excesoNegativo

    document.getElementById("vida").style.width = ancho + "px"
}

function ataque(cantidad) {
    vida = vida - cantidad
    actualizarBarra()
}

function curarVida(cantidad) {
    vida = vida + cantidad
    actualizarBarra()
}
