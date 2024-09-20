import unittest
from src.auto_driving_car_simulation.simulation.field import Field
from src.auto_driving_car_simulation.simulation.car import Car
from src.auto_driving_car_simulation.simulation.simulation import Simulation


class TestEndToEndSimulation(unittest.TestCase):

    def test_single_car_simulation(self):
        # Step 1: Setup the environment
        field = Field(5, 5)
        simulation = Simulation(field)

        # Step 2: Add a car to the simulation
        car = Car("TestCar", 0, 0, 'N')
        car.set_commands("FFRFF")
        simulation.add_car(car)

        # Step 3: Run the simulation
        simulation.run_simulation()

        # Step 4: Verify the final position and direction
        self.assertEqual(car.x, 2)
        self.assertEqual(car.y, 2)
        self.assertEqual(car.direction, 'E')


if __name__ == '__main__':
    unittest.main()