"""Uso del flujo condicional 'while'"""

numero = int(input("Cuantos saludos deseas enviar:"))

while numero < 8:
    print(numero)
    numero = numero + 1

print("Llegó al final del bucle")