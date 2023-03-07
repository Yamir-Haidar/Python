print(" Escribe un programa que itere sobre los 10 primeros números enteros y en cada iteración, "
      "imprima la suma del numero actual y el anterior.\n")
previous = 0
for i in range(10):
    current = i + 1
    total = previous + current
    print(f"The sum of {previous} and {current} is {total}")
    previous = current
