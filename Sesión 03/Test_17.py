"""Usando las propiedades de cadenas o strings"""
"""Metodo de string"""

cadena = "Python para la predicción de fraudes"

cadena_sin_espacios = cadena.split()
print("Cadena separada por espacios en blanco dentro del string: {}".format(cadena_sin_espacios))

for palabra in cadena_sin_espacios:
    print(palabra)