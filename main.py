class Attraction:
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity
        
    def get_details(self):
        return f"Attraction: {self._name}, Capacity: {self._capacity}"
    
    def start(self):
        print("The attraction is starting")

class ThrillRide(Attraction):
    def __init__(self, name, capacity, min_height):
        super().__init__(name, capacity)
        self._min_height = min_height
                
    def start(self):
        print(f"Thrill Ride {self._name} is now starting. Hold on tight!")
        
    def is_eligible(self, person):
        return person._height >= self._min_height
        
class FamilyRide(Attraction):
    def __init__(self, name, capacity, min_age):
        super().__init__(name, capacity)
        self._min_age = min_age
        
    def start(self):
        print(f"Family Ride {self._name} is now starting. Enjoy the fun!")
        
    def is_eligible(self, person):
        return person._age >= self._min_age
        
class Staff:
    def __init__(self, name, role):
        self._name = name
        self._role = role
    
    def work(self):
        print(f"Staff {self._name} is performing their role: {self._role}")
        
class Visitor:
    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height

    def ride(self, attraction):
        if attraction.is_eligible(self):
            print(f"{self._name} can ride {attraction._name}")
        else:
            print(f"Ride access blocked for {self._name}")


thrill = ThrillRide("Dragon Coaster", 20, 140)
family = FamilyRide("Merry-Go-Round", 30, 4)
visitor = Visitor("Emir", 17, 187)
staff = Staff("Saif", "Cleaning")

visitor.ride(thrill)
visitor.ride(family)
staff.work()