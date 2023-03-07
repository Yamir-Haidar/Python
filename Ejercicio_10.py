print("Escribe un programa que dado un número devuelva cada uno de sus caracteres por "
      "separado en orden inverso al número.\n"
      "Ejemplo: Dado el número 7536, la salida tiene que ser “6 3 5 7”.")
number = int(input("Digite el numero: "))
str_number = str(number)
print(" ".join(str_number[::-1]))
