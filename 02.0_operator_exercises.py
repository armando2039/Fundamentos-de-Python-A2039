
# 1. Realiza las siguientes operaciones aritméticas:
# A)	Suma: 15 + 25
# B)	Resta: 50 - 22
# C)	Multiplicación: 8 * 7
# D)	División: 100 / 20

print(15 + 25) # Suma
print(50 - 22) # Resta
print(8 * 7) # Multiplicación
print(100 / 20) # División
print(100 // 20) # División entera, devuelve la parte entera de la división.
print(100 % 20) # esto es el resto de la división, 100 entre 20.
### El resto de la división se refiere a la cantidad que sobra después de dividir un número entre otro. Por ejemplo, si dividimos 10 entre 3, el resultado es 3 con un resto de 1, porque 3 cabe 3 veces en 10 y sobra 1.
# En Python, el operador % se utiliza para calcular el resto de una división. Por ejemplo, 10 % 3 devuelve 1, que es el resto de la división de 10 entre 3.
# El operador // se utiliza para realizar una división entera, que devuelve la parte entera de la división sin el resto. Por ejemplo, 10 // 3 devuelve 3, que es la parte entera de la división de 10 entre 3.
# El operador ** se utiliza para realizar una potencia. Por ejemplo, 3 ** 3 devuelve 27, que es 3 elevado a la 3.
print(3 ** 3) # Potencia, 3 elevado a la 3.


# 2. Calcula el resto de la división de 37 entre 5 y almacénalo en una variable remainder. Luego imprímelo.

remainder = 37 % 5
print(remainder) # Imprime el resto de la vivión de 37 entre 5.


# 3. Convierte el número 7 en una cadena de texto y concaténalo con la frase "es mi número favorito". Imprime el resultado.
favorite_number = str(7) + " es mi número favorito"
print(favorite_number) # Imprime la cadena de texto que contiene el número 7 y la frase "es mi número favorito".


# 4. Repite la palabra "Python" 10 veces usando el operador de multiplicación para cadenas y luego imprí­mela.
repeated_world = "Python " * 10
print(repeated_world) # Imprime la palabra " Python" repetida 10 veces.


# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.
a = 12
b = 8
resultado = a > b
print(resultado) # Imprime el resultado de la comparación entre a y b.


# 6. Compara dos cadenas de texto ("apple" y "banana") usando los operadores > y < y explica cuál tiene mayor orden alfabético.
cadena_1 = "apple"
cadena_2 = "banana"
print(cadena_1 > cadena_2)
print(cadena_1 < cadena_2)
# La cadena "banana" tiene un mayor orden alfabético que "apple" porque la letra 'b' en "banana" es mayor que la letra 'a' en "apple" según el orden alfabético.


# 7. Realiza una comparación lógica usando and para verificar si el número 10 es mayor que 5 y menor que 20. Imprime el resultado.
number = 10
logical_result = number > 5 and number < 20
print(logical_result) # Imprime el resultado de la comparación lógica entre 10, 5 y 20.


# 8. Usa el operador or para verificar si el número 7 es menor que 3 o mayor que 5. Imprime el resultado.
print(7 < 3 or 7 > 5) # Imprime le resultado de la comparación lógica entre 7, 3 y 5.



# 9. Aplica el operador not para invertir el resultado de la comparación 15 > 20. ¿Cuál es el resultado?
print(not (15 > 20)) # Imprime el resultado de la comparación lógica entre 15 y 20, invertido por le operador not.


# 10. Combina operadores aritméticos y lógicos: Verifica si el número resultante de la expresión (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.
result_10 = (5 * 3) + 2
print(result_10 > 10 and result_10 < 20) # Imprime el resultado de la comparación lógica entre el resultado de la expresión y los números 10 y 20.


print(10 % 3)
print(4 **2)

print( 4 >= 4 and 2 < 5) # Donde and es un operador lógico que devuelve True si ambas condiciones son verdaderas.

print( 3 > 4 or 2 > 3) # Donde or es un operador lógico que devuelve True si al menos una de de las condiciones es verdadera.

# El operador or devuelve True si al menos una de las condiciones es verdadera.
# El operador not invierte el resultado de una expresión booleana, es decir, devuelve True si la expresión es False y viceversa.
# 11. Usa el operador de identidad is para verificar si una variable es igual a otra. Crea dos variables con el mismo valor y verifica si son idénticas.

### Los operadores de lógica funcionan con la tabla de verdad de la Algebra Boolena.


# orden gerarquico de operaciones:
# Orden de operaciones:
# 1. Paréntesis
# 2. Potencias
# 3. Multiplicación y división
# 4. Suma y resta
# 5. Comparaciones
# 6. Lógicos
# 7. Asignación
# 8. Identidad
# 9. Membresía
# 10. Identidad
# 11. Bitwise
# 12. Desplazamiento
# 13. Aritméticos

# == significa igual, != significa diferente, > significa mayor que, < significa menor que, >= significa mayor o igual que, <= significa menor o igual que.
