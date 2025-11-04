function sumar() {
    var n1 = parseFloat(document.getElementById("numero1").value);
    var n2 = parseFloat(document.getElementById("numero2").value);
    var r = n1 + n2;
    document.getElementById("resultado").textContent = "El resultado de la suma entre " + n1 + " y "+ n2 + " es : " + r;
}

function restar() {
    var n1 = parseFloat(document.getElementById("numero1").value);
    var n2 = parseFloat(document.getElementById("numero2").value);
    var r = n1 - n2;
    document.getElementById("resultado").textContent = "El resultado de la resta entre " + n1 + " y "+ n2 + " es : " + r;
}

function multiplicar() {
    var n1 = parseFloat(document.getElementById("numero1").value);
    var n2 = parseFloat(document.getElementById("numero2").value);
    var r = n1 * n2;
    document.getElementById("resultado").textContent = "El resultado de la multiplicación entre " + n1 + " y "+ n2 + " es : " + r;
}

function dividir() {
    var n1 = parseFloat(document.getElementById("numero1").value);
    var n2 = parseFloat(document.getElementById("numero2").value);
    var r = n1 / n2;
    document.getElementById("resultado").textContent = "El resultado de la división entre " + n1 + " y "+ n2 + " es : " + r;
}
