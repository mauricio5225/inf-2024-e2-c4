
#Mayra Noemi Perez
#16:36
# Menú de la aplicación
# Menú de la aplicación

from tkinter import Tk, Menu

ventana = Tk()
menu_barra = Menu(ventana)

import tkinter as tk

ventana = tk.Tk()
menu_barra = tk.Menu(ventana)
menu_archivo = tk.Menu(menu_barra, tearoff=0)

# Añadir más elementos al menú si es necesario
menu_barra.add_cascade(label="Archivo", menu=menu_archivo)

ventana.config(menu=menu_barra)
ventana.mainlo






ventana.config(menu=menu_barra)
menu_archivo = tk.Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Salir", command=ventana.quit)

# Reloj
etiqueta_reloj = tk.Label(ventana, font=('Arial', 18), fg="yellow", bg='blue4')
etiqueta_reloj.place(anchor='ne', relx=1, rely=0.05)  # n, ne, e, se, s, sw, w, nw, or center
# etiqueta_reloj.pack(pady=1)
etiqueta_semana = tk.Label(ventana, font=("Arial", 18), fg="yellow", bg='blue4')
etiqueta_semana.place(anchor='ne', relx=1, rely=0.00)  # etiqueta_semana.pack(pady=1)
actualizar_reloj()

# Lista de empleados (menú desplegable)
label_empleado = tk.Label(ventana, text="Seleccione su nombre:", font=('Arial', 14), bg='orange', fg='Blue4')
label_empleado.place(anchor='nw', relx=0, rely=0)  # label_empleado.pack(pady=5)

listbox_empleados = ttk.Combobox(ventana, values=empleados, state='readonly')
listbox_empleados.current(0)  # Establecer el valor por defecto
listbox_empleados.place(anchor='nw', relx=0.20, rely=0.001)  # listbox_empleados.pack()

# Botón para abrir la lista de empleados con scroll
boton_lista_completa = tk.Button(ventana, text="Ver lista completa", font=('Arial', 12), bg='lime green', fg='black', command=abrir_lista_empleados)
boton_lista_completa.place(anchor='nw', relx=0.02, rely=0.05)  # boton_lista_completa.pack(pady=5)

# Botones de Entrada y Salida
boton_entrada = tk.Button(ventana, text="Entrada", bg='lime green', fg='black', command=lambda: registrar_entrada_salida("entrada"))
boton_entrada.place(anchor='nw', relx=0.20, rely=0.05)  # boton_entrada.pack(pady=5)

boton_salida = tk.Button(ventana, text="Salida", bg='lime green', fg='black', command=lambda: registrar_entrada_salida("salida"))
boton_salida.place(anchor='nw', relx=0.30, rely=0.05)  # boton_salida.pack(pady=5)

# Botón de registro
boton = tk.Button(ventana, text="Registro de asistencia", command=lambda: mostrar_ventana_secundaria(ventana))
boton.place(anchor='center', relx=0.5, rely=0.5)  # boton.pack()

# Etiqueta para mensajes de error
mensaje_error = tk.Label(ventana, text="", fg="yellow", bg='black', font=('Arial', 20))
mensaje_error.place(anchor='nw', relx=0, rely=0.10)  # mensaje_error.pack(pady=5, padx=5) y largo //x ancho

# Etiqueta de registro
etiqueta_resultado = tk.Label(ventana, text="", bg='orange')
# etiqueta_resultado.pack()
# resultado=tk.Label()
# resultado.pack()

# Cuadro de entrada para agregar nuevo empleado
label_nuevo_empleado = tk.Label(ventana, text="Agregar nuevo empleado:", font=('Arial', 14), bg='orange', fg='Blue4')
label_nuevo_empleado.place(anchor='nw', relx=0.00, rely=0.20)  # label_nuevo_empleado.pack(pady=5)

entrada_nuevo_empleado = tk.Entry(ventana)
entrada_nuevo_empleado.place(anchor='nw', relx=0.23, rely=0.21)  # entrada_nuevo_empleado.pack(pady=10)

boton_agregar_empleado = tk.Button(ventana, text="Agregar", command=agregar_empleado, bg='lime green', fg='black')
boton_agregar_empleado.place(anchor='nw', relx=0.23, rely=0.25)  # boton_agregar_empleado.pack(pady=5)

# Botón para eliminar empleado
boton_eliminar_empleado = tk.Button(ventana, text="Eliminar empleado", command=eliminar_empleado, bg='lime green', fg='black')
boton_eliminar_empleado.place(anchor='nw', relx=0.30, rely=0.25)  # boton_eliminar_empleado.pack(pady=5)

# Lista de registros (con barra de desplazamiento)
frame_registro = tk.Frame(ventana)
frame_registro.pack(side=tk.BOTTOM, pady=5, fill=tk.X, expand=False)
# frame_registro.place(anchor='center', relx=0.5, rely=0.5)

scrollbar = tk.Scrollbar(frame_registro)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)  # CURSOR

lista_registro = tk.Listbox(frame_registro, background='bisque', yscrollcommand=scrollbar.set)
lista_registro.pack(fill=tk.X, expand=True)  # TABLERO

scrollbar.config(command=lista_registro.yview)
