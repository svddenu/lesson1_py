calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    lenght = 0
    temp = []
    for i in range(len(string)):
        lenght += 1
    temp.append(str(lenght))
    temp.append(string.upper())
    temp.append(string.lower())
    return temp

def is_contains(string, list_search):
    count_calls()
    a = 0
    for i in list_search:
        if string.lower() == i.lower():
            return True
        else:
            a += 1
            if a == len(list_search):
                return False


print(string_info('Armageddon'))
print(string_info('Offensive'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('Avagers', ['averagers', 'AvAggErSS', 'Awagers']))
print(calls)