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

    def __len__(self):
        return self.floors

    def __str__(self):
        return f'"{self.name}", кол-во этажей {self.floors}'

h1: House = House('ЖК Горский', 30)
h2 = House('Домик в деревне', 2)

print(h1)
print(h2)
print()
print(len(h1))
print(len(h2))