function cambiar(){
    var nombre = document.getElementById("cajita").value
    document.getElementById("Resultado").innerHTML="Bienvenido "+ nombre
}

function sumar(){
    
    var num1 = parseFloat(document.getElementById("n1").innerHTML)
    var num2 = parseFloat(document.getElementById("n2").innerHTML)
    var sumar = num1 + num2
    document.getElementById("Resultado1").innerHTML="La suma es "+ sumar
}