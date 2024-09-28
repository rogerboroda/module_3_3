def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print("1.Функция с параметрами по умолчанию:")
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params()

print()
print("2.Распаковка параметров:")
values_list = [2, 'orange', 2>1]
values_dict = {'a': 3, 'b': 'apple','c': 1<7}

print_params(*values_list)
print_params(**values_dict)

print()
print("3.Распаковка + отдельные параметры:")
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)