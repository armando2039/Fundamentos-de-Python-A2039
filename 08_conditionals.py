### Conditionals ###

# Conditionals are used to execute a block of code based on a condition.
# Los condicionales se utilizan para ejecutar un bloque de código según una condición.
# If the condition is True, the block of code is executed.

# -- Si se cumple una condición yo ejecuto lo que te me digas que esta dentro de la condicional.-- 
# un condicional es una estructura de control que permite evaluar si una expresión es verdadera o falsa

# Se escribe una condicional en python utilizando la palabra reservada if, seguida de una expresión booleana y dos puntos.
# La expresión booleana puede ser cualquier expresión que devuelva un valor verdadero o falso.

# La estructura básica de un condicional es la siguiente:
# if <expresión booleana>:
#     <bloque de código>
# else:
#     <bloque de código>
# if <expresión booleana>:
#     <bloque de código>   

# elif <expresión booleana>:
#     <bloque de código>

# else:
#     <bloque de código>

# if <expresión booleana>:
#     <bloque de código>


my_condition = True
# if the condition is True, the block of code is executed.
# si la condición es verdadera, se ejecuta el bloque de código.

if my_condition:
    print("se ejecuta la condición if")


print("la ejecución continua")

# if the condition is False, the block of code is not executed.
# si la condición es falsa, no se ejecuta el bloque de código.

my_condition = 5 * 2 # no es ni tru ni false simplemente es algo con valor y lo por valido.

if my_condition == 10: # en valor buleano es true por eso se ejecuta el bloque de código.
    print("se ejecuta la condición del segundo if")

print("la ejecución continua")

# si no se cumple la condición entonces haz esto

if my_condition > 10 and my_condition < 20:
    print("es mayor que 10 y menor que 20")
elif my_condition == 25: # si se cumple la condición del elif entonces se ejecuta el bloque de código.
    # elif es una abreviatura de else if
    # se utiliza para evaluar una segunda condición si la primera no se cumple.
    # si la condición del if no se cumple, se evalúa la condición del elif.

    print("es igual a 25")
else: # si no se cumple el if ni el elif entonces se ejecuta el else.
    print("es menor o igual que 10 o mayor o igual que 20")

print("la ejecución continua")

my_string = ""
if not my_string: # not es un operador lógico que invierte el valor de una expresión booleana.
    # si la cadena de texto es vacía, se ejecuta el bloque de código.
    # if my_string == "":
    #     print("mi cadena de texto esta vacía")
    # if my_string != "":
    #     print("mi cadena de texto no esta vacía")
    # if my_string == False:
    #     print("mi cadena de texto es falsa")
    # if my_string == True:
    #     print("mi cadena de texto es verdadera")
    # if my_string == None:
    #     print("mi cadena de texto es nula")
    # if my_string == 0:
    #     print("mi cadena de texto es cero")
    print("mi cadena de texto esta vacía")



#










