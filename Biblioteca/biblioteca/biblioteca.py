from .usuario import Usuario 
from .libro import Libro
from datetime import datetime
#import usuario
#import libro

usuarios = []
libros = []
class Biblioteca:
    def __init__(self):
        pass

    def alta_socio():
        dni = input("Introduce el dni del usuario: ")
        nombre = input("Introduce el nombre del usuario: ")
        correo = input("Introduce correo del usuario: ")
        telefono = input("Introduce telefono del usuario: ")
        domicilio = input("Introduce el domicilio del usuario: ")
        libro_prestamo = ""
        user = Usuario(dni, nombre, correo, telefono, domicilio, libro_prestamo)
        #user = usuario.Usuario(dni, nombre, correo, telefono, domicilio, libro_prestamo)
        usuarios.append(user)
        return user

    def baja_socio():
        dni = input("Introduce el dni del usuario: ")
        for i in range(0,len(usuarios)):
            if usuarios[i].dni == dni:
                usuarios.remove(usuarios[i])

    def alta_libro():
        isbn = input("Introduce el isbn del libro: ")
        titulo = input("Introduce el titulo del libro: ")
        autor = input("Introduce autor del libro: ")
        genero = input("Introduce genero del libro: ")
        portada = input("Introduce el portada del libro: ")
        sinopsis = input("Introduce el sinopsis del libro: ")
        try:
            ejemplares = int(input("Introduce el ejemplares del libro: "))
        except:
            print("📛 El valor esperado era un número 📛")
            ejemplares = None
        if ejemplares is not None:
            usuario_libro_prestado = ""
            fecha_presatamo = ""
            book = Libro(isbn, titulo, autor, genero, portada, sinopsis, ejemplares, usuario_libro_prestado, fecha_presatamo)
            libros.append(book)
            return book
        else: 
            print("No se pudo ingresar el libro porque no hay ejemplares asignados")

    def baja_libro():
        isbn = input("Introduce el isbn del libro: ")
        for i in range(0,len(libros)):
            if libros[i].isbn == isbn:
                libros.remove(libros[i])
    
    def prestar():
        dni = input("Introduce el dni del socio a prestar: ")
        isbn = input("Introduce el isbn del libro a prestar: ")
        for i in range(0,len(usuarios)):
            if usuarios[i].dni == dni:
                 for i in range(0, len(libros)):
                     if libros[i].isbn == isbn:
                         usuarios[i].libros_en_prestamo = libros[i].isbn
                         libros[i].usuario_libro_prestado = usuarios[i].dni
                         libros[i].fecha_prestamo = str(datetime.now())
                         print("Se ha prestado el libro con ISBN " + libros[i].isbn + " al usuario con DNI " + usuarios[i].dni)

    def devolver():
        isbn = input("Introduce el libro a devolver: ")
        dni = input("¿Qué usuario quiere devolver el libro? DNI: ")
        for i in range(0, len(libros)):
            if libros[i].isbn == isbn:
                for i in range(0, len(usuarios)):
                    if usuarios[i].dni == dni:
                        usuarios[i].libros_en_prestamo = ""
                        libros[i].usuario_libro_prestado = ""
                        libros[i].fecha_presatamo = ""
                        print("Se ha devuelto el libro con ISBN " + libros[i].isbn)
    
    def consultar_libros():
        for i in range(0, len(libros)):
            print(libros[i])

    def consultar_libro():
        isbn = input("¿Qué libro quieres consultar? ISBN: ")
        for i in range(0, len(libros)):
            if libros[i].isbn == isbn:
                print(libros[i])

    def consultar_usuarios():
        for i in range(0, len(usuarios)):
            print(usuarios[i])
    
    def consultar_usuario():
        dni = input("Introduce el dni del usuario: ")
        for i in range(0, len(usuarios)):
            if usuarios[i].dni == dni:
                print(usuarios[i])

    def consultar_prestamos_usuarios():
        for i in range(0, len(usuarios)):
            if not usuarios[i].libros_en_prestamo:
                print("EL usuario con DNI: " + usuarios[i].dni+" no tiene ningún libro prestado")  
            else:
                print("EL usuario con DNI: " + usuarios[i].dni+" tiene presatado el libro " + usuarios[i].libros_en_prestamo)  
    
    def consultar_prestamo_libros():
        for i in range(0, len(libros)):
            if not libros[i].fecha_prestamo and not libros[i].usuario_libro_prestado:
                print("El libro con ISBN: " + libros[i].isbn + " no se le ha prestado a ningún usuario")
            else:
                print("El libro con ISBN: " + libros[i].isbn + " fué prestado en el momento: " + libros[i].fecha_prestamo + " y lo tiene el usuario con DNI " + libros[i].usuario_libro_prestado)
