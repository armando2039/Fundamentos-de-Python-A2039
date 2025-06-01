# Variables


# Buena práctica de programación es escribir el nombre de la variable como formato snake_case, es decir en minusculas y con guiones bajos entre palabras.
# 
# # En Python, las variables son contenedores que almacenan datos. Puedes pensar en ellas como etiquetas que le pones a un valor para poder referenciarlo más tarde.
#  


my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable) # Convertimos un entero a string.
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


my_bool_variable = False
print(my_bool_variable)


# Contacatenación de variables en un print, hay diferentes formas una de ellas es poner una coma entre las variables.
print(type(print(my_string_variable, my_int_to_str_variable, my_bool_variable)))
print("Este es el valor de:", my_bool_variable)


# Algunas funciones del sistema.  

print(len(my_string_variable)) # len() devuelve la longitud de una cadena, es decir, el número de caracteres que contiene.

# Variables de una sola linea ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Armando", "Borja", "Armand1to", 33
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

name = input("¿Cuál es tu nombre? ")   # input es una función que permite al usuario introducir un valor por teclado (por consola)
age = input('¿Cuantos años tienes? ') # input se utiliza para crear aplicaciones que trabajan directamente en la terminal ó si estamos creando scripts que se ejecuten en la terminal. 
                                      # input su proposito es
print(name)
print(age)

# Cabiamos su tipo de dato
name = 33
age = "Armando"
print(name)
print(age)

# Forzamos el tipo de dato
address: str = "Mi dirección" # Aqui estamos tipando el programa, es decir, le estamos diciendo que la variable address que queremos que sea de tipo string.
address = 32
print(type(address))







