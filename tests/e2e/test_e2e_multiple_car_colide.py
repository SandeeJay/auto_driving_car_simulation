import unittest
from src.auto_driving_car_simulation.simulation.field import Field
from src.auto_driving_car_simulation.simulation.car import Car
from src.auto_driving_car_simulation.simulation.simulation import Simulation


class TestMultipleCarCollision(unittest.TestCase):

    def test_multiple_car_collision(self):
        field = Field(10, 10)
        simulation = Simulation(field)

        # Step 2: Add multiple cars to the simulation
        car1 = Car("Car1", 5, 5, 'N')
        car2 = Car("Car2", 5, 6, 'S')
        car3 = Car("Car3", 6, 5, 'W')
        car4 = Car("Car4", 6, 6, 'E')
        car1.set_commands("F")
        car2.set_commands("F")
        car3.set_commands("F")
        car4.set_commands("F")
        simulation.add_car(car1)
        simulation.add_car(car2)
        simulation.add_car(car3)
        simulation.add_car(car4)

        # Step 3: Run the simulation
        simulation.run_simulation()

        # Step 4: Verify the collisions
        self.assertIn(1, simulation.collisions)
        self.assertEqual(simulation.collisions[1][1], (5, 6))
        self.assertIn("Car1", simulation.collisions[1][0])
        self.assertIn("Car2", simulation.collisions[1][0])

        # Verify final positions and directions of cars
        self.assertEqual((car3.x, car3.y, car3.direction), (5, 5, 'W'))
        self.assertEqual((car4.x, car4.y, car4.direction), (7, 6, 'E'))


if __name__ == '__main__':
    unittest.main()
