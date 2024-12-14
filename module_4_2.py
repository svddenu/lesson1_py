def test_func(x):
    a = x ** 2
    b = a / 3
    def inner_func(b):
        if b % 2 == 0:
            print('Четное')
        else:
            print('Нечетное')
    inner_func(b)
    return a, b

print(test_func(7))
print(inner_func(6))