# tests/unit/test_simulation.py
import unittest
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
        field = Field(10, 10)
        simulation = Simulation(field)
        car1 = Car("Car1", 1, 2, 'N')
        car2 = Car("Car2", 7, 8, 'W')
        car1.set_commands("FFRFFFFRRL")
        car2.set_commands("FFLFFFFFFF")
        simulation.add_car(car1)
        simulation.add_car(car2)
        simulation.run_simulation()
        print([car for car in simulation.cars])  # Debugging output
        self.assertIn((5, 4), [pos for _, pos in simulation.collisions.values()])

    def test_boundary_collision(self):
        field = Field(5, 5)
        simulation = Simulation(field)
        car = Car("BoundaryTestCar", 0, 0, 'N')
        car.set_commands("FFFFF")
        simulation.add_car(car)
        simulation.run_simulation()
        self.assertIn(car.name, simulation.stopped_cars)


if __name__ == '__main__':
    unittest.main()
