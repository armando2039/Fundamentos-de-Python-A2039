
# 1. Crea un set con los números del 1 al 5 e imprí­melo.
my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))


# 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprí­melo.
my_set.add(6) # Añade el número 6 al set
print(my_set)


# 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?
my_set.add(5) # Intenta añadir el número 5 al set nuevamente
print(my_set)
# Salida: {1, 2, 3, 4, 5, 6} (no cambia por que los sets no admiten duplicados)



# 4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado.
print(3 in my_set)  # Verifica si el número 3 está en el set y lo imprime


# 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
my_set.remove(4)  # Elimina el número 4 del set
print(my_set) 


# 6. Usa el método clear() para vaciar un set y luego imprime su longitud.
my_set.clear()  # Vacía el set.
print(len(my_set))  # Imprime la longitud del set (debería ser 0).


# 7. Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.
my_set = {"manzana", "naranja", "plátano"}  # Crea un set de frutas
my_list = list(my_set)  # Convierte el set en una lsita
print(type(my_list)) 
print(my_list[0])  # imprime el primer elemento de la lista.


# 8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
my_set1 = {1, 2, 3}  # Primer set.
my_set2 = {4, 5, 6}  # Segundo set.
my_union_set = my_set1.union(my_set2)  # realiza la unión de los dos sets.
print(my_union_set)


# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
my_set1 = {1, 2, 3, 4}  # Primer set.
my_set2 = {3, 4, 5, 6}  # Segundo set.
my_difference_set = my_set1.difference(my_set2)  #Calcula la diferencia entre los dos sets.
print(my_difference_set)
# resultado: {1, 2} (elementos que están en my_set1 pero no en my_set2), {1, 2, 5, 6} (elementos que están en my_set2 pero no en my_set1)


# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.
my_set = {1, 2, 3}  # Crea un set.
del my_set  # Elimina el set usando del.
# print(my_set)  # Esto generará un error: NameError porque my_set ya no existe.
# Intentar imprimir my_set después de eliminarlo generará un error.
try:
    print(my_set)  # Esto generará un error: NameError porque my_set ya no existe.
except NameError as e: # Captura el error si my_set no existe.
    # Maneja el error de que my_set no existe.
    # Puedes imprimir un mensaje de error o manejarlo de otra manera.
    # Aquí, simplemente imprimimos el error.
    # Esto es útil para evitar que el programa se detenga abruptamente.
    # y para proporcionar una retroalimentación clara sobre lo que salió mal.
    print(f"Error: {e}")   # Esto imprimirá el error: name 'my_set' is not defined
# Salida: Error: name 'my_set' is not defined 



# El set ha sido eliminado correctamente.
# 11. Crea un set vacío y verifica su tipo.
my_empty_set = set()  # Crea un set vacío.
print(my_empty_set)  # Imprime el set vacío.

# discard() no lanza un error si el elemento no existe.
# remove() lanza un error si el elemento no existe.