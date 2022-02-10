class Usuario:

    def __init__(self, dni="", nombre="", correo_electronico="", telefono="", domicilio="", libros_en_prestamo=""):
        self.__dni = dni
        self.__nombre = nombre
        self.__correo_electronico = correo_electronico
        self.__telefono = telefono
        self.__domicilio = domicilio
        self.__libros_en_prestamo = libros_en_prestamo

    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self, dni):
        self.__dni = dni
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    @property
    def correo_electronico(self):
        return self.__correo_electronico
    @correo_electronico.setter
    def correo_electronico(self, correo_electronico):
        self.__correo_electronico = correo_electronico
    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono
    @property
    def domicilio(self):
        return self.__domicilio
    @domicilio.setter
    def domicilio(self, domicilio):
        self.__domicilio = domicilio
    @property
    def libros_en_prestamo(self):
        return self.__libros_en_prestamo
    @libros_en_prestamo.setter
    def libros_en_prestamo(self, libros_en_prestamo):
        self.__libros_en_prestamo = libros_en_prestamo

    def __str__(self):
        if len(self.__libros_en_prestamo) is 0:
            return "DNI: " + self.dni + "\nNombre: " + self.nombre + "\nCorreo: " + self.correo_electronico + "\nTeléfono: " + self.telefono + "\nDomicilio: " + self.domicilio
        else:
            return "DNI: " + self.dni + "\nNombre: " + self.nombre + "\nCorreo: " + self.correo_electronico + "\nTeléfono: " + self.telefono + "\nDomicilio: " + self.domicilio + "\nLibro prestado: " + self.libros_en_prestamo