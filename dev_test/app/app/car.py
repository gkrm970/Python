class Car:

    # Accelerate rate
    accelerate_rate = 5

    # Brake rate
    brake_rate = 5

    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self) -> int | None:
        self.speed += self.accelerate_rate
        return self.speed

    def brake(self) -> int | float | None:
        self.speed -= self.brake_rate
        return self.speed

    def get_speed(self) -> int | float | None:
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
