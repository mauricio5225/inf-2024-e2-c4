#ejemplo boton saludo
#agregar el boton 4 en la zona de abajo

import tkinter as tk

ventana = tk.Tk()
ventana.title('¡Ahora tenemos 4 botones!')
ventana.geometry('400x200')

boton1 = tk.Button(ventana, text="Botón 1")
boton2 = tk.Button(ventana, text="Botón 2")
boton3 = tk.Button(ventana, text="Botón 3")
boton4 = tk.Button(ventana, text="Botón 4")  # Nuevo botón 4

boton1.pack(side="top")
boton2.pack(side="left")
boton3.pack(side="right")
boton4.pack(side="bottom")  # Empaquetar el botón 4 en la parte inferior

ventana.mainloop()
