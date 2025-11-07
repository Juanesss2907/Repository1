from tkinter import *

# Funciones de operación
def operar(tipo):
    try:
        numero1 = float(txt1.get())
        numero2 = float(txt2.get())

        if tipo == "suma":
            resultado = numero1 + numero2
        elif tipo == "resta":
            resultado = numero1 - numero2
        elif tipo == "multiplicacion":
            resultado = numero1 * numero2
        elif tipo == "division":
            if numero2 == 0:
                resultado = "Error: división por cero"
            else:
                resultado = numero1 / numero2
        else:
            resultado = "Operación inválida"

        total.set(resultado)
    except ValueError:
        total.set("Error: entrada inválida")

# Configuración de ventana principal
ventana = Tk()
ventana.title("Calculadora Básica")
ventana.geometry("400x450")
ventana.resizable(False, False)
ventana.config(bg="#f0f4f8")

# Estilos
fuente_label = ("Segoe UI", 12, "bold")
fuente_entry = ("Segoe UI", 12)
fuente_boton = ("Segoe UI", 12, "bold")
color_resultado = "#333333"

# Etiquetas y entradas
Label(ventana, text="Número 1:", font=fuente_label, bg="#f0f4f8").pack(pady=(20, 5))
txt1 = Entry(ventana, font=fuente_entry, justify="center")
txt1.pack(padx=20, pady=5, ipady=5, fill=X)

Label(ventana, text="Número 2:", font=fuente_label, bg="#f0f4f8").pack(pady=5)
txt2 = Entry(ventana, font=fuente_entry, justify="center")
txt2.pack(padx=20, pady=5, ipady=5, fill=X)

# Botones de operación
FrameBotones = Frame(ventana, bg="#f0f4f8")
FrameBotones.pack(pady=15)

Button(FrameBotones, text="Sumar", font=fuente_boton, bg="#4CAF50", fg="white",
       command=lambda: operar("suma")).pack(side=LEFT, padx=5, ipadx=10, ipady=5)

Button(FrameBotones, text="Restar", font=fuente_boton, bg="#2196F3", fg="white",
       command=lambda: operar("resta")).pack(side=LEFT, padx=5, ipadx=10, ipady=5)

Button(FrameBotones, text="Multiplicar", font=fuente_boton, bg="#FF9800", fg="white",
       command=lambda: operar("multiplicacion")).pack(side=LEFT, padx=5, ipadx=10, ipady=5)

Button(FrameBotones, text="Dividir", font=fuente_boton, bg="#9C27B0", fg="white",
       command=lambda: operar("division")).pack(side=LEFT, padx=5, ipadx=10, ipady=5)

# Resultado
Label(ventana, text="Resultado:", font=fuente_label, bg="#f0f4f8").pack(pady=10)
total = StringVar()
txtresult = Entry(ventana, font=fuente_entry, textvariable=total,
                  state="readonly", justify="center", fg=color_resultado)
txtresult.pack(padx=20, pady=5, ipady=5, fill=X)

ventana.mainloop()