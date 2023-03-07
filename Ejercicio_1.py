print("Dados dos numeros enteros retorna su producto solo si es mayor que 1000, en caso "
      "contrario retorna la suma.\n")
number_one = int(input("Digite el primer numero: "))
number_two = int(input("Digite el segundo numero: "))
multiplication = number_one * number_two
total = number_one + number_two
if multiplication > 1000:
    print("La multiplicacion es mayor que 1000. Su multiplicacion es: " + str(multiplication))
elif multiplication < 1000:
    print("La multiplicacion es menor que 1000. Su suma es: " + str(total))
else:
    print("La multiplicacion es igual a 1000. Su suma es: " + str(total))
