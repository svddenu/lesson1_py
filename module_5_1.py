class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def go_to(self, floor):
        if floor <= 0 or floor >= self.floors:
            print('Такого этажа нет')
        else:
            for i in range(1, floor + 1):
                print(i)

h1 = House('ЖК Горский', 30)
h2 = House('Домик в деревне', 2)

print(h1.go_to(5))
print(h2.go_to(5))