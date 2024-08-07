import tkinter as tk

ventana = tk.Tk()
ventana.title('Mi primera ventana con Tkinter')
ventana.geometry('400x600')

etiqueta = tk.Label(ventana, text='Hola mundo!', font=('Arial', 20))
etiqueta.pack()



ventana.mainloop()