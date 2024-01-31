"""Usando las propiedades de cadenas o strings"""
"""
Requisitos:
- Ingresar nombre y apellido por consola (cada valor tiene que estar en una variable distinta
- concatenar ambos valores en una sola variable
- Obetern el tamaño de tu nombre completo
- IMprimir en mayusculas
Indicar mediante condicionales si el tamaño del nombre es mayor o NO al del apellido paterno

"""

nombre = input("Ingresar su nombre: ")
apellido = input("Ingresar su apellido: ")
completo = nombre + " " + apellido

print("El tamaño del nombre completo es: {}".format(len(completo)))
print(completo.upper())

if len(nombre) >= len(apellido):
    print("El tamaño del nombre es mayor al del apellido")
else:
    print("El tamaño del nombre es menor al del apellido")