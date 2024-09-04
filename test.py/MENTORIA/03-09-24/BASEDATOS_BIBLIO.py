import sqlite3

#conecto a la base de datos (se va a crear si no existe)
conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()


# Crearr una tabla de usuarios

cursor-execute('''
CREATE TABLE IF NOT EXISTS Usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    dni TEXT NOT NULL UNIQUE,
    domicilio TEXT,
    telefono TEXT,  
    correo TEXT,
    es_socio INTEGER NOT NULL
)
''')

# CREO TABLA DE LIBROS

cursor.execute('''
CREATE TABLE IF NOT EXISTS Libros(
    id INTEGEWR PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    disponible INTEGER NOT NULL DEFAULT 1,
    usuario_id INTEGER,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
)
''')

# confirmar los cambieos

conn.commit()

# cerrar la conexion
conn.close()

print("La base de datos y las tablas han sido creadas exitosamente.")