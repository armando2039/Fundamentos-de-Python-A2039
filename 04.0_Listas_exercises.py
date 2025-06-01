
# 1. Crea una lista con los números del 1 al 5 e imprí­mela. 
my_list = [1, 2, 3, 4, 5]
print(my_list)


# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
my_other_list = [10, 20, 30, 40, 50]
print(my_other_list[2]) # Imprime el tercer elemento (índice 2)


# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprí­mela.
my_list = [1, 2, 3, 4, 5]
my_list.append(6) # Agrega el número 6 al final de la lista
print(my_list) # Imprime la lista actualizada


# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].
my_other_list = [10, 20, 30, 40, 50]
my_other_list.insert(2, 15)  # Inserta el número 15 en la posición 2 (índice 2)
print(my_other_list)


# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
my_other_list = [10, 20, 30, 30, 40, 50]
my_other_list.remove(30)  # Elimina el primer valor 30 de la lista
print(my_other_list)


# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable. Imprime la variable y la lista.
my_list = [1, 2, 3, 4, 5]
last_element = my_list.pop()  # Elimina el última elemento y lo almacena en una variable llamada last_element
print(last_element)  # Imprime el último elemento eliminado
print(my_list)  # Imprime la lista actualizada después de eliminar el último elemento


# 7. Invierte la lista [100, 200, 300, 400, 500] e imprí­mela.
my_other_list = [100, 200, 300, 400, 500]
my_other_list.reverse()  # Invierte la lista
print(my_other_list)  # Imprime la lista invertida


# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprí­mela.
my_list = [3, 1, 4, 2, 5]
my_list.sort()  # Ordena la lista en orden ascendente
print(my_list) 


# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
my_list = my_list1 + my_list2  # Concatena las dos listas
print(my_list)  # Imprime la lista resultante de la concatenación


# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
my_other_list = [10, 20, 30, 40, 50]
my_sublist = my_other_list[1:3]  # Crea una sublista desde la posición 1 hasta la 3 (sin incluir la 3)
print(my_sublist)  # Imprime la sublista creada






