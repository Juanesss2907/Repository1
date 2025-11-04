from tkinter import*

def sumar(): #funciona para la operacion suma
    numero1  = int(txt1.get()) # obtener el valor del primer entry
    numero2 = int(txt2.get())  # obtener el valor del segumdo entry
    suma = numero1 +numero2
    return total.set(suma)# retortna el rezultado en el entry total

### inicializacion de la ventana #
ventanap = Tk() # se inicializa el marco del objeto o ventana
ventanap.title("calculadora suma") # titulo de la ventana
ventanap.geometry("500x500") # tamañode la ventana 
ventanap.resizable(False,False)
# que no se pueda modificar el tamaño de la ventana 
ventanap.config(bg="lightblue") #color de fondo de la ventana 

#definicion de etiquetas 
lbl1 = Label(ventanap, text="Numero 1: ",bg="orange", 
             font=("Arial",12))
lbl1.pack(padx=5,pady=3,ipadx=5,ipady=5,fill= X)
##ipad para acomodar el texto dentro del label
##definicion del primer entry
txt1 = Entry(ventanap, font=("Arial", 12))
txt1.pack(padx=5,pady=3,ipadx=5,ipady=5,fill=X)

lbl2 = Label(ventanap, text="Numero 2: ",bg="aquamarine", 
             font=("Arial",12))
lbl2.pack(padx=5,pady=3,ipadx=5,ipady=5,fill= X)
##ipad para acomodar el texto dentro del label
##definicion del primer entry
txt2 = Entry(ventanap, font=("Arial", 12))
txt2.pack(padx=5,pady=3,ipadx=5,ipady=5,fill=X)

btnsumar = Button(ventanap, text="Sumar", bg="pink",
                  font=("Arial",12), command=sumar)
btnsumar.pack(padx=5,pady=3, ipadx=5,ipady=5, fill=X)
## tomar dimensiones del boton, acomodar la ventana y
# el texto en la caja

### label y entry para el resultado
lbresult = Label(ventanap, text="Total: ", bg="lightblue",
                 fg="red", font=("Arial",12))
lbresult.pack(padx=5,pady=3, ipadx=5, ipady=5,fill=X)

total = StringVar()# variable para el resultado

txtresult = Entry(ventanap, state="disabled",font=("Arial",12),
textvariable=total)
txtresult.pack(padx=5,pady=3,ipadx=10,ipady=10,fill=X)
ventanap.mainloop() #cierrre de la ventana principal