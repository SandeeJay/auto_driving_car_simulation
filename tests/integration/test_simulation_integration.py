import unittest
import pytest
from src.auto_driving_car_simulation.simulation.simulation import Simulation
from src.auto_driving_car_simulation.simulation.car import Car
from src.auto_driving_car_simulation.simulation.field import Field


class TestSimulation(unittest.TestCase):

    def test_add_car(self):
        field = Field(5, 5)
        simulation = Simulation(field)
        car = Car("TestCar", 0, 0, 'N')
        simulation.add_car(car)
        self.assertEqual(len(simulation.cars), 1)

    def test_run_simulation(self):
        field = Field(5, 5)
        simulation = Simulation(field)
        car = Car("TestCar", 0, 0, 'N')
        car.set_commands("FFRFF")
        simulation.add_car(car)
        simulation.run_simulation()
        self.assertEqual(car.x, 2)
        self.assertEqual(car.y, 2)
        self.assertEqual(car.direction, 'E')

    def test_duplicate_car_name(self):
        field = Field(5, 5)
        simulation = Simulation(field)
        car1 = Car("TestCar", 0, 0, 'N')
        simulation.add_car(car1)
        with pytest.raises(ValueError):
            Car.validate_car_name("TestCar", simulation)

    def test_reset_simulation(self):
        field = Field(5, 5)
        simulation = Simulation(field)
        car = Car("TestCar", 0, 0, 'N')
        simulation.add_car(car)
        simulation.reset()
        self.assertEqual(len(simulation.cars), 0)
        self.assertEqual(len(simulation.stopped_cars), 0)
        self.assertEqual(len(simulation.collisions), 0)
        self.assertEqual(len(simulation.boundary_collisions), 0)

    def test_collision_detection(self):
        field = Field(5, 5)
        simulation = Simulation(field)
        car1 = Car("Car1", 1, 2, 'N')
        car2 = Car("Car2", 3, 4, 'W')
        car1.set_commands("FF")
        car2.set_commands("FF")
        simulation.add_car(car1)
        simulation.add_car(car2)
        simulation.run_simulation()
        self.assertIn((1, 4), [pos for _, pos in simulation.collisions.values()])

    def test_boundary_collision(self):
        field = Field(5, 5)
        simulation = Simulation(field)
        car = Car("BoundaryTestCar", 0, 0, 'N')
        car.set_commands("FFFFF")
        simulation.add_car(car)
        simulation.run_simulation()
        self.assertIn(car.name, simulation.stopped_cars)
        self.assertIn(car.name, simulation.boundary_collisions)


if __name__ == '__main__':
    unittest.main()
