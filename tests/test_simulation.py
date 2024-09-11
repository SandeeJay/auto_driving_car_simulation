import pytest
from src.simulation import Simulation
from src.car import Car
from src.field import Field


def test_add_car():
    """
    Test adding a car to the simulation.
    """
    field = Field(5, 5)
    simulation = Simulation(field)
    car = Car("TestCar", 0, 0, 'N')
    simulation.add_car(car)
    assert len(simulation.cars) == 1


def test_run_simulation():
    """
    Test running the simulation.
    """
    field = Field(5, 5)
    simulation = Simulation(field)
    car = Car("TestCar", 0, 0, 'N')
    car.set_commands("FFRFF")
    simulation.add_car(car)
    simulation.run_simulation()
    assert car.x == 2
    assert car.y == 2
    assert car.direction == 'E'


def test_duplicate_car_name():
    """
    Test adding a car with a duplicate name to the simulation.
    """
    field = Field(5, 5)
    simulation = Simulation(field)
    car1 = Car("TestCar", 0, 0, 'N')
    car2 = Car("TestCar", 1, 1, 'E')
    simulation.add_car(car1)
    with pytest.raises(ValueError):
        simulation.add_car(car2)