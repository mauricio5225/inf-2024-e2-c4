class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # El libro está disponible al ser agregado

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return True
        return False

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' por {self.autor} ({estado})"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro and libro.prestar():
            print(f"Han prestado el libro: {libro.titulo}")
        else:
            print(f"El libro '{titulo}' no está disponible para prestar.")

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro and libro.devolver():
            print(f"Han devuelto el libro: {libro.titulo}")
        else:
            print(f"El libro '{titulo}' no fue prestado.")

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)


# Ejemplo de uso
biblioteca = Biblioteca()

libro1 = Libro("veintemil leguas de viaje de submarino", "juio verne")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.mostrar_libros()

biblioteca.prestar_libro("veintemil leguas de viaje de submarino")
biblioteca.mostrar_libros()

biblioteca.devolver_libro("veintemil leguas de viaje de submarino")
biblioteca.mostrar_libros()
