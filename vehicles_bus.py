class vehicles:
    wheels=4
    def __init__(self,company,max_speed,milage):
        self.company=company
        self.max_speed=max_speed
        self.milage=milage
    def seating_capacity(self,capacity):
        self.capacity=capacity

    def show(self):
        print("Company:",self.company)
        print("Maximum speed:",self.max_speed)
        print("Milage:",self.milage)
        print("Seating Capacity",self.capacity)
        print("Wheels:",vehicles.wheels)

class bus(vehicles):
    def __init__(self,company,max_speed,milage,fuel):
        self.fuel=fuel
        super().__init__(company,max_speed,milage)

    def show(self):
        super().show()
        # print("Company:",self.company)
        # print("Maximum speed:",self.max_speed)
        # print("Milage:",self.milage)
        # print("Seating Capacity",self.capacity)
        # print("Wheels:",vehicles.wheels)
        print("Fule used:",self.fuel)


b1=bus("Toyota",500,350,"Petrol")
b1.seating_capacity(20)
b1.show()

v1=vehicles("BMW",100,80)
v1.seating_capacity(4)
v1.show()




