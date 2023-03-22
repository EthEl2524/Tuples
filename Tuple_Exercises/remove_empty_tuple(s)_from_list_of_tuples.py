#  remove an empty tuple(s) from a list of tuples

#  Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
#  Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

sample_data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
print(sample_data)
delete_empty_tuple = [t for t in sample_data if t]
print(delete_empty_tuple)

