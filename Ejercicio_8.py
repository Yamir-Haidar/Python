def es_palindromo(number_function):
    number_str = str(number_function)
    return number_str == number_str[::-1]


print("– Escriba una función que verifique si un número es palíndromo. Un número es palíndromo "
      "cuando se lee de igual forma en reverso. Ejemplo: 121")
number = int(input("Digite el numero: "))
if es_palindromo(number):
    print("El numero", number, "es palindromo")
else:
    print("El numero", number, "no es palindromo")
