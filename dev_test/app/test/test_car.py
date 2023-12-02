import pytest

from app.app.car import Car


class TestCar:

    @pytest.fixture
    def my_car(self) -> Car:
        """Create a new car object"""
        return Car("Ford", "Mustang", 2023)

    year = 2023
    accelerate_rate = 5
    brake_rate = -5
    speed_after_accelerate = 5
    current_speed = 0

    def test_accelerate(self, my_car: Car) -> None:
        """Test the accelerate method"""
        my_car.accelerate()
        assert my_car.speed == self.speed_after_accelerate
        assert my_car.get_speed() == self.speed_after_accelerate

    def test_brake(self, my_car: Car) -> None:
        """Test the brake method"""
        my_car.brake()
        assert my_car.speed == self.brake_rate
        assert my_car.get_speed() == self.brake_rate

    def test_get_speed(self, my_car: Car) -> None:
        """Test the get_speed method"""
        assert my_car.get_speed() == self.current_speed
        assert my_car.speed == self.current_speed

    def test_make(self, my_car: Car) -> None:
        """Test the make property"""
        assert my_car.make == "Ford"

    def test_model(self, my_car: Car) -> None:
        """Test the model property"""
        assert my_car.model == "Mustang"

    def test_year(self, my_car: Car) -> None:
        """Test the year property"""
        assert my_car.year == self.year


# Run the tests
