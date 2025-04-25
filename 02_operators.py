### Operadores ###

print(3 +4)
print(3 - 4)
print(3 * 4)
print(3 / 4)

# floor division calcula la parte entera de la división
print(10 // 3)
print(3 % 4)

# potencia
print(3 ** 3)

print("Hola" + "Armando" + "Mundo")
print("Hola " + str(3))
print("Hola " * 5)
print("hola " * (2 ** 3))

my_float = 2.5 * 2
print(" Hola " * int(my_float)) 

### Operadores de comparación ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)   
print(3 == 3.0)
print(3 == "3")
print(3 == int("3"))
print(3 == float("3"))
print(3 == float("3.0"))
print(3 == float("3.1"))
print(3 == float("3.9"))

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(5 != 4)

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

print(3 > 4 == 2) 
print("Hola" > "python")
print("Hola" < "python")
print("Hola" == "python")
print("Hola" != "python")
print("Hola" <= "Hola")
print("Hola" >= "Hola")

print("Hola" >= "Bola")
print("Hola" >= "Zola") # Ordenacion lexicografica alfabetica
print("aaaa" >= "abaa") # a no es mayor que b
print("aaaa" >= "aaaa") # a es igual a a
print("aaaa" >= "aaab") # a es menor que b
print("aaaa" >= "aaba") # a es menor que b
print("aaaa" <= "baaa") # a es menor que b # Ordenación alabética por ASCII

### Operadores Lógicos ###
# and, or, not

print(3 > 2 and 4 > 3) 

# Lógica Booleana
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(not True) # False
print(not False) # True

print(not True and True) # False
print(not True or True) # True
print(not False and True) # True
print(not False or True) # True

print(not True and False) # False
print(not True or False) # False
print(not False and False) # False
print(not False or False) # False

print(not True and not True) # False
print(not True or not True) # False
print(not False and not True) # False
print(not False or not True) # True

print(not True and not False) # False
print(not True or not False) # True
print(not False and not False) # True
print(not False or not False) # True

print(not True and not True and not True) # False
print(not True or not True or not True) # False
print(not False and not True and not True) # False
print(not False or not True or not True) # True

print(not(3 > 4)) # True esto es para negar toda al condición = contrario de falso es verdadero
print(not(3 < 4)) # False con que uno de los dos sea verdadero la condición es verdadera
print(not(3 == 4)) # True
print(not(3 != 4)) # False
print(not(3 >= 4)) # True
print(not(3 <= 4)) # False
print(not(3 > 4 and 3 < 4)) # True
















 

