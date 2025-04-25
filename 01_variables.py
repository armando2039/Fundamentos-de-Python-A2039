# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


my_bool_variable = False
print(my_bool_variable)


# Contacatenación de variables en un print
print(type(print(my_string_variable, my_int_to_str_variable, my_bool_variable)))
print("Este es el valor de:", my_bool_variable)


# Algunas funciones del sistema.  

print(len(my_string_variable))

# Variables de una sola linea ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Armando", "Borja", "Armand1to", 33
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

name = input("¿Cuál es tu nombre? ")   # input es una función que permite al usuario introducir un valor por teclado (por consola)
age = input('¿Cuantos años tienes? ')

print(name)
print(age)

# Cabiamos su tipo de dato
name = 33
age = "Armando"
print(name)
print(age)

# Forzamos el tipo de dato
address: str = "Mi dirección"
address = 32
print(type(address))







