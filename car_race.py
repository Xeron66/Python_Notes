class Car:
    def __init__(self, name: str, speed: int, fuel: int):
        self.name = name
        self.speed = speed
        self.fuel = fuel
        self.distance = 0

    def move(self):
        self.distance = self.distance + self.speed
        self.fuel = max(self.fuel - self.speed, 0)
    
    def status(self):
        return f'Car: {self.name} -> Distance: {self.distance} | Fuel: {self.fuel}'



car1: Car = Car("Ferrari", 10, 50)
car2: Car = Car("Lambo", 8, 40)

i = 0
print("--- Race Start! Finish line at 50 units ---")
while True:
    i+=1
    print("Turn ", i,": ")
    car1.move()
    print(car1.status())
    car2.move()
    print(car2.status())
    if car1.distance >= 50:
        print(f'Winner: ({car1.name})')
        break
    elif car2.distance >= 50:
        print(f'Winner: ({car2.name})')
        break
    elif car1.fuel <= 0:
        print(f'Winner: ({car2.name})')
        break
    elif car2.fuel <= 0:
        print(f'Winner: ({car1.name})')
        break
    elif car1.fuel <= 0 and car2.fuel <= 0:
        print("No Winner!")
        break