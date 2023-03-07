import random

print("Escribir una función que retorne True si el primero y el último número de la lista son "
      "iguales. Si los números son diferentes retorna False.\n")
numbers = [random.randint(0, 8) for _ in range(10)]
print(numbers[0] == numbers[len(numbers) - 1])


