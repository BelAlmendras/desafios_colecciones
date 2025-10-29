biblioteca =[]

biblioteca.append({"nombre": "El Principito", "autor": "Antoine de Saint-Exupery", "anio": "1943"})
biblioteca.append({"nombre": "Cien años de soledad", "autor": "Gabriel Garcia Marquez", "anio": "1967"})
biblioteca.append({"nombre": "1984", "autor": "George Orwell", "anio": "1949"})

def mostrar_libros(biblioteca):
    print("=== Mi Biblioteca ===")
    for i, mi_biblioteca in enumerate(biblioteca, start=1):
        print(f"{i}. {mi_biblioteca['nombre']} - {mi_biblioteca['autor']} - {mi_biblioteca['anio']}")


mostrar_libros(biblioteca)
opcion = input("Desea agregar un libro? (s/n): ").lower()

while opcion == "s" or opcion == "si":
    if opcion != "s" and opcion != "si":
        print("===================================")
        print("Gracias por utilizar mi biblioteca.")
        print("===================================")
        break
    try:
        mi_biblioteca = {
            "nombre": input("Ingrese el nombre del libro: "),
            "autor": input("Ingrese el autor del libro: "),
            "anio": int(input("Ingrese el año del libro: ")),
            
        }
        biblioteca.append(mi_biblioteca)
        print("LIBRO GUARDADO CON EXITO")
    except ValueError:
        print("Error: El año debe ser un número entero.")

    opcion = input("Desea agregar otro libro? (s/n): ").lower()
    if opcion != "s" and opcion != "si":
        print("===================================")
        print("Gracias por utilizar mi biblioteca.")
        print("===================================")
        break 
        
mostrar_libros(biblioteca)

categorias = ('Ficcion', 'Historia', 'Ciencia Ficcion')
print("\nCategorias diposibles:", categorias)