import unittest
from src.auto_driving_car_simulation.simulation.simulation import Simulation
from src.auto_driving_car_simulation.simulation.car import Car
from src.auto_driving_car_simulation.simulation.field import Field


class TestSimulation(unittest.TestCase):

    def setUp(self):
        self.field = Field(5, 5)
        self.simulation = Simulation(self.field)

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

    def test_process_step_execute_commands(self):
        car = Car("TestCar", 0, 0, 'N')
        car.set_commands("FFRFF")
        self.simulation.add_car(car)
        self.simulation.process_step(0)
        self.assertEqual(car.x, 0)
        self.assertEqual(car.y, 1)
        self.assertEqual(car.direction, 'N')

    def test_execute_car_command_turn_left(self):
        car = Car("TestCar", 0, 0, 'N')
        car.set_commands("L")
        self.simulation.add_car(car)
        self.simulation.execute_car_command(car, 0)
        self.assertEqual(car.direction, 'W')

    def test_execute_car_command_turn_right(self):
        car = Car("TestCar", 0, 0, 'N')
        car.set_commands("R")
        self.simulation.add_car(car)
        self.simulation.execute_car_command(car, 0)
        self.assertEqual(car.direction, 'E')

    def test_execute_car_command_move_forward_within_boundaries(self):
        car = Car("TestCar", 0, 0, 'N')
        car.set_commands("F")
        self.simulation.add_car(car)
        self.simulation.execute_car_command(car, 0)
        self.assertEqual(car.x, 0)
        self.assertEqual(car.y, 1)

    def test_execute_car_command_move_forward_out_of_boundaries(self):
        car = Car("TestCar", 0, 4, 'N')
        car.set_commands("F")
        self.simulation.add_car(car)
        self.simulation.execute_car_command(car, 0)
        self.assertEqual(car.x, 0)
        self.assertEqual(car.y, 4)
        self.assertIn(car.name, self.simulation.stopped_cars)
        self.assertIn(car.name, self.simulation.boundary_collisions)

    def test_no_collision(self):
        car1 = Car("Car1", 0, 0, 'N')
        car2 = Car("Car2", 1, 1, 'E')
        self.simulation.add_car(car1)
        self.simulation.add_car(car2)
        self.simulation.check_collisions(0)
        self.assertEqual(len(self.simulation.collisions), 0)

    def test_single_collision(self):
        car1 = Car("Car1", 0, 0, 'N')
        car2 = Car("Car2", 0, 0, 'E')
        self.simulation.add_car(car1)
        self.simulation.add_car(car2)
        self.simulation.check_collisions(0)
        self.assertEqual(len(self.simulation.collisions), 1)
        self.assertIn(1, self.simulation.collisions)
        self.assertEqual(self.simulation.collisions[1], (['Car1', 'Car2'], (0, 0)))


if __name__ == '__main__':
    unittest.main()
