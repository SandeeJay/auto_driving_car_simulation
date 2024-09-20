# tests/unit/test_car.py
import pytest
from src.auto_driving_car_simulation.simulation.car import Car
from src.auto_driving_car_simulation.simulation.field import Field
from src.auto_driving_car_simulation.simulation.simulation import Simulation


def test_car_initialization():
    car = Car("TestCar", 0, 0, 'N')
    assert car.name == "TestCar"
    assert car.x == 0
    assert car.y == 0
    assert car.direction == 'N'


def test_car_turn_left():
    car = Car("TestCar", 0, 0, 'N')
    car.turn_left()
    assert car.direction == 'W'


def test_car_turn_right():
    car = Car("TestCar", 0, 0, 'N')
    car.turn_right()
    assert car.direction == 'E'


def test_car_move_forward():
    field = Field(5, 5)
    car = Car("TestCar", 0, 0, 'N')
    car.move_forward(field)
    assert car.y == 1


def test_duplicate_car_name():
    field = Field(5, 5)
    simulation = Simulation(field)
    car1 = Car("TestCar", 0, 0, 'N')
    simulation.add_car(car1)
    with pytest.raises(ValueError):
        Car.validate_car_name("TestCar", simulation)


def test_invalid_car_name():

    field = Field(5, 5)
    simulation = Simulation(field)
    with pytest.raises(ValueError):
        Car.validate_car_name("", simulation)


def test_invalid_commands():
    car = Car("TestCar", 0, 0, 'N')
    with pytest.raises(ValueError):
        car.set_commands("XYZ")


def test_move_forward_within_boundaries():
    field = Field(5, 5)
    car = Car("TestCar", 0, 0, 'N')
    car.move_forward(field)
    assert car.x == 0
    assert car.y == 1


def test_move_forward_out_of_boundaries():
    field = Field(5, 5)
    car = Car("TestCar", 0, 4, 'N')
    car.move_forward(field)
    assert car.x == 0
    assert car.y == 4  # Sho
