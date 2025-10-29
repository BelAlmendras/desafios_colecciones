contactos =[]

contactos.append({"nombre": "Ana", "telefono": 987654321, "correo": "ana@mail.com"})
contactos.append({"nombre": "Luis", "telefono": 912345678, "correo": "luis@mail.com"})
contactos.append({"nombre": "Sofía", "telefono": 998877665, "correo": "sofia@mail.com"})

def mostrar_contactos(contactos):
    print("=== Mis Contactos ===")
    for i, contacto in enumerate(contactos, start=1):
        print(f"{i}. {contacto['nombre']} - {contacto['telefono']} -  {contacto['correo']} ")


mostrar_contactos(contactos)
opcion = input("Desea agregar un contacto? (s/n): ").lower()

while opcion == "s" or opcion == "si":
    if opcion != "s" and opcion != "si":
        print("Gracias por utilizar la agenda de contactos.")
        break
    try:
        contacto = {
            "nombre": input("Ingrese el nombre del contacto: "),
            "telefono": int(input("Ingrese el número de teléfono del contacto: ")),
            "correo": input("Ingrese el correo electrónico del contacto: "),
            
        }
        contactos.append(contacto)
        print("CONTACTO GUARDADO CON EXITO")
    except ValueError:
        print("Error: El número de teléfono debe ser un número entero.")

    opcion = input("Desea agregar otro contacto? (s/n): ").lower()
    if opcion != "s" and opcion != "si":
        print("Gracias por utilizar la agenda de contactos.")
        break 
        
mostrar_contactos(contactos)

tipo_contacto = ('amigos', 'familia', 'trabajo')
print("\nTipos de contacto:", tipo_contacto)