lista_1=[]
lista_2=[]

lista_1.append("Luis")
lista_1.append(33)
lista_1.append("Ingeniero de Minas")
lista_2.append("Adrian")
lista_2.append(30)
lista_2.append("Geologo")

sumalis= lista_1 + lista_2

print("La suma de las listas es:{}". format(sumalis))

sumalis.reverse()
print("La lista actualizada sería:{}". format(sumalis))

del sumalis[1]
del sumalis[3]
print("La lista actualizada sería:{}". format(sumalis))