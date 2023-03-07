def erase_to(string_function, number_function):
      string_function = string_function[number_function::]
      return string_function

print("Escribe una función que dado un string y un número entero n, elimine los caracteres del "
      "string empezando del índice 0 hasta el n.\n")
string = str(input("Escriba una cadena de caracteres: "))
number = int(input("Escriba un numero: "))
print(erase_to(string, number))
