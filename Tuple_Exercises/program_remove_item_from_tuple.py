sample_list = [(10, 20, 30), (40, 50, 60), (70, 80, 110)]
print(sample_list)

new_list = [(x, y, z) for (x, y, z) in sample_list if z != 110]
print(new_list)
