import pytest

from app.app.car import Car


class TestCar:

    @pytest.fixture
    def my_car(self):
        """Create a new car object"""
        return Car("Ford", "Mustang", 2023)

    def test_accelerate(self, my_car):
        """Test the accelerate method"""
        my_car.accelerate()
        assert my_car.speed == 5
        assert my_car.get_speed() == 5
        assert my_car.get_speed() == my_car.speed

    def test_brake(self, my_car):
        """Test the brake method"""
        my_car.brake()
        assert my_car.speed == -5
        assert my_car.get_speed() == -5

    def test_get_speed(self, my_car):
        """Test the get_speed method"""
        assert my_car.get_speed() == 0
        assert my_car.speed == 0

    def test_make(self, my_car):
        """Test the make property"""
        assert my_car.make == "Ford"

    def test_model(self, my_car):
        """Test the model property"""
        assert my_car.model == "Mustang"

    def test_year(self, my_car):
        """Test the year property"""
        assert my_car.year == 2023

# Run the tests
