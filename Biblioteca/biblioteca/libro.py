class Libro:

    def __init__(self, isbn="", titulo="", autor="", genero="", portada="", sinopsis="", ejemplares=1, usuario_libro_prestado="", fecha_prestamo=""):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__portada = portada
        self.__sinopsis = sinopsis
        self.__ejemplares = ejemplares
        self.__usuario_libro_prestado = usuario_libro_prestado
        self.__fecha_prestamo = fecha_prestamo

    @property
    def isbn(self):
        return self.__isbn
    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn
    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
    @property
    def autor(self):
        return self.__autor
    @autor.setter
    def autor(self, autor):
        self.__autor = autor
    @property
    def genero(self):
        return self.__genero
    @genero.setter
    def genero(self, genero):
        self.__genero = genero
    @property
    def portada(self):
        return self.__portada
    @portada.setter
    def portada(self, portada):
        self.__portada = portada
    @property
    def sinopsis(self):
        return self.__sinopsis
    @sinopsis.setter
    def sinopsis(self, sinopsis):
        self.__sinopsis = sinopsis
    @property
    def ejemplares(self):
        return self.__ejemplares
    @ejemplares.setter
    def ejemplares(self, ejemplares):
        self.__ejemplares = ejemplares
    @property
    def usuario_libro_prestado(self):
        return self.__usuario_libro_prestado
    @usuario_libro_prestado.setter
    def usuario_libro_prestado(self, usuario_libro_prestado):
        self.__usuario_libro_prestado = usuario_libro_prestado
    @property
    def fecha_prestamo(self):
        return self.__fecha_prestamo
    @fecha_prestamo.setter
    def fecha_prestamo(self, fecha_prestamo):
        self.__fecha_prestamo = fecha_prestamo

    def __str__(self):
        if len(self.usuario_libro_prestado) is 0 and len(self.fecha_prestamo) is 0:
            return "Isbn: " + self.isbn + "\nTítulo: " + self.titulo + "\nAutor: " + self.autor + "\nGénero: " + self.genero + "\nPortada: " + self.portada + "\nSinopsis: " + self.sinopsis + "\nEjemplares: " + str(self.ejemplares)
        else:
            return "Isbn: " + self.isbn + "\nTítulo: " + self.titulo + "\nAutor: " + self.autor + "\nGénero: " + self.genero + "\nPortada: " + self.portada + "\nSinopsis: " + self.sinopsis + "\nEjemplares: " + self.ejemplares + "\nLibro prestado a usuario: " + self.usuario_libro_prestado + "\nFecha préstamo: " + str(self.fecha_prestamo)