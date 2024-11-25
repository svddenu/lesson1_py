def print_params(a = 1, b = '', c = True):
    print(a, b, c)

value_list = (1, 'String', False)
value_dict = {'a': 3, 'b': 'Python', 'c': False}
value_list_2 = (True, 'GG')

print_params(*value_list)
print_params(**value_dict)
print_params(*value_list_2, 42)