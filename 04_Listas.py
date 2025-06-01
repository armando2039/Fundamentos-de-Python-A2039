
### Listas ###
# Las listas son un tipo de dato que nos permite almacenar varios valores en una sola variable.
# Las listas se pueden crear utilizando corchetes [] o la función list().
# Las listas son mutables, es decir, podemos modificarlas una vez que las hemos creado.
# Las listas pueden contener cualquier tipo de dato, incluso otras listas.
# Las listas pueden contener datos duplicados.
# Las listas pueden contener datos de diferentes tipos.

my_list = list()
my_other_list = []

print(len(my_list)) # vamos allar la longitud de la lista
print(len(my_other_list)) # se calcula la longitud del contenido de la variable

my_list = [35, 30, 17, 25, 28]

print(my_list)
print(len(my_list))

my_other_list = ["Armando", "Rodriguez", 25, 1.75, True] # Lista con diferentes tipos de datos
print(my_other_list)

print(type(my_other_list)) # Tipo de dato de la variable
print(type(my_list))

print(my_other_list[2])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])
print(my_other_list[-5])

print(my_other_list.count(25)) # Contar cuantas veces se repite un valor en la lista

name, surname, age, height, is_student = my_other_list
print(name)

my_list2 = "Hola python"
print(my_list)
print(type(my_list))

my_other_list.append("Hola") # Agregar un elemento a la lista, por default al final de la lista
print(my_other_list)

my_other_list.insert(1, "Python") # Agregar un elemento en una posición especifica
print(my_other_list)

my_other_list.remove(25) # Eliminar un elemento de la lista
print(my_other_list) 

my_other_list.pop(1) # Eliminar un elemento de la lista por posición

print(my_list.pop())  # Eliminar el último elemento de la lista y devolverlo
print(my_list)

print(my_list.pop(1))  # Eliminar un elmento de la lista por posición y devolverlo

print(my_list)

my_pop_element = my_list.pop(1) # Eliminar un elemento de la lista por posición y guardarlo en una variable
print(my_pop_element)
print(my_list)

my_new_list = my_list.copy() # Copiar una lista

my_list.clear() # Limpiar una lista
print(my_list) # Lista vacia
print(my_new_list) # Lista copiada

my_new_list.reverse() # Invertir una lista
print(my_new_list)

my_new_list.sort() # Ordenar una lista
print(my_new_list)

my_new_list.find()  # No existe el método find() para listas, se usa index() para encontrar la posición de un elemento
print(my_new_list)


my_new_list.count()  # contar cuantas veces se repite un valor en la lista 
print(my_new_list)


my_new_list.insert()  # insertar un elemento en una posición especifica
my_new_list.append()  # agregar un elemento al final de la lista 
print(my_new_list)



