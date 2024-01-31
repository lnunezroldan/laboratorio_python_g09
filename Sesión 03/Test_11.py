"""Uso del flujo condicional 'if'"""
"""if ternario"""


"""
Requisitos:
- Ingresar el sueldo de un empleado
- Si el sueldo es mayor de 3000, imprimir 'Su sueldo no tiene bonificacion'
- Caso contrario, 'Su sueldo tiene bonificacion este año'"""

sueldo = int(input("Ingresar su sueldo:"))

final = "Su sueldo no tiene bonificacion" if sueldo > 3000 else "Su sueldo tiene bonificacion"
print(final)