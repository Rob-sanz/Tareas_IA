##Igresar estudiantes y sus notas y almacenarlos en un disccionario, al fnal mostrar datos ingrados

seguir = True
contador = 1
estudiantes = {}

while seguir:
    print(f"Ingrese estudiante N.{contador}")
    nombre = input("Nombre: ")
    nota = input("Nota: ")

    estudiantes["Nombre"] = nombre
    estudiantes["Nota"] = nota

    estudiantes[f"Estudiante {contador}"] = {
        "Nombre": nombre,
        "Nota": nota
    }

    respuesta = input("Quieres agregar otro estudiante Y/N?")
    while respuesta != "N" and respuesta != "Y" and respuesta != "n" and respuesta != "y":
        respuesta = input("Quieres agregar otro estudiante Y/N?")

    if respuesta == "N" or respuesta == "n":
        seguir = False
    elif respuesta == "Y" or respuesta == "y":
        contador += 1

print("Estudiantes ingresados:")
for clave, valor in estudiantes.items():
    print(f"{clave}: {valor}")