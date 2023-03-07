print("Dadas dos listas de números, escribe un programa que cree una nueva lista que contenga "
      "los números impares de la primera lista y los números impares de la segunda lista.")
list_1 = [0, 1, 2, 3, 4, 575]
print("La primera lista es: ", list_1)
list_2 = [6, 7, 8, 9, 23, 13]
print("La segunda lista es: ", list_2)
list_3 = []
for i in list_1 + list_2:
    if i % 2 != 0:
        list_3.append(i)
print(list_3)
