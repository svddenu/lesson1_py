def get_multiplied_digits(number):
    str_number = str(number).lstrip('0')
    if not str_number:
        return 1
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


print(get_multiplied_digits(40203))
print(get_multiplied_digits(6))
print(get_multiplied_digits(6123))
