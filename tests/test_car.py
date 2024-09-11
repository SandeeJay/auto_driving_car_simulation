import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from src.car import Car
from src.field import Field


def test_car_initialization():
    """
    Test the initialization of a Car object.
    """
    car = Car("TestCar", 0, 0, 'N')
    assert car.name == "TestCar"
    assert car.x == 0
    assert car.y == 0
    assert car.direction == 'N'


def test_car_turn_left():
    """
    Test the turn_left method of the Car class.
    """
    car = Car("TestCar", 0, 0, 'N')
    car.turn_left()
    assert car.direction == 'W'


def test_car_turn_right():
    """
    Test the turn_right method of the Car class.
    """
    car = Car("TestCar", 0, 0, 'N')
    car.turn_right()
    assert car.direction == 'E'


def test_car_move_forward():
    """
    Test the move_forward method of the Car class.
    """
    field = Field(5, 5)
    car = Car("TestCar", 0, 0, 'N')
    car.move_forward(field)
    assert car.y == 1


def test_invalid_car_name():
    """
    Test the initialization of a Car object with an invalid name.
    """
    with pytest.raises(ValueError):
        Car("", 0, 0, 'N')


def test_invalid_commands():
    """
    Test the set_commands method of the Car class with invalid commands.
    """
    car = Car("TestCar", 0, 0, 'N')
    with pytest.raises(ValueError):
        car.set_commands("XYZ")
