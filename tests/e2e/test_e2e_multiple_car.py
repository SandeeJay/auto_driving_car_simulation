import unittest
from unittest.mock import patch
from src.auto_driving_car_simulation.main import main
from src.auto_driving_car_simulation.simulation.simulation import Simulation
from src.auto_driving_car_simulation.simulation.car import Car
from src.auto_driving_car_simulation.simulation.field import Field


class TestE2EMultipleCars(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        '5 5',  # Field dimensions
        '1', 'Car1', '0 0 N', 'FFRFF',  # Add Car1
        '1', 'Car2', '1 1 E', 'LFFR',  # Add Car2
        '1', 'Car3', '2 2 S', 'FFLFF',  # Add Car3
        '1', 'Car4', '3 3 W', 'RFFL',  # Add Car4
        '1', 'Car5', '4 4 N', 'FFRFF',  # Add Car5
        '2'  # Run simulation
    ])
    @patch('builtins.print')
    def test_multiple_cars_simulation(self, mock_print, mock_input):
        try:
            main()
        except StopIteration:
            pass
        self.assertTrue(mock_print.called)
        mock_print.assert_any_call("After simulation, the result is:")

        # Verify final positions and directions
        field = Field(5, 5)
        simulation = Simulation(field)
        car1 = Car("Car1", 0, 0, 'N')
        car1.set_commands("FFRFF")
        car2 = Car("Car2", 1, 1, 'E')
        car2.set_commands("LFFR")
        car3 = Car("Car3", 2, 2, 'S')
        car3.set_commands("FFLFF")
        car4 = Car("Car4", 3, 3, 'W')
        car4.set_commands("RFFL")
        car5 = Car("Car5", 4, 4, 'N')
        car5.set_commands("FFRFF")
        simulation.add_car(car1)
        simulation.add_car(car2)
        simulation.add_car(car3)
        simulation.add_car(car4)
        simulation.add_car(car5)
        simulation.run_simulation()

        self.assertEqual((car1.x, car1.y, car1.direction), (2, 2, 'E'))
        self.assertEqual((car2.x, car2.y, car2.direction), (1, 3, 'E'))
        self.assertEqual((car3.x, car3.y, car3.direction), (4, 0, 'E'))
        self.assertEqual((car4.x, car4.y, car4.direction), (3, 4, 'N'))
        self.assertEqual((car5.x, car5.y, car5.direction), (4, 4, 'N'))


if __name__ == '__main__':
    unittest.main()
