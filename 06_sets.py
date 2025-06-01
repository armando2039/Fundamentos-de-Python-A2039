### Sets ###

my_set = set()
my_other_set = {}


print(type(my_set))
print(type(my_other_set))

my_other_set = {"Armando2039", "Brito", 35}
print(type(my_other_set))

print(len(my_other_set))

# un set no es una estrcutura ordenada
# un set no puede tener elementos duplicados
# un set no puede tener elementos mutables
# No se pueden acceder a los elementos de un set por su indice, elemento o, elemento 1, etc.

my_other_set.add("Rodriguez")  ### Por dentro lo que esta utilizando es un hash para almacenar los elementos.
print(my_other_set)            ### Por lo cual no se pueden tener elementos mutables como listas o diccionarios. 

### Tampoco se puede acceder a los elementos por su indice.
### un set mo admite operaciones como el slicing, por lo cual no se puede acceder a un elemento en especifico.
### para permitir que no exista repetidos, se utiliza un hash para almacenar los elementos.
                         
                         
                               
print("Brito" in my_other_set)  ## in es un operador que verifica si un elemento esta dentro de un set.

print("Brite" in my_other_set)  # not in is the opposite of in palabra rerservada que verifica si un elemento no esta dentro de un set.


### dell, palabra reservada del sistema.
#### para eliminar un elemento de un set se utiliza la palabra reservada remove, discard o pop.
### remove elimina un elemento del set, si el elemento no existe, lanza un error.
### discard elimina un elemento del set, si el elemento no existe, no lanza un error.

### las operaciones propias de un objeto accedemos a ellas con el punto.

my_other_set.remove("Brito")
print(my_other_set)

my_set = {"Armando2039", "Brito", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set.clear()
print(len(my_other_set))

my_other_set = {"Kotlin", "Swift", "python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set.union(my_set).union({"JavaScript", "c#"})))

print(my_new_set.difference(my_set))


