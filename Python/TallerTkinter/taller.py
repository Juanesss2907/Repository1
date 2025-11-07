import tkinter as tk

# Ejercicios 1 / 2
ventana1 = tk.Tk()
ventana1.title("Ejercicio 1 y 2")
ventana1.geometry("400x400")

marco1 = tk.Frame(ventana1, width=300, height=300, bg="red")
marco1.pack(padx=25, pady=10)  

texto1 = tk.Label(marco1, text="Hola, soy Juanes Ruiz", bg="lightblue")
texto1.place(relx=0.5, rely=0.5, anchor="center")


# Ejercicios 3 / 4
ventana2 = tk.Toplevel()
ventana2.title("Ejercicio 3 y 4")
ventana2.geometry("450x400")

marco_izq = tk.Frame(ventana2, width=200, height=400, bg="Fuchsia", bd=0) 
marco_izq.pack(side="left")

marco_der = tk.Frame(ventana2, width=200, height=400, bg="Purple", bd=0) 
marco_der.pack(side="right")


# Ejercicio 5
ventana3 = tk.Toplevel()
ventana3.title("Ejercicio 5")
ventana3.geometry("400x400")

filas = 8
columnas = 8
tam_celda = 50

for fila in range(filas):
    for col in range(columnas):
        color = "aqua" if (fila + col) % 2 == 0 else "black"
        celda = tk.Frame(ventana3, width=tam_celda, height=tam_celda, bg=color)
        celda.grid(row=fila, column=col)

ventana1.mainloop()
