// Ejercicio 1
console.log("Esto es ex1.js")

// Ejercicio 2
function boton(){ 
    var nombre = prompt("Ingresa tu nombre:");
    var apellido = prompt("Ingresa tu apellido:");
    var nacimiento = prompt("Ingresa tu año de nacimiento:");
    var año = 2025;
    var edad = año - nacimiento;

    document.getElementById("student_message").innerHTML =
    "Hola, mi nombre es: " + nombre + " " + apellido +
    ", tengo " + edad + " años y estoy aprendiendo Javascript.";
}

// Ejercicio 3
var num1 = parseFloat(document.getElementById("num_1").innerHTML);
var num2 = parseFloat(document.getElementById("num_2").innerHTML);
var promedio = parseFloat((num1 + num2) / 2).toFixed(2);

function boto(){
    document.getElementById("result").innerHTML =
    "El promedio de estos numeros es " + promedio;
}

// Ejercicio 4
var phone1 = "988866552"
var phone2 = "99087612366"
var phone3 = 876543123

console.log(phone1.length == 9)
console.log(phone2.length == 9)
console.log(phone3.toString().length == 9)

// Ejercicio 5
console.log(32**6)

// Ejercicio 8
function Url1() {
    var url2 = document.getElementById("url_1").innerHTML;
    url2 = "https://" + url2;
    document.getElementById("url_2").innerHTML = url2;
}

function Url2() {
    var url3 = document.getElementById("url_3").innerHTML;
    url3 = url3.replace("https://", "");
    document.getElementById("url_4").innerHTML = url3;
}

