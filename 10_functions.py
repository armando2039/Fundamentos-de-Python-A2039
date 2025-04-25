### Functions ###

# una función intenta encapsular una logica muy concreta, 
# una función va ah intentar resolver un problema concreteo que nosotros vamos a indicar.

def my_function ():
    print("Esto es una función")


my_function () # la función se define con la palabra reservada def, seguida del nombre de la función y paréntesis.
my_function () # Una función nos srive para llamarla y ejecute código.
my_function () 

def sum_two_values (first_number, second_number):
    print(first_number + second_number)

    return first_number + second_number # return devuelve el resultado de la función.
# return es el resultado de la función.

sum_two_values (5, 7) # la función se llama y se le pasan los argumentos.
# primero una función simple, despues una función que resibe paramétros.
sum_two_values (54754, 71231)
sum_two_values ("5", "7")
sum_two_values (1.4, 5.2)  


def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return first_value + second_value


my_result = sum_two_values (1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return (10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}") #vamos a tener un formato de cadena, vamos acceder a los valores de la cadena.

print_name ("Armando", "Del Real")

def print_texts(*texts): # el asterisco indica que se van a recibir varios valores.
    for text in texts: # el for va a iterar sobre los textos.
        print(text)
         
print_texts ("Hola", "Adios", "Hasta luego") # se le pasan varios argumentos a la función.



def print_upper_texts(*texts):
    print(type(texts)) # el type nos dice que tipo de dato es, el texts indica que es una tupla.
    print(len(texts)) # el len nos dice la longitud de la tupla.
    for text in texts: # el for indica que va a iterar sobre los textos, el in indica que va a iterar sobre los textos.
        print(text.upper()) # el upper convierte el texto a mayúsculas.
    

# print_upper_texts ("Hola", "Adios", "Hasta luego") # se le pasan varios argumentos a la función.
# print_upper_texts ("Hola", "Adios", "Hasta luego", "Esto es un texto") # se le pasan varios argumentos a la función.
# print_upper_texts ("Hola", "Adios", "Hasta luego", "Esto es un texto", "Esto es otro texto") # se le pasan varios argumentos a la función.

# En realidad lo que hace es intrepretarlo como una tupla, es decir que le estamos pasando valores concatenados, uno tras otro con una coma.


