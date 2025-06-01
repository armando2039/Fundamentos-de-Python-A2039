### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.70, "Armando2039", "Brito")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])



print(my_tuple.count("Armando2039"))
print(my_tuple.count("Rodriguez"))
print(my_tuple.index("Brito"))
print(my_tuple.index("Armando2039"))


### Tuples are immutable, you can't change the values of a tuple

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple) # Convertir una tupla a lista
print(type(my_tuple))

my_tuple[3] = "Rodriguez" # Cambiar un valor de la lista
my_tuple.insert(1, "Azul") # Insertar un valor en una posición específica
my_tuple = tuple(my_tuple) # Convertir una lista a tupla
print(my_tuple)
print(type(my_tuple))

del my_tuple # Eliminar una tupla
print(my_tuple)  # Esto generará un error porque my_tuple ya no existe

















