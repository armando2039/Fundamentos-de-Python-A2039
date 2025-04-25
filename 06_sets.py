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


my_other_set.add("Rodriguez")
print(my_other_set)

print("Brito" in my_other_set)
print("Brite" in my_other_set)

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


