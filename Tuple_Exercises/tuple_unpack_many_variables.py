#  Python program to unpack a tuple into several variables


#  Creating the tuple
tuple_1 = 1, 2, 3, 4, 5, 6
print(tuple_1)
n1, n2, n3, n4, n5, n6 = tuple_1  # n-tuple is a sequence (or ordered list) of n elements, n is a non-negative integer.


#  Unpacking the tuple
print(n1 + n2 + n3 + n4 + n5 + n6)


#  Numbers of variables should be equal to number of items in tuple
n1, n2, n3, n4, n5, n6 = tuple_1
