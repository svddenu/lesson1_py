immutable_var = (1, 2, 4, 6, 8, 'kuku')
print(immutable_var)
# immutable_var [0, 3] = 8             Нельзя изменить так как неизменяемый тип кортежа, в отличии от списка
# Но можно создать кортеж с списком внутри и присваивать другие значения в этом списке
immutable_var_2 = ([1, 2 , 6], 0, 8)
print(immutable_var_2)
immutable_var_2 [0][0] = 8
print(immutable_var_2)


InBox = ['apples', 4, 'bananas', 2, 'phones', 1]
print(InBox)
InBox [4] = 'laptop'
print(InBox + ['Modified'])