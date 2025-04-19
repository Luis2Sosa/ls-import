def nosotros():
    return "Somos una compañia que esta especializada en ofrecer el mejor servicio del pais"
def horario():
    return "Nuestro horario es de 8 am a 5 pm 'Dias feriados no laboramos'"
def contacto():
    return "Nuestro numero de contacto es '849-357-7777'"
def soporte():
    return "Tenemos soporte las 24 horas del dia"

def func(funcion):
    return funcion()

opciones = {
    "nosotros": nosotros,
    "horario": horario,
    "contacto": contacto,
    "soporte": soporte
}

print("BIENVENIDOS A 'LS IMPORT")
print("Los mejores en servicios en todo el pais\n")

while True:
    print("Menu\n")
    print("Nosotros")
    print("Horario")
    print("Contacto")
    print("Soporte")
    print("Salir\n")
    
    
    opcion = input("Buenas! Que desea saber?\n").lower()
    if opcion == "salir":
        print("\nGracias por utilizar nuestro sistema, cualquier duda, no dudes en escribirnos.")
        break
    detalles = opciones.get(opcion, lambda: "Opcion no valida.\n")
    print(detalles())
    
print("Este cambio es una prueba de Git modificando un archivo existente")
    