"""Listas en Python"""

"""Listas del(): Elimina un valor indicando el indice del valor en la lista"""

paises=[]
paises.append("Perú")
paises.append("Brasil")
paises.append("Canadá")
paises.append("España")
paises.append("Chile")

print("Los valores de mi lista de paises es: {}".format(paises))

del paises[2]
print("Mi lista actualizada tiene los siguientes valores: {}".format(paises))