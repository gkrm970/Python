class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed


# Create a new car object
my_car = Car("Ford", "Mustang", 2023)

# Print the car's make, model, and year
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")

# Accelerate the car
my_car.accelerate()
print(f"Current speed: {my_car.get_speed()}")

# Brake the car
my_car.brake()
print(f"Current speed: {my_car.get_speed()}")
