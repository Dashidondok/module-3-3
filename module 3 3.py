def print_params(a = 1, b = 'stoka', c = True):
    print(a, b, c)
print_params(3, 8)
print_params(15)
print_params()

print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['Urban', 185, 61]
values_dict = {'a' : 2, 'b' : 5, 'c' : False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['univers', 17]
print_params(*values_list_2, 42)