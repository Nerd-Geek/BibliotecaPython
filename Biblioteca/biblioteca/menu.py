from .biblioteca import Biblioteca

class Menu:
    def main():
        salir = True

        while(salir):
            print("1- Alta de socio β")
            print("2- Baja de socio β")
            print("3- Alta de libro β")
            print("4- Baja de libro β")
            print("5- Prestar libro π€")
            print("6- Devolver libro π")
            print("7- Consultar libros ππ")
            print("8- Consultar usuarios ππ")
            print("9- Consultar prestamos ππ€")
            print("10- Salir π")
            try:
                opcion = int(input("ΒΏQue opciΓ³n escoges?\n"))
            except ValueError:
                print("π El valor esperado era un nΓΊmero π")
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
                    print("π El valor esperado era un nΓΊmero π")
                    opcion_dos = None
                if opcion_dos == 1:
                    Biblioteca.consultar_libros()
                elif opcion_dos == 2:
                    Biblioteca.consultar_libro()
            elif opcion == 8:
                try:
                    opncion_dos = int(input("1. Obtener todos los usuarios \n2. Obtener un usuario \n"))
                except:
                    print("π El valor esperado era un nΓΊmero π")
                    opcion_dos = None
                if opncion_dos == 1:
                    Biblioteca.consultar_usuarios()
                elif opncion_dos == 2:
                    Biblioteca.consultar_usuario()
            elif opcion == 9:
                try:
                    opcion_dos = int(input("1. Prestamos usuarios \n2. Prestamos libros \n"))
                except:
                    print("π El valor esperado era un nΓΊmero π")
                    opcion_dos = None
                if opcion_dos == 1:
                    Biblioteca.consultar_prestamos_usuarios()
                elif opcion_dos == 2:
                    Biblioteca.consultar_prestamo_libros()
            elif opcion == 10:
                salir = False
        