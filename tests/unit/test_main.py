import unittest
import pytest
from unittest.mock import patch, MagicMock
from src.auto_driving_car_simulation.main import setup_field, add_car_to_simulation, get_valid_car_name, get_valid_car_position, get_valid_car_commands, handle_post_simulation_options, main
from src.auto_driving_car_simulation.simulation.field import Field
from src.auto_driving_car_simulation.simulation.car import Car
from src.auto_driving_car_simulation.simulation.simulation import Simulation


class TestMainFunctions(unittest.TestCase):

    @patch('builtins.input', side_effect=['5 5'])
    def test_setup_field(self, mock_input):
        field = setup_field()
        self.assertEqual(field.width, 5)
        self.assertEqual(field.height, 5)

    @patch('builtins.input', side_effect=['Car1', '0 0 N', 'FFRFF'])
    def test_add_car_to_simulation(self, mock_input):
        field = Field(5, 5)
        simulation = Simulation(field)
        add_car_to_simulation(simulation)
        self.assertEqual(len(simulation.cars), 1)
        self.assertEqual(simulation.cars[0].name, 'Car1')

    @patch('builtins.input', side_effect=['Car1'])
    def test_get_valid_car_name(self, mock_input):
        field = Field(5, 5)
        simulation = Simulation(field)
        name = get_valid_car_name(simulation)
        self.assertEqual(name, 'Car1')

    @patch('builtins.input', side_effect=["", "Car1"])
    def test_get_valid_car_name_empty(self, mock_input):
        field = Field(5, 5)
        simulation = Simulation(field)
        name = get_valid_car_name(simulation)
        self.assertEqual(name, 'Car1')

    @patch('builtins.input', side_effect=['0 0 N'])
    def test_get_valid_car_position(self, mock_input):
        field = Field(5, 5)
        simulation = Simulation(field)
        x, y, direction = get_valid_car_position(simulation, 'Car1')
        self.assertEqual((x, y, direction), (0, 0, 'N'))

    @patch('builtins.input', side_effect=['-1 0 N', '0 -1 N', '5 5 N', '0 0 N'])
    @patch('builtins.print')
    def test_get_valid_car_position_out_of_bounds(self, mock_print, mock_input):
        field = Field(5, 5)
        simulation = Simulation(field)
        x, y, direction = get_valid_car_position(simulation, 'Car1')
        self.assertEqual((x, y, direction), (0, 0, 'N'))
        self.assertEqual(mock_print.call_count, 3)

    @patch('builtins.input', side_effect=['FFRFF'])
    def test_get_valid_car_commands(self, mock_input):
        commands = get_valid_car_commands('Car1')
        self.assertEqual(commands, 'FFRFF')

    @patch('builtins.input', side_effect=['FFXFF', 'FFRFF'])
    @patch('builtins.print')
    def test_get_valid_car_commands_invalid(self, mock_print, mock_input):
        commands = get_valid_car_commands('Car1')
        self.assertEqual(commands, 'FFRFF')
        self.assertEqual(mock_print.call_count, 1)

    @patch('builtins.input', side_effect=['5 5', '1', 'Car1', '0 0 N', 'FFRFF', '2'])
    @patch('builtins.print')
    def test_main(self, mock_print, mock_input):
        try:
            main()
        except StopIteration:
            pass
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=['0 0 A', '0 0 N'])
    @patch('builtins.print')
    def test_get_valid_car_position_invalid_direction(self, mock_print, mock_input):
        field = Field(5, 5)
        simulation = Simulation(field)
        x, y, direction = get_valid_car_position(simulation, 'Car1')
        self.assertEqual((x, y, direction), (0, 0, 'N'))
        self.assertEqual(mock_print.call_count, 1)

    @patch('builtins.input', side_effect=['1'])
    @patch('src.auto_driving_car_simulation.main.main', side_effect=StopIteration)
    def test_handle_post_simulation_options_reset(self, mock_main, mock_input):
        field = Field(5, 5)
        simulation = Simulation(field)
        with self.assertRaises(StopIteration):
            handle_post_simulation_options(simulation)
        self.assertTrue(mock_main.called)

    @patch('builtins.input', side_effect=['2'])
    @patch('builtins.print')
    def test_handle_post_simulation_options_exit(self, mock_print, mock_input):
        field = Field(5, 5)
        simulation = Simulation(field)
        handle_post_simulation_options(simulation)
        mock_print.assert_any_call("Thank you for running the simulation. Goodbye!")

    @patch('builtins.input', side_effect=['3', '2'])
    @patch('builtins.print')
    def test_handle_post_simulation_options_invalid_option(self, mock_print, mock_input):
        field = Field(5, 5)
        simulation = Simulation(field)
        handle_post_simulation_options(simulation)
        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_any_call("Invalid option. Choose 1 or 2.")

    @patch('builtins.input', side_effect=['5 5', '1', 'Car1', '0 0 N', 'FFRFF', '2'])
    @patch('builtins.print')
    def test_main_add_car_and_run_simulation(self, mock_print, mock_input):
        try:
            main()
        except StopIteration:
            pass
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=['5 5', '1', 'Car1', '0 0 N', 'FFRFF', '1', 'Car2', '1 1 E', 'LFFR', '2'])
    @patch('builtins.print')
    def test_main_add_multiple_cars_and_run_simulation(self, mock_print, mock_input):
        try:
            main()
        except StopIteration:
            pass
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=['5 5', '3', '2'])
    @patch('builtins.print')
    def test_main_invalid_option(self, mock_print, mock_input):
        try:
            main()
        except StopIteration:
            pass
        self.assertTrue(mock_print.called)
        mock_print.assert_any_call("Invalid option. Choose 1 or 2.")

    @patch('builtins.input', side_effect=["0 0 N", "1 1 E"])
    @patch('builtins.print')
    def test_initial_position_collision(self, mock_print, mock_input):
        self.field = Field(5, 5)
        self.simulation = Simulation(self.field)
        self.car1 = Car("Car1", 0, 0, 'N')
        self.simulation.add_car(self.car1)
        x, y, direction = get_valid_car_position(self.simulation, "Car2")
        self.assertEqual((x, y, direction), (1, 1, 'E'))
        mock_print.assert_any_call("Position (0, 0) is already occupied by another car. Please choose a different position.")


if __name__ == '__main__':
    unittest.main()
