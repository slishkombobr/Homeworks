class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            for floor in range(1, new_floor + 1):
                print(floor)
            else:
                print("Такого этажа не существует")

house = House('ЖК Эльбрус', 30)
house.go_to(5)
house.go_to(31)

house1 = House('ЖК Горский', 18)
house1.go_to(2)
house1.go_to(20)

house2 = House('Домик в деревне', 2)
house2.go_to(5)
house2.go_to(31)



