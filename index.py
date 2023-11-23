from sympy import *
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr
from tkinter import *


ventana = Tk()
ventana.geometry('900x400')
ventana.title("Cálculo Diferencial e Integral: f(x)")

anuncio = Label(ventana, text="Introduce una función de x:", font=("Times New Roman", 20), fg="black")
anuncio.pack()

funcion = Entry(ventana, font=("Times New Roman", 20))
funcion.pack()

etiqueta = Label(ventana, text="Resultado", font=("Times New Roman", 20), fg="brown")
etiqueta.pack()

boton1 = Button(ventana, text="Derivar Función", font=("Times New Roman", 20), command=Derivar)
boton1.pack()

boton2 = Button(ventana, text="Integrar Función", font=("Times New Roman", 20), command=Integrar)
boton2.pack()

ventana.mainloop()



# PARTE MATEMATICA



def Derivar():
    try:
        x = symbols('x')
        fun_escrita = funcion.get()
        f = parse_expr(fun_escrita)
        derivada = diff(f,x)
        etiqueta.configure(text=derivada)
    except:
        etiqueta.configure(text="Introduce una función correcta")
        
        
def Integrar():
    try:
        x = symbols('x')
        fun_escrita2 = funcion.get()
        g = parse_expr(fun_escrita2)
        integral = integrate(g,x)
        etiqueta.configure(text=integral)
    except:
        etiqueta.configure(text="Introduce una función correcta")




# PARTE GRAFICA



