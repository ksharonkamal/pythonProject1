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

v1=vehicles("BMW",100,80)
v1.seating_capacity(4)
v1.show()

v2=vehicles("Toyota",80,60)
v2.seating_capacity(2)
v2.show()


