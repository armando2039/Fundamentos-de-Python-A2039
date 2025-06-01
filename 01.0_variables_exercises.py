
# 1. Declara y asigna valores a las siguientes variables:
# a)	name: una cadena que contenga tu nombre.
# b)	age: un número entero que represente tu edad.
# c)	height: un número flotante que represente tu altura.
# d)	Imprime cada variable en una lí­nea separada.

name = "Armando"
age = 35
height = 1.75

print(name)
print(age)
print(height)


# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuántos años tienes.

age_str = str(age)
print(type(age_str))

print('Me llamo', name, 'y tengo', age_str, 'años.')


# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprí­mela.

is_student = True
print('Me llamo', name, 'y soy estudiante:', is_student)


# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.

full_name = "Armando A2039 Sr_Rodriguez"
print(len(full_name))


# 5. Declara tres variables en una sola línea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.

name, surname, city = 'Armando', 'Rodriguez', 'Madrid'
print('Me llamo', name, surname, 'y soy de', city)


# 6. Usa la función input() para solicitar al usuario su color favorito y almacénale en una variable color. Luego, imprime el valor ingresado.

color = input('¿Cuál es tu color favorito? ')
name =input('¿Cuál es tu nombre? ')
print('Hola me llamo', name, 'y mi color favorito es', color)


# 7. Declara una variable fruit e inicialí­zala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = 'Manzana'
print('La fruta es:', fruit)
fruit = 'Pera'
print('La fruta es:', fruit)


# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprí­melo.

price = 10.85
price_int = int(price)
print('El precio es:', price_int)
print(int(price))


# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección usando la función len(). Imprime el resultado.

adress = 'Calle Siempre Viva 689'
address_len = len(adress)
print('La dirección tiene', address_len, 'caracteres.')


# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().
phone = int(5549483949)
print(type(phone))
phone = 7471071005

phone_str = str(phone)
print(type(phone_str))



# 11. Declara una variable llamada is_active y asígnale un valor booleano. Luego, cambia su valor a su opuesto (True a False o viceversa) e imprímelo.
is_active = True
print('El valor de is_active es:', is_active)
is_active = not is_active # not es el operador lógico que invierte el valor booleano
print('El valor de is_active es:', is_active)

# 12. Declara una variable llamada pi y asígnale el valor de pi (3.14159). Luego, imprímelo con 2 decimales.
pi = 3.14159
print('El valor de pi es:', round(pi, 2)) # round() redondea el número a 2 decimales