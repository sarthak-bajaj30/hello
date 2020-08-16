class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    def add_passangers(self, name):
        if not self.open_seats():
            return False
        self.passangers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passangers)



flight = Flight(3)

people =["Harry","ron", "hermoine","ginny"]
for person in people:
    success = flight.add_passangers(person)
    if success:
        print("congrats "+person+" your seat is confirmed")
    else:
        print("sorry no seats available")