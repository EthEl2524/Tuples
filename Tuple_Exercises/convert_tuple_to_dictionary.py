#  convert a tuple to a dictionary


# Create a tuple
tuple_1 = tuple(((3, 'F'), (25, 'Z')))

#  Print dictionary
print(dict((y, x) for x, y in tuple_1))
