"""Usando las propiedades de cadenas o strings"""
"""Metodo de string"""

cadena = "Conexion a base de datos con Python"
cadena_2 = cadena.replace(cadena[0:6], "pppppp")
print("Cadena con reemplazos, tiene el siguiente valor actualizado: {}".format(cadena_2))

"""Eliminando espacios en blanco de mi cadena (después)"""
cadena_3 = "Conexion a base de datos con Python    "
cadena_4 = cadena_3.rstrip()
print(cadena_3)
print("Mi cadena actualizada sin espacios en blanco es la siguiente: {}".format(cadena_4))

cadena_5 = "           Conexion a base de datos con Python"
cadena_6 = cadena_5.lstrip()
print(cadena_5)
print("Mi cadena actualizada sin espacios en blanco es la siguiente: {}".format(cadena_6))