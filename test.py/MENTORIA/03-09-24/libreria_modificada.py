# Vamos a crear una biblioteca simple. Tendremos libros con título, autor y si están disponibles o prestados.
# Los usuarios podrán buscar libros, prestarlos y devolverlos.

import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

# Crear tablas
cursor.execute('''CREATE TABLE IF NOT EXISTS Libros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT UNIQUE,
                    autor TEXT,
                    disponible INTEGER,
                    usuario_id INTEGER,
                    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    apellido TEXT,
                    dni TEXT,
                    domicilio TEXT,
                    telefono TEXT,
                    correo TEXT,
                    es_socio INTEGER)''')

conn.commit()

class Usuario:
    def __init__(self, nombre, apellido, dni, domicilio, telefono, correo, es_socio, usuario_id=None):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.domicilio = domicilio
        self.telefono = telefono
        self.correo = correo
        self.es_socio = es_socio
        self.id = usuario_id

    def guardar(self):
        if self.id is None:
            
            cursor.execute('''INSERT INTO Usuarios (nombre, apellido, dni, domicilio, telefono, correo, es_socio)
                          VALUES (?, ?, ?, ?, ?, ?, ?)''',
                          (self.nombre, self.apellido, self.dni, self.domicilio, self.telefono,
                           self.correo, int(self.es_socio)))
            conn.commit()
            self.id = cursor.lastrowid
        else:
            cursor.execute('''UPDATE Usuarios SET nombre = ?, apellido = ?, dni = ?, domicilio = ?, telefono = ?,
                           correo = ?, es_socio = ? WHERE id = ?''',
                           (self.nombre, self.apellido, self.dni, self.domicilio,
                        self.telefono, self.correo, int(self.es_socio), self.id ) )

            conn.commit()
            
    def __str__(self):
        return f"ID: {self.id}, {self.nombre} {self.apellido}, DNI: {self.dni}, Socio {'SI' if self.es_socio else 'NO'}"

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True
        self.usuario_id = None

    def guardar(self):
        cursor.execute('''INSERT INTO Libros (titulo, autor, disponible, usuario_id)
                          VALUES (?, ?, ?, ?)''',
                       (self.titulo, self.autor, int(self.disponible), self.usuario_id))
        conn.commit()

    def prestar(self, usuario_id):
        if self.disponible:
            self.disponible = False
            self.usuario_id = usuario_id
            cursor.execute('''UPDATE Libros SET disponible = ?, usuario_id = ? WHERE titulo = ?''',
                           (int(self.disponible), self.usuario_id, self.titulo))
            conn.commit()
            return True
        return False

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            usuario_id = self.usuario_id
            self.usuario_id = None
            cursor.execute('''UPDATE Libros SET disponible = ?, usuario_id = NULL WHERE titulo = ?''',
                           (int(self.disponible), self.titulo))
            conn.commit()
            return usuario_id
        return None

    def __str__(self):
        estado = "Disponible" if self.disponible else f"Prestado (Usuario ID: {self.usuario_id})"
        return f"'{self.titulo}' por {self.autor} ({estado})"

class Biblioteca:
    def agregar_libro(self, libro):
        libro.guardar()

    def buscar_libro(self, titulo):
        titulo = titulo.lower()
        cursor.execute('''SELECT * FROM Libros WHERE LOWER(titulo) = ?''', (titulo,))
        libro_data = cursor.fetchone()
        if libro_data:
            libro = Libro(libro_data[1], libro_data[2])
            libro.disponible = bool(libro_data[3])
            libro.usuario_id = libro_data[4]
            return libro
        return None

    def prestar_libro(self, titulo, usuario_id):
        libro = self.buscar_libro(titulo)
        if libro and libro.prestar(usuario_id):
            print(f"Has prestado el libro: {libro.titulo} al Usuario ID {usuario_id}")
        else:
            print(f"El libro '{titulo}' no está disponible para prestar.")

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        usuario_id = libro.devolver() if libro else None
        if usuario_id:
            print(f"El usuario ID {usuario_id} ha devuelto el libro: {libro.titulo}")
        else:
            print(f"El libro '{titulo}' no fue prestado.")

    def mostrar_libros(self):
        cursor.execute('''SELECT * FROM Libros''')
        libros = cursor.fetchall()
        for libro in libros:
            estado = "Disponible" if libro[3] else f"Prestado (Usuario ID: {libro[3]})"
            print(f"'{libro[1]}' por {libro[2]} ({estado})")

    def mostrar_usuarios(self):
        cursor.execute('''SELECT * FROM Usuarios''')
        usuarios = cursor.fetchall()
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, {usuario[1]} {usuario[2]}, DNI: {usuario[3]}, Socio: {'Sí' if usuario[7] else 'No'}")


# Ejemplo de uso
biblioteca = Biblioteca()

libro1 = Libro("1984", "George Orwell")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro3 = Libro("La isla del fin del mundo", "Julio Verne")
libro4 = Libro("Viaje al fondo de la tierra", "Julio Verne")
libro5 = Libro("La Biblia","La Iglesia")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)
biblioteca.agregar_libro(libro5)

# Menú interactivo
while True:
    print("\n1. Registrar usuario")
    print("2. Buscar libro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Mostrar todos los libros")
    print("6. Mostrar todos los usuarios")
    print("7. Modificar usuario")
    print("8. Salir")
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        dni = input("Ingrese el DNI: ")
        domicilio = input("Ingrese el domicilio: ")
        telefono = input("Ingrese el teléfono: ")
        correo = input("Ingrese el correo: ")
        es_socio = int(input("¿Es socio? (1: Sí, 0: No): "))
        usuario = Usuario(nombre, apellido, dni, domicilio, telefono, correo, es_socio)
        usuario_id = usuario.guardar()
        print(f"Usuario registrado con ID: {usuario_id}")

    elif opcion == 2:
        titulo = input("Ingrese el título del libro: ")
        libro = biblioteca.buscar_libro(titulo)
        if libro:
            print(f"El libro '{libro.titulo}' está {'disponible' if libro.disponible else 'prestado'}.")
        else:
            print("Libro no encontrado.")

    elif opcion == 3:
        biblioteca.mostrar_usuarios()
        usuario_id = int(input("Ingrese el ID del usuario que retira el libro: "))
        titulo = input("Ingrese el título del libro a prestar: ")
        biblioteca.prestar_libro(titulo, usuario_id)

    elif opcion == 4:
        titulo = input("Ingrese el título del libro a devolver: ")
        biblioteca.devolver_libro(titulo)

    elif opcion == 5:
        biblioteca.mostrar_libros()

    elif opcion == 6:
        cursor.execute('''SELECT * FROM Usuarios''')
        usuarios = cursor.fetchall()
        for usuario_data in usuarios:
            usuario = Usuario(usuario_data[1], usuario_data[2], usuario_data[3], usuario_data[4], usuario_data[5], usuario_data[6], usuario_data[0])
            print(usuario)
        
    elif opcion == 7:
        usuario_id = int(input("Ingrese el ID del usuario a modificar: "))
        cursor.execute('''SELECT * FROM Usuarios WHERE id = ?''', (usuario_id,))
        usuario_data = cursor.fetchone()
        if usuario_data:
            nombre = input(f"Nombre ({usuario_data[1]}): ") or usuario_data[1]
            apellido = input(f"Apellido ({usuario_data[2]}): ") or usuario_data[2]
            dni = input(f"DNI ({usuario_data[3]}): ") or usuario_data[3]
            domicilio = input(f"Domicilio ({usuario_data[4]}): ") or usuario_data[4]
            telefono = input(f"Teléfono ({usuario_data[5]}): ") or usuario_data[5]
            correo = input(f"Correo ({usuario_data[6]}): ") or usuario_data[6]
            es_socio = int(input(f"¿Es socio? (1 para Sí, 0 para No) ({usuario_data[7]}): ") or usuario_data[7])
            usuario = Usuario(nombre, apellido, dni, domicilio, telefono, correo, es_socio, usuario_id)
            usuario.guardar()
        else:
            print("Usuario no encontrado.")

    elif opcion == 8:
        break

    else:
        print("Opción inválida.")

# Cerrar la conexión a la base de datos
conn.close()
