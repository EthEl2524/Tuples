#  convert a list of tuples into a dictionary

_list = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
_dict = {}

for a, b in _list:
    _dict.setdefault(a, []).append(b)
    print(_dict)
    