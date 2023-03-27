#  program to replace the last value of tuples in a list

#  Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#  Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

sample_list = [(10, 20, 30), (40, 50, 60), (70, 80, "XXX")]
print(sample_list)

new_list = [(x, y, 90) if z == "XXX" else (x, y, z) for (x, y, z) in sample_list]
print(new_list)





