
## Loops ##
# Loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or to repeat a block of code multiple times.
# Los bucles se utilizan para iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena) o para repetir un bloque de código varias veces.
# Iterar es intentar repetir algo, no sirve para pasar por el mismo codigo varias veces.
# In Python, there are two main types of loops: for loops and while loops.

# while loop: el while true, mientras sea verdadero has algo.
# while es parecido a la condicional if, pero se repite mientras la condicion sea verdadera.
# en condionales cuando algo se cumple tenemos el else
# else es el caso contrario, si no se cumple la condicion.
# elif es el caso intermedio, si no se cumple la condicion pero se cumple otra.

my_condition = 0

while my_condition <10:
    print(my_condition)
    my_condition += 2  # Incrementa el valor de my_condition en 2 cada vez que se cumple la condicion.
# En este caso, el bucle se ejecutará mientras my_condition sea menor que 10.

else: # Es opcional, si no se cumple la función. No se acepta un else sin un if (while), ni el elif
    print("my condition is greater or equal to 10")

print("the execution continues")

while my_condition < 20: # El while hace que un código se repita varias veces, en función de una condición.
    my_condition += 1
    if my_condition == 15: # if significa si, si se cumple la condición.
        print("se detiene la ejecución")
        break  # salir del bucle si la condicion se cumple.
    print(my_condition)


print("my condition is less than 20")

# la palabra reservada 'for' es para iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena) o para repetir un bloque de código un número específico de veces.
# el bucle 'for', nos sirve para iterar un listado de elementos.

my_list = [35, 24, 62, 52, 30, 30, 17]
# los listados guardan elementos de uno en uno de forma ordenada.
# los listados son mutables, se pueden modificar.
# los listados son iterables, se pueden recorrer.
# los listados son indexables, se pueden acceder a sus elementos por su posición.
# los listados pueden contener elementos de diferentes tipos de datos.

for element in my_list:  # un for se va a repetir tantas ves como elementos tengamos iterables (tanta veces como elementos tenga).
    print(element)

my_tuple = (35, 1.77, "Armando", "Del Real", "Rodriguez")
for element in my_tuple:
    print(element)
# Los tuplas guardan elementos pero no se pueden retocar.
  


my_set ={"Armando", "Del Real", "Rodriguez", 35}
for element in my_set:
    print(element)
# los sets guardan elementos que no estan repetidos.



my_dict = {"Nombre": "Armando", "Apellido": "Del Real", "Edad": 35, "Altura": 1.77}
for element in my_dict:
    print(element)
# los diccionarios guardan elementos en pares de clave y valor.
# los diccionarios guardan elementos de forma clave-valor.

# un for itera estructuras que son iterables. Una estructura iterable lo unico que hace es almacenar más de un valor.
# un for impreme las keys no imprime los valores.
# si quiero imprimir los valores tengo que usar el metodo items() para imprimir los valores.
for key, value in my_dict.items():
    print(key, value)  

