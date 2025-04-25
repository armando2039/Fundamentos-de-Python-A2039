### Strings ###

my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string)) # vamos allar la longitud de la cadena
print(len(my_other_string)) # se calcula la longitud del contenido de la variable

print(my_string + " " + my_other_string) # concatenamos las dos cadenas

my_new_line_string = "Este es un string \n con salto de linea"
print(my_new_line_string) # \n es un salto de linea

my_tab_string = "tEste es un string con tabulación"
print(my_tab_string) # \t es un tabulador

my_scape_string = "\\tEste es un string \\n escapado"
print(my_scape_string) # \\ es un caracter de escape

# Formateo

name, surname, age = "Armando", "Rodriguez", 25

print("Mi nombre es {} {} y mi edad {}".format(name, surname, age)) # Formateo de cadenas
print("Mi nombre es %s %s y mi edad %d" %(name, surname, age)) # Formateo de cadenas, deinimos el tipo de formato

print(f"Mi nombre es {name} {surname} y mi edad {age}") # Formateo de cadenas, inferencia de datos, si queremos imprimir datos tal cual
print(f"Mi nombre es {name.upper()} {surname.lower()} y mi edad {age}") # Formateo de cadenas, inferencia de datos, si queremos imprimir datos tal
print(f"Mi nombre es {name.capitalize()} {surname.capitalize()} y mi edad {age}") # Hace que el primer caracter de la cadena sea mayuscula y el resto minuscula

# Desempaquetado de caracteres 
language = "Python"
a, b, c, d, e, f = language
print(a)
print(e)
print(d)

# Division de cadenas

language_slicce = language[0:3]
print(language_slicce)

language_slicce = language[1:]
print(language_slicce)

language_slicce = language[-2]
print(language_slicce)

language_slicce = language[1:2:3]
print(language_slicce)

language_slicce = language[0:6:2]
print(language_slicce)

# Reverse

reverse_language = language[::-1]
print(reverse_language)

# Funciones

print(language.upper())
print(language.lower())
print(language.capitalize())
print(language.count("t"))
print(language.replace("t", "T"))
print(language.replace("t", "T", 1))
print(language.find("t"))
print(language.find("T"))
print(language.index("t"))

print(language.isalpha())
print(language.isdigit())
print(language.isalnum())
print(language.islower())
print(language.isupper())

print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo
print("Py".lower() == "py".lower())  # Es lo mismo
print("Py".upper() == "py".upper())  # Es lo mismo
print("Py".upper() == "PY".upper())  # Es lo mismo
print("Py".lower() == "py".lower())  # Es lo mismo  







