import random

all_roman = [(10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
number = random.randint(3, 20)           # рандмные числа которые будут на колонне

def to_roman(num):                             # функция для перевода из арабских цифр в римские
    roman = ''
    while num > 0:
        for i, r in all_roman:
            while num >= i:
                roman += r
                num -= i
    return roman

def result(number):                             # функция просчета пар
    colums = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                colums += str(i) + str(j)
    return colums


print('При входе в данж мы видим число на колонне')
print('Но вот не задача, число написанно на римском: ' + to_roman(number))
print(result(int(input('Введи число с колонны в наш суперкалькулятор3000: '))))
passwords = str(result(number))

print()
print('Вот пароль для открытия двери: ' + passwords)
#print('Первое число: ' + passwords[0])
#print('Второе число: ' + passwords[-1])