
# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprí­mela.
my_tuple = (10, 20 ,30, 40, 50)
print(my_tuple)


# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.
my_tuple = (100, 200, 300, 400, 500)
print(my_tuple[1])


# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
my_tuple = (1, 2, 3)
#my_tuple[1] = 10  # Esto generará un error: TypeError, ya que las tuplas son inmutables


# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
my_tuple = (1, 2, 3, 3, 4, 5, 3)
print(my_tuple.count(3))  # Esto imprimirá 3, ya que el número 3 aparece tres veces


# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
my_tuple = ("Java", "Python", "JavaScript", "Python")
print(my_tuple.index("Python"))  # Esto imprimirá 1, que es el índice de la primera aparición de "Python"


# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
my_tuple1 = (1, 2, 3) 
my_tuple2 = (4, 5, 6)
my_tuple = my_tuple1 + my_tuple2
print(my_tuple)  # Esto imprimirá (1, 2, 3, 4, 5, 6)


# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
my_tuple = (10, 20, 30, 40, 50)
my_subtuple = my_tuple[2:4]  # Esto tomará los elementos en las posiciones 2 y 3
print(my_subtuple)  # Esto imprimirá (30, 40)


# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
my_tuple = ("rojo", "verde", "azul")
my_list = list(my_tuple)  # Convierte la tupla en una lista
my_list[1] = "amarillo"  # Cambia el segundo elemento a "amarillo"
my_modified_tuple = tuple(my_list)  # Convierte la lista de nuevo en una tupla
print(my_modified_tuple) 


# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
my_tuple = (1, 2, 3)
del my_tuple  # Elimina la tupla
#print(my_tuple)
# print(my_tuple)  # Esto generará un error porque my_tuple ya no existe


# 10. Crea una tupla con un solo elemento (el número 100) e imprí­mela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
my_tuple = (100,)  # La coma es necesaria para definir una tupla de un solo elemento
print(my_tuple)

