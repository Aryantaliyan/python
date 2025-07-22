my_tuple=(45,6,7,5,45,3,4,3,"aryan")
print(type(my_tuple))
list=list(my_tuple)
list.remove("aryan")
my_tuple=tuple(list)
print(my_tuple)
print(my_tuple.count(45))
print(my_tuple.index(45))

