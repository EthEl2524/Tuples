#  Python program to add an item to a tuple

tuple_1 = (2, 5, 7, 11, 3)
tuple_1 = tuple_1 + (20,)  # Using merge of tuples with the + operator, add an element, it will create a new tuple
print(tuple_1)

tuple_1 = tuple_1[:5] + ("X", "Y", "Z") + tuple_1[:5]  # adding items in a specific index i.e. at count  of 5
print(tuple_1)

list_1 = list(tuple_1)  # converting the tuple to list
list_1.append("ZZZ")  # use different ways to add items in list
tuple_1 = tuple(list_1)
print(tuple_1)
