"""Página de inicio interactiva:
Componentes: Menú desplegable, Reloj simple.
Descripción: Una página de inicio con un menú desplegable para
navegar entre diferentes secciones de la página y un reloj
simple que muestra la hora actual en la esquina superior derecha."""

import tkinter as tk
from tkinter import Menu
import time

# Función para actualizar el reloj
def actualizar_reloj():
    hora_actual = time.strftime('%H:%M:%S')
    etiqueta_reloj.config(text=hora_actual)
    etiqueta_reloj.after(1000, actualizar_reloj)

# Funciones para los menús
def mostrar_seccion1():
    etiqueta_principal.config(text="Sección 1 seleccionada")

def mostrar_seccion2():
    etiqueta_principal.config(text="Sección 2 seleccionada")

def salir():
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Página de Inicio Interactiva")
root.geometry("400x200")

# Menú desplegable
menu_bar = Menu(root)
root.config(menu=menu_bar)

menu_navegacion = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Navegar", menu=menu_navegacion)
menu_navegacion.add_command(label="Sección 1", command=mostrar_seccion1)
menu_navegacion.add_command(label="Sección 2", command=mostrar_seccion2)
menu_navegacion.add_separator()
menu_navegacion.add_command(label="Salir", command=salir)

# Etiqueta principal
etiqueta_principal = tk.Label(root, text="Bienvenido a la Página de Inicio", font=('Helvetica', 16))
etiqueta_principal.pack(pady=50)

# Reloj en la esquina superior derecha
etiqueta_reloj = tk.Label(root, font=('Helvetica', 12))
etiqueta_reloj.place(relx=1.0, rely=0.0, anchor='ne')
actualizar_reloj()

# Ejecución de la ventana
root.mainloop()
