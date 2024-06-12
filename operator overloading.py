class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

b1=Building(5, 'Многоэтажка')
b2=Building(1, "Частный")
print(b1 == b2)

