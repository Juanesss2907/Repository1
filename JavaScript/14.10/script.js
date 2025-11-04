console.log("Listo")

var num1;
num1 = parseFloat(prompt("Ingrese un numero"))
var num2;
num2 = parseFloat(prompt("Ingrese un numero"))

var sum = num1 + num2;
document.writeln("<br> El valor de la suma es:  " +sum)
var resta = num1 - num2;
document.writeln("<br> El valor de la sutraccion es: " +resta)
var division = num1 / num2;
document.writeln("<br> El valor de division es: " +division)
var multiplicacion = num1 * num2;
document.writeln("<br> El valor de la multiplicacion es: " +multiplicacion)
var modulo = num1 % num2;
document.writeln("<br> El valor de la modulo es: " +modulo)

altura = prompt("Ingrese el valor de altura")
base = prompt("Ingrese el valor de base")
area = (base * altura)/2
console.log(area);
document.writeln("<br> El area es: " + area)

var cateto1;
cateto1 = parseFloat(prompt("Ingrese el primer cateto"))
var cateto2;
cateto2 = parseFloat(prompt("Ingrese el segundo cateto"))
var hipotenusa = Math.sqrt(cateto1**2 + cateto2**2)
document.writeln("<br> La hipotenusa es: " +hipotenusa)

var celsius;
celsius = parseFloat(prompt("Ingrese los grados"))
var fahrenheit = (celsius * 9/5) + 32
document.writeln("<br> Los grandos son: " +fahrenheit)