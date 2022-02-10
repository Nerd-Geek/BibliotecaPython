from .biblioteca import Biblioteca

class Menu:
    def main():
        salir = True

        while(salir):
            print("1- Alta de socio ✅")
            print("2- Baja de socio ❌")
            print("3- Alta de libro ✅")
            print("4- Baja de libro ❌")
            print("5- Prestar libro 🤝")
            print("6- Devolver libro 📚")
            print("7- Consultar libros 🔎📙")
            print("8- Consultar usuarios 🔎🙂")
            print("9- Consultar prestamos 🔎🤝")
            print("10- Salir 🔚")
            try:
                opcion = int(input("¿Que opción escoges?\n"))
            except ValueError:
                print("📛 El valor esperado era un número 📛")
                opcion = None
            if opcion == 1:
                Biblioteca.alta_socio()
                print("Se ha dado de alta un socio")
            elif opcion == 2:
                Biblioteca.baja_socio()
                print("Se ha dado de baja un libro")
            elif opcion == 3:
                Biblioteca.alta_libro()
                print("Se ha dado de alta un libro")
            elif opcion == 4:
                Biblioteca.baja_libro()
                print("Se ha dado de baja un libro")
            elif opcion == 5:
                Biblioteca.prestar()
            elif opcion == 6:
                Biblioteca.devolver()
            elif opcion == 7:
                try:
                    opcion_dos = int(input("1. Obtener todos los libros \n2. Obtener un libro \n"))
                except ValueError:
                    print("📛 El valor esperado era un número 📛")
                    opcion_dos = None
                if opcion_dos == 1:
                    Biblioteca.consultar_libros()
                elif opcion_dos == 2:
                    Biblioteca.consultar_libro()
            elif opcion == 8:
                try:
                    opncion_dos = int(input("1. Obtener todos los usuarios \n2. Obtener un usuario \n"))
                except:
                    print("📛 El valor esperado era un número 📛")
                    opcion_dos = None
                if opncion_dos == 1:
                    Biblioteca.consultar_usuarios()
                elif opncion_dos == 2:
                    Biblioteca.consultar_usuario()
            elif opcion == 9:
                try:
                    opcion_dos = int(input("1. Prestamos usuarios \n2. Prestamos libros \n"))
                except:
                    print("📛 El valor esperado era un número 📛")
                    opcion_dos = None
                if opcion_dos == 1:
                    Biblioteca.consultar_prestamos_usuarios()
                elif opcion_dos == 2:
                    Biblioteca.consultar_prestamo_libros()
            elif opcion == 10:
                salir = False
        