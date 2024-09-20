import unittest
from src.auto_driving_car_simulation.simulation.field import Field
from src.auto_driving_car_simulation.simulation.car import Car
from src.auto_driving_car_simulation.simulation.simulation import Simulation


class TestEndToEndSimulation(unittest.TestCase):

    def test_two_car_collision(self):
        # Step 1: Setup the environment
        field = Field(5, 5)
        simulation = Simulation(field)

        # Step 2: Add two cars to the simulation
        car1 = Car("Car1", 0, 0, 'N')
        car2 = Car("Car2", 0, 2, 'S')
        car1.set_commands("FF")
        car2.set_commands("FF")
        simulation.add_car(car1)
        simulation.add_car(car2)

        # Step 3: Run the simulation
        simulation.run_simulation()

        # Step 4: Verify the collision
        self.assertIn(1, simulation.collisions)
        self.assertEqual(simulation.collisions[1][1], (0, 1))
        self.assertIn("Car1", simulation.collisions[1][0])
        self.assertIn("Car2", simulation.collisions[1][0])


if __name__ == '__main__':
    unittest.main()
