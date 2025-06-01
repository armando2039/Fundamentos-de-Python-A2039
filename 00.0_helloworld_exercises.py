### 00.0 Exercises: Hello World

# 1. Imprime "¡Hola Mundo!" por consola.

print("¡Hola Mundo¡") # Esto imprime "¡Hola Mundo!" en la consola.

# 2. Escribe un comentario de una sola lí­nea explicando qué hace el código del Ejercicio 1.

# Este código imprime '¡Hola Mundo!' en la consola. Este es el primer programa que se suele escribir al aprender un un nuevo lenguaje de programación.

# 3. Imprime tu nombre y edad en la misma lí­nea utilizando la función print.

print("Mi nombre es Armando y tengo 35 años")

# 4. Usa la función type() para imprimir el tipo de dato de una cadena de texto, un número entero y un número decimal.

print(type('!Hola python¡'))
print(type(35))
print(type(35.5))

# 5. Escribe un comentario en varias lí­neas explicando qué son los tipos de datos en Python.

"""
Los tipos de datos en python son una forma de clasificar los diferentes tipos
de datos que se pueden almacenar en una variable.

Python tiene varios tipos de datos incorporados, como:
- int: para números enteros
- float: para números decimales
- str: para cadenas de texto
- bool: para valores booleanos (True ó false)
- list: para listas de elementos
- tuple: para tuplas de elementos
- set: para conjuntos de elementos
- dict: para diccionarios de elementos
- NoneType: patra valores nulos
- function: para funciones
- type: para tipos de datos
- complex: para números complejos

Los tipos de datos son importantes porque determinan cómo se pueden manipular y operar los datos dentro de un programa. 
Cada tipo de dato tiene sus propias propiedades y métodos que se pueden utilizar para trabajar con ellos.
Por ejemplo, los números enteros y flotantes se pueden sumar, restar, multiplicar y dividir,
mientras que las cadenas de texto se pueden concatenar y dividir.

Los tipos de datos también son importantes para la memoría y el rendimiento de un programa.
Algunos tipos de datos ocupan más espacio en memoria que otros, y algunos son más rápidos de procesar.
Por ejemplo, las listas y los diccionarios son más lentos de procesar que los números enteros y flotantes.

Los tipos de datos también son importantes para la legibilidad y el mantenimiento del código.
Al utilizar tipos de datos adecuados, el código se vuelve más fácil de leer y entender.
Esto es especialmente importante en proyectos grandes y complejos, donde muchas perosnas trabajan en el mismo código.

Además, los tipos de datos son importantes para la depuración y el manejo de errores.
Si se utilizan tipos de datos incorrectos, pueden producirse errores en tiempo de ejecución que son dificiles de detectar y corregir.
Por último, los tipos de datos son importantes para la interoperabilidad entre diferentes lenguajes de programación.
Algunos lenguajes de programación tienen tipos de datos diferentes o no tienen tipos de datos en absoluto.
Esto puede dificultar la comunicación entre diferentes lenguajes de programación y hacer que sea más difícil trabajar con bibliotecas y frameworks de terceros.
Por lo tanto, es importante comprender los tipos de datos en Python y cómo se utilizan en la programación.

Los tipos de datos son una parte fundamental de la programación y son esenciales para
comprender cómo funciona un lenguaje de programación.
"""

# 6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".

print("Hola" + " " + "Mundo") # Esto imprime "Hola Mundo" concatenado, en la consola.

# 7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma lí­nea.

nombre = "Armando" 
edad = 35
print("Mi nombre es " + nombre + " y tengo " + str(edad) + " años") # Esto imprime "Mi nombre es Armando y tengo 35 años" en la consola.

# 8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.
nombre_usuario = input("¿Cuál es tu nombre? ") # Solicita al usuario su nombre
print("Hola " + nombre_usuario + "!") # Imprime un saludo con el nombre del usuario

# 8.1 Usa la función input() para solicitar al usuario su edad y luego imprímela.
edad_usuario = input("¿Cuál es tu edad? ") # Solicita al usuario su edad
print("Tienes " + edad_usuario + " años") # Imprime la edad del ususario

# 8.2 Escribe un programa que solicite al usuario su nombre y edad, y luego imprima ambos en la misma línea.
# nombre_usuario = input("¿Cuál es tu nombre? ") # Solicitra al usuario su nombre
# edad_usuario = input("¿Cuál es tu edad? ") # Solicita al usuario su edad
""" 'input' es una función que permite al usuario ingresar datos por teclado
 ### input() devuelve una cadena de texto, por lo que es necesario convertir la edad a un número en caso de que se necesite realizar operaciones matemáticas con ella.
 En este caso, no es necesario convertir la edad a un número, ya que solo se va a imprimir.
 la función input() se utiliza para solicitar al usuario que ingrese un valor 
 y devuelve ese valor como una cadena de texto
 de esta manera, se puede almacenar el valor ingresado por el usuario en una variable
 y luego utilizarlo en el programa.

# La función input() se utiliza para solicitar al usuario que ingrese un valor
# y devuelve ese valor como una cadena de texto.
# En este caso, se solicita al usuario que ingrese su nombre y su edad.
# Luego, se imprime un saludo que incluye el nombre y la edad del usuario.
"""

print("Hola " + nombre_usuario + "! Tienes " + edad_usuario + " años") # Imprime un saludo con el nombre y la edad del usuario


# 9. Usa print() para mostrar el resultado de la suma de dos números enteros y el tipo de dato resultante.

print(10 + 5) # Esto imprime el resultado de la suma de 10 y 5, que es 15.
print(type(10 + 5)) # Esto imprime el tipo de dato del resultado de la suma, que es un entero (int).


# 9.1 Usa print() para mostrar el resultado de la suma de un número entero y un número decimal, y el tipo de dato resultante.
print(10 + 5.5) # Esto imprime el resultado de la suma de 10 y 5.5, que es 15.5.
print(type(10 + 5.5)) # Esto imprime el tipo de dato del resultado de la suma, que es un número decimal (float).
# 9.2 Usa print() para mostrar el resultado de la suma de un número entero y una cadena de texto, y el tipo de dato resultante.
# print(10 + "5") # Esto generará un error porque no se puede sumar un número entero y una cadena de texto.
# 9.3 Usa print() para mostrar el resultado de la suma de un número entero y un número complejo, y el tipo de dato resultante.
print(10 + 5j) # Esto imprime el resultado de la suma de 10 y 5j, que es un número complejo (10 + 5j).
print(type(10 + 5j)) # Esto imprime el tipo de dato del resultado de la suma, que es un número complejo (complex).
# 9.4 Usa print() para mostrar el resultado de la suma de un número entero y un booleano, y el tipo de dato resultante.
print(10 + True) # Esto imprime el resultado de la suma de 10 y True, que es 11 (True se convierte en 1).
print(type(10 + True)) # Esto imprime el tipo de dato del resultado de la suma, que es un entero (int).
# 9.5 Usa print() para mostrar el resultado de la suma de un número entero y None, y el tipo de dato resultante.
# print(10 + None) # Esto generará un error porque no se puede sumar un número entero y None.
print(10 + False)
print(type(10 + False))


# 10. Comenta el código del Ejercicio 9, y explica qué hace cada lí­nea usando comentarios de una sola lí­nea.
# Este codigo imprime el resultado de la suma de dos números enteros y el tipo de dato resultante.
# print(10 + 5) # Esto imrpime el resultado de la suma de 10 y 5, que es 15.
# print(type(10 + 5)) # Esto imprime el tipo de dato del resulatdo de la suma, que es una entero (int).

