### Exception Handling ##

# Manejo de errores, 


# 'print(5 + "5")' # SyntaxError: invalid syntax
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

numberOne = 5
numberTwo = 1

numberTwo = "1"

# 'print(numberOne + numberTwo)' # python no se capaz de sumar un 'entero' con un 'string'.

# Para evitar que el programa se detenga, se puede usar un bloque try/except
# El bloque try contiene el código que puede generar una excepción.
# El bloque except contiene el código que se ejecuta si se produce una excepción.
# El bloque finally contiene el código que se ejecuta siempre, independientemente de si se produce una excepción o no.

 #if type(numberTwo) == int:
    #print(numberOne + numberTwo)
#else:
    #print('No se cumplio la condición')


try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
# Se puede usar un bloque try/except para manejar excepciones en Python.
except:
    print('Si se ha producido un error')
else:
    # El bloque else se ejecuta si no se produce ninguna excepción.
    print('La ejecución continúa sin errores')
finally:
    # El bloque finally se ejecuta siempre, independientemente de si se produce una excepción o no.
    print('La ejecución continúa siempre')


# Excepciones po tipo.
# # Se pueden manejar excepciones específicas utilizando el bloque except.

try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except ValueError:
    print('Se ha producido un error de valor')
except TypeError:
    print('Se ha producido un error de tipado')

# Se pueden manejar múltiples excepciones utilizando una tupla.
try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except (ValueError, TypeError):
    print('Se ha producido un error de valor o de tipado')
    

# Captura de la información de la excepción.

try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except ValueError as error: # un objeto error que nos da información, genera una variable que captura la info de la excepción.
    print(error)
 # Nos da una trasa del error, nos genera información de lo que ha producido el error.
except TypeError as error:
    print(error)
# Se puede capturar la excepción y generar un mensaje personalizado.
except TypeError as error:
    print('Se ha producido un error de tipado')
    print(error)

    # Donde 'error' es el nombre de una variable que nosostros capturamos.
    # es el nombre que le estamos dando a la variable que contiene la información del error.



try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except ValueError as error: # un objeto error que nos da información, genera una variable que captura la info de la excepción.
    print(error)
 # Nos da una trasa del error, nos genera información de lo que ha producido el error.
except Exception as my_random_error_name:
    print(my_random_error_name)




