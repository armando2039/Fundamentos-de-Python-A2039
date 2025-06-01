# Esto es un comentario: 
# Nuestro hola mundo en python
print ("Hola Python") # esto es una cadena de texto, comilla doble o simple es indistinto.
print ('Hola Python')

print(type("Hola Python"))



""" 
Esto es un comentario de varias lineas
Nuestro hola mundo en python

"""

'''
Esto es un comentario de varias lineas
Nuestro hola mundo en python
''' 

# consultar el tipo de dato
print(type("Hola Python")) # tipo de dato string
print(type(10)) # tipo de dato entero: tipo de dato int
print(type(10.5)) # tipo de dato flotante: tipo de dato float
print(type(True)) # tipo de dato booleano: tipo de dato bool
print(type(False)) # tipo de dato booleano: tipo de dato bool
print(type(None)) # tipo de dato NoneType: tipo de dato NoneType
print(type([1,2,3])) # tipo de dato lista: tipo de dato list
print(type((1,2,3))) # tipo de dato tupla: tipo de dato tuple 
print(type({1,2,3})) # tipo de dato conjunto: tipo de dato set
print(type({"nombre":"Juan","edad":25})) # tipo de dato diccionario: tipo de dato dict
print(type(print)) # tipo de dato funcion: tipo de dato function
print(type(len)) # tipo de dato funcion: tipo de dato function
print(type(type)) # tipo de dato type: tipo de dato type
print(type(10) == int) # True: tipo de dato entero
print(type(10) == str) # False: tipo de dato string
print(type("hola") == str) # True: tipo de dato string
print(type("1 + 2j")) # tipo de dato string
print(type(1 + 2j)) # tipo de dato complejo: tipo de dato complex
print(type( 1 + 2j) == complex) # True: tipo de dato complex
print(type( 1 + 2j) == int) # False: tipo de dato int
print(type( 1 + 2j) == float) # False: tipo de dato float


print(type(print("Mi cadena de texto"))) # Tipo 'non type': Nonetype
print(type(print("Mi cadena de texto")) == None) # True: NoneType


