print("Escribe un programa que dado un string escrito por consola, muestre los caracteres que "
      "están presentes en un índice impar.\n")
text = input("Inserte una cadena de caracteres: ")
odd_chars = text[1::2]
print("Los caracteres en posiciones impares son:", odd_chars)
