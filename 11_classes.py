### Classes ###
# es el concepto de poder identificar nuestro código dentro de un ambito de actuación.

class MyPerson: # En este caso los nombres de las clases se escriben con CamelCase.
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def sayHello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')

        pass # es la manera de intentar que se ejecute un bloque de código, pero no se ejecuta nada
        # pass es una instrucción nula que no hace nada.

print (MyPerson)

class Person: 
    def __init__ (self, name, surname): # es el constructor clase, se ejecuta cuando se crea un objeto de la clase.
        self.name = name
        self.surname = surname # self se refiere a la instancia de la clase, es decir, a la persona que se está creando.
# esto significa que ya tenemos la capacidad de que esta persona pueda recibir un parámetro.

my_person = Person('Armando', 'Rodriguez')
print(f"{my_person.name} {my_person.surname}") # f es una forma de formatear cadenas de texto, y se utiliza para insertar variables dentro de una cadena de texto.
# en este caso estamos creando un objeto de la clase Person, y le estamos pasando los parámetros name y surname.


class Person: 
    def __init__ (self, name, surname, alias = "sin alias"): # el alias es un parámetro opcional, si no se le pasa nada, se le asigna el valor por defecto "sin alias".):
        self.full_name = f"{name} {surname} ({alias})" # me estoy creando una propiedad almacenada que se llama full name.

    def walk (self):
        print(f"{self.full_name} is walking")
        

my_person = Person('Armando', 'Rodriguez')
print(my_person.full_name)
my_person.walk()

my_other_person = Person('Armando', 'Rodriguez', 'Sr. Rodriguez')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Alan del Valle (Alan del Real)" # accedemos a la propiedad full_name y le asignamos un nuevo valor.
# esto no es una buena práctica, ya que estamos modificando el valor de una propiedad de la clase.
print(my_other_person.full_name)

self.__class_name # es una forma de hacer que la propiedad sea privada, y no se pueda acceder desde fuera de la clase.
# en este caso, no se puede acceder a la propiedad full_name desde fuera de la clase.

def get_name(self):
    return self.full_name # es una forma de acceder a la propiedad full_name desde fuera de la clase.
def set_name(self, name):
    self.full_name = name # es una forma de modificar la propiedad full_name desde fuera de la clase.
def del_name(self):
    del self.full_name # es una forma de eliminar la propiedad full_name desde fuera de la clase.

self # es una forma de acceder a la instancia de la clase, es decir, a la persona que se está creando.

         