"""Listas en Python"""

"""Listas count(): Cantidad de veces que aparece el elemento que se repite en una lista"""

var_1= ["Python", "java", "PHP", "Ruby", "Javascript", "Typescript"]

var_1.append("Python")
var_1.append("Python")
var_1.append("Python")
var_1.append("NodeJS")

print("Mi lista actualizada es: {}".format(var_1))
print("La cantidad de veces que se repite 'Python' es: {}".format(var_1.count("Python")))
print("La cantidad de veces que se repite 'java' es: {}".format(var_1.count("java")))