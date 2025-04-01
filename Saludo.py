"""
Hacer un programa donde se pida un nombre por teclado y se imprima “Hola 
..el_nombre_ingresado”

"""

import tkinter as tk
from tkinter import messagebox as MessageBox

class Saludo:
    def __init__(self, nombre = str()):
        self.nombre = nombre    

raiz = tk.Tk()
raiz.geometry('200x100')

nombre = Saludo()

def saludame():
    nombre.nombre = entrada.get()
    MessageBox.showinfo(message=f'Hola {nombre.nombre}!')
    
etiqueta = tk.Label(raiz, text='Ingresa tu nombre')
etiqueta.pack()
entrada = tk.Entry(raiz)
entrada.pack()
boton = tk.Button(raiz, text='Saludame', command=saludame)
boton.pack()
boton_salida = tk.Button(raiz, text='Salir', command=raiz.destroy)
boton_salida.pack()

raiz.mainloop()
