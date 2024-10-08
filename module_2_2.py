fisrtN = input('Ведите 1-ое число: ')
secondN = input('Ведите 2-ое число: ')
thirdN = input('Ведите 3-ое число: ')

if fisrtN == secondN and secondN == thirdN and fisrtN == thirdN:
    print(3)
elif fisrtN == secondN or fisrtN == thirdN or secondN == thirdN:
    print(2)
else:
    print(0)