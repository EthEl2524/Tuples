#  Python program to create the colon of a tuple

tuple_1 = ('T', 'u', 'p', 'l', 'e')
tuple_1 = ''.join(tuple_1)
print(tuple_1)
tuple_1 = list(tuple_1)
tuple_1.append(':')
tuple_1 = tuple(tuple_1)
tuple_1 = ''.join(tuple_1)
print(tuple_1)



from copy import deepcopy


#  create a tuple
tuplex = ("HELLO", 5, [], True)
print(tuplex)

#  make a copy of a tuple using deepcopy() function
tuplex_colon = deepcopy(tuplex)
tuplex_colon[2].append(50)
print(tuplex_colon)
print(tuplex)
