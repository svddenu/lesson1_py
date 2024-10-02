# Словарь
my_dict = {'Name': 'svdden', 'birth': 2002, }
print(my_dict)

print(my_dict.get('Name'))
print(my_dict.get('date' , 'Не установлена дата'))

my_dict.update({'date': 14.11, 'email': '@ya.ru'})
print(my_dict)
del my_dict['date']
print(my_dict)

# Множества
my_set = {1, 1, 2, 2, 3, 4, 7, 8, 8, 'Names', 'Uza','Uza', 'names', 1.22}
print(my_set)
my_set.add(15)
my_set.add('dates')
my_set.remove('Names')
print(my_set)