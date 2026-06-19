class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        final_fare = total_fare + (total_fare * 10 / 100)
        return final_fare


bus = Bus(50)
print("Total Bus fare is: INR", int(bus.fare()))
