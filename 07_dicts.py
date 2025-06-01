### Dictionaries ###
# Dictionaries are a collection of key-value pairs.
# They are
# - mutable
# - unordered
# - indexed
# - written with curly brackets {}

my_dict = {}
my_other_dict = dict()

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Armando2039", "Apellido": "Brito", "Edad":35, 1:"Python"}

my_dict = {
    "Nombre":"Armando2039",
    "Apellido": "Brito",
    "Edad":35,
    "Lenguajes":["Python", "Kotlin", "Swift"],
    1:1.77
    }

# Esto es un JSON

print(my_other_dict)
print(my_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Nombre"])
 
my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Armando2039" in my_dict)  # False, porque no es una llave
print("Apellido" in my_dict)  # True, porque es una llave, solo se puede buscar "claves"
print(my_dict["Nombre"])

print(my_dict.items()) # un listado de cada uno de los items
print(my_dict.keys()) # un listado de las llaves
print(my_dict.values()) # un listado de los valores

my_new_dict = my_other_dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)





