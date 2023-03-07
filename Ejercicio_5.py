print("Dada una lista imprima los números que son divisibles por 5\n")
numbers = [1, 5, 23, 50, 10, 23]
numbers_2 = []
for n in numbers:
    if n % 5 == 0:
        numbers_2.append(n)
print(numbers_2)
