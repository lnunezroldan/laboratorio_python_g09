"""
Requisitos:
-
"""
var1 = input("Ingrese su nombre: ")
var2 = input("Ingrese su apellido: ")
var3 = input("Ingrese su distrito de residencia: ")
var4 = input("Ingrese su sueldo: ")

nombre, apellido, distrito, sueldo, bono = [var1, var2, var3, var4, int(var4)*3*0.9]


print("{} {} recibirá {} soles de bono a fin de año".format(nombre,apellido,bono))
