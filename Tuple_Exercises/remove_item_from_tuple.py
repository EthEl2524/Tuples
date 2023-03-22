#  remove an item from a tuple

tuple_1 = 'T', 1, 'M', 3, 'S', 'C', '@', 'P', 3
print(tuple_1)

tuple_1 = list(tuple_1)  # conversion to list
print(tuple_1)

tuple_1.remove(3)
tuple_1 = tuple(tuple_1)  # converting back to tuple
print(tuple_1)





