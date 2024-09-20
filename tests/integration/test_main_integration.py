import unittest
from src.auto_driving_car_simulation.simulation.field import Field
from src.auto_driving_car_simulation.simulation.car import Car
from src.auto_driving_car_simulation.simulation.simulation import Simulation


class TestSimulationIntegration(unittest.TestCase):

    def setUp(self):
        self.field = Field(5, 5)
        self.simulation = Simulation(self.field)

    def test_multiple_cars_different_commands(self):
        car1 = Car("Car1", 0, 0, 'N')
        car2 = Car("Car2", 1, 1, 'E')
        car3 = Car("Car3", 2, 2, 'S')

        car1.set_commands("FFRFF")
        car2.set_commands("LFFR")
        car3.set_commands("FFLFF")

        self.simulation.add_car(car1)
        self.simulation.add_car(car2)
        self.simulation.add_car(car3)

        self.simulation.run_simulation()

        self.assertEqual(car1.x, 2)
        self.assertEqual(car1.y, 2)
        self.assertEqual(car1.direction, 'E')

        self.assertEqual(car2.x, 1)
        self.assertEqual(car2.y, 3)
        self.assertEqual(car2.direction, 'E')

        self.assertEqual(car3.x, 4)
        self.assertEqual(car3.y, 0)
        self.assertEqual(car3.direction, 'E')


if __name__ == '__main__':
    unittest.main()