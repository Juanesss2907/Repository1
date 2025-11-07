console.log("Conexion Establecida");

function ej1() {
  var n1 = parseFloat(document.getElementById("num1").value);
  var n2 = parseFloat(document.getElementById("num2").value);

  var suma = n1 + n2;
  var resta = n1 - n2;
  var mult = n1 * n2;
  var div = n1 / n2;
  var mod = n1 % n2;

  document.getElementById("resultado1").innerHTML =
    "Suma: " + suma + "<br>" +
    "Resta: " + resta + "<br>" +
    "Multiplicacion: " + mult + "<br>" +
    "Division: " + div + "<br>" +
    "Modulo: " + mod;
}

function ej2() {
  var base = parseFloat(document.getElementById("base").value);
  var altura = parseFloat(document.getElementById("altura").value);
  var area = (base * altura) / 2;

  document.getElementById("resultado2").innerHTML = "Area: " + area;
}

function ej3() {
  var c1 = parseFloat(document.getElementById("cat1").value);
  var c2 = parseFloat(document.getElementById("cat2").value);
  var hip = Math.sqrt(c1 * c1 + c2 * c2);

  document.getElementById("resultado3").innerHTML = "Hipotenusa: " + hip;
}

function ej4() {
  var c = parseFloat(document.getElementById("celsius").value);
  var f = (c * 9/5) + 32;

  document.getElementById("resultado4").innerHTML = "Fahrenheit: " + f;
}

