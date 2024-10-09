"""
Hacer un programa donde se pida un nombre por teclado y se imprima “Hola 'el_nombre_ingresado'”.
"""
import sys
import tkinter as tk

def greet():
    greeting = input_box.get()
    greet_label = tk.Label(text=f'Hola {greeting}!')
    greet_label.pack()

def exit():
    return sys.exit()


window = tk.Tk()
window.geometry('300x300')

label = tk.Label(text='Ingrese su nombre: ')
label.pack()
input_box = tk.Entry()
input_box.pack()
button = tk.Button(text='Enviar', command=greet)
button.pack()
button = tk.Button(text='Salir', command=exit)
button.pack()

window.mainloop()
