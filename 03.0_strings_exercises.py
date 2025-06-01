
# 1. Declara una variable text con la frase "Aprendiendo Python" y luego imprime la longitud de la cadena usando len().

text = "Aprendiendo Python"
print(len(text))


# 2. Concatena dos cadenas: "Hola" y "Python", y muestra el resultado en una sola línea.

print('Hola', 'Python') ### Concatena dos cadenas e imprime un espacio entre ellas.


# 3. Crea una cadena que incluya un salto de lí­nea, y luego imprí­mela para ver el resultado.

my_new_line_string = "Este es un string \n con salto de línea"
print(my_new_line_string) # \n es un salto de línea


# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.

name, surname, age = "Armando", "Rodriguez", 25
print(f"Mi nombre es {name} {surname} y mi edad es {age} años") # Formateo de cadenas con f-strings, si queremos imprimir datos tal cual.


# 5. Desempaqueta los caracteres de la palabra "Python" en variables separadas y luego imprí­melos uno por uno.

language = "Python"
a, b, c, d, e, f = language
print(a) # Imprime la letra P
print(b) # Imprime la letra y
print(c) # Imprime la letra t
print(d) # Imprime la letra h
print(e) # Imprime la letra o
print(f) # Imprime la letra n

### El desempaquetado de caracteres permite asignar cada letra a una variable diferente, lo que facilita su manipulación y uso posterior.

# Usa slicing para extraer los caracteres de la palabra "Python" desde la posición 1 hasta la 4 (sin incluir la 4) y muéstralo.

language_slice = language[1:4] # [1:4] significa que queremos los caracteres desde la posición 1 hasta la posición 4 (sin incluir la posición 4)
print(language_slice) # Imprime la subcandena "yth"

### El slicing permite extraer una parte de la cadena original, lo que es útil para obtener subcadenas específicas.


# 6. Extrae un "slice" de la palabra "Programación" para obtener los caracteres desde la posición 3 hasta la 7.

language_slice = "Programación"[3:7] # [3:7] significa que queremos los caracteres desde la posición 3 hasta la posición 7 (sin incluir la posición 7)
print(language_slice) # Imprime la subcadena "gram"


# 7. Invierte la cadena "Python" usando slicing y muestra el resultado.

language_slice = language[::-1] ### [::-1] significa que queremos invertir la cadena
print(language_slice) # Imprime la cadena invertida "nohtyP"


# 8. Convierte la cadena "aprendiendo python" en mayúsculas usando el método adecuado e imprí­mela.

my_string = "aprendiendo python"
my_string = my_string.upper() # La función upper() convierte la cadena a mayúsculas
print(my_string)


# 9. Cuenta cuántas veces aparece la letra "n" en la cadena "Programación en Python".

my_string = "Programación en Python"
print(my_string.count("n")) # La función count() cuenta cuántas veces aparece un carácter en la cadena


# 10. Verifica si la cadena "12345" es numérica usando el método adecuado e imprime el resultado.

my_string = "12345"
print(my_string.isnumeric()) # La función isnumeric() verifica si la cadena es numérica, te imprime el resultado con un booleano True o False.


# 11. Reemplaza la letra "o" por "0" en la cadena "Hola Mundo" y muestra el resultado.

my_string = "Hola Mundo"
my_string = my_string.replace("o", "0") # La función replace() reemplaza un carácter por otro en la cadena
print(my_string)

# 12. Encuentra la posición de la letra "P" en la cadena "Python" usando el método adecuado
my_string = "Python"
print(my_string.find("P")) # La función find() encuentra la posición de un carácter en la cadena
print(my_string.index("P")) # La función index() encuentra la posición de un carácter en la cadena

# 13. Verifica si la cadena "Python" contiene solo letras usando el método adecuado e imprime el resultado.
my_string = "Python"
print(my_string.isalpha()) # La función isalpha() verifica si la cadena contiene solo letras, te imprime el resultado con un booleano True o False.




