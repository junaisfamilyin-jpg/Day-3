class vehicle:
    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

class bus(vehicle):
    def display(self):
        print("The name of the bus is", self.name)
        print("The Maximum speed of the bus is", self.max_speed)
        print("The milage of the bus is", self.milage)

school_bus1 = bus("shrimp", 90, 900)
school_bus2 = bus("apple", 899, 93284)
school_bus3 = bus("Coding", 8375, 19283)

# print(school_bus.name)
# print(school_bus.max_speed)
# print(school_bus.milage)
school_bus1.display()
school_bus2.display()
school_bus3.display()
