# operatins on tuple

# creating tuple
my_tuple=("red","green","black","yellow")

# indexing
print(my_tuple[2])

# adding
my_tuple = my_tuple + ("pink",)

# removing
temp_list = list(my_tuple)
temp_list.remove("black")
my_tuple= tuple(temp_list)

print(my_tuple)