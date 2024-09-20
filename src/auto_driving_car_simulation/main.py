from .simulation.field import Field
from .simulation.car import Car
from .simulation.simulation import Simulation
from .localize.localize import localizations
from .config.config import Config
from .utils.logger import Logger


logger = Logger.setup_logger('MAIN')


def setup_field():
    """
    Prompts the user to input the dimensions of the field and returns a Field object.

    Returns:
    --------
    Field
        The field object with the specified dimensions.
    """
    while True:
        try:
            width, height = map(int, input(localizations['input_dimensions_prompt']).split())
            if width <= 0 or height <= 0:
                print(localizations['invalid_dimensions_error'])
                continue
            print(localizations['field_setup_success'].format(width=width, height=height))
            return Field(width, height)
        except ValueError as ve:
            logger.debug("Invalid input: %s", ve)
            print(localizations['invalid_dimensions_error'])


def add_car_to_simulation(simulation):
    """
    Prompts the user to input car details and adds the car to the simulation.

    Parameters:
    -----------
    simulation : Simulation
        The simulation object to which the car will be added.
    """
    name = get_valid_car_name(simulation)
    x, y, direction = get_valid_car_position(simulation, name)
    commands = get_valid_car_commands(name)
    car = Car(name, x, y, direction)
    car.set_commands(commands)
    simulation.add_car(car)
    simulation.display_initial_car_positions()

def get_valid_car_name(simulation: Simulation):
    """
    Prompts the user to input a valid car name.

    Parameters:
    -----------
    simulation : Simulation
        The simulation object to check for duplicate names.

    Returns:
    --------
    str
        The valid car name.
    """
    while True:
        try:
            name = input(localizations['car_name_prompt']).strip()
            Car.validate_car_name(name, simulation)
            return name
        except ValueError:
            continue


def get_valid_car_position(simulation, name: str):
    """
    Prompts the user to input valid car position and direction.

    Parameters:
    -----------
    simulation : Simulation
        The simulation object to check the field boundaries.
    name : str
        The name of the car.

    Returns:
    --------
    tuple
        The x-coordinate, y-coordinate, and direction of the car.
    """
    while True:
        try:
            x, y, direction = input(localizations['car_position_prompt'].format(name=name)).split()
            x, y = int(x), int(y)
            if x < 0 or y < 0:
                print(localizations['invalid_coordinates_error'])
                continue
            if direction not in Config.CAR_DIRECTIONS:
                print(localizations['invalid_direction_error'])
                continue
            if not simulation.field.is_within_boundaries(x, y):
                print(localizations['out_of_bounds_error'])
                continue
            return x, y, direction
        except ValueError:
            print(localizations['invalid_input_error'])
            continue


def get_valid_car_commands(name: str):
    """
    Prompts the user to input valid car commands.

    Parameters:
    -----------
    name : str
        The name of the car.

    Returns:
    --------
    str
        The valid commands for the car.
    """
    while True:
        try:
            commands = input(localizations['commands_prompt'].format(name=name))
            if not all(c in Config.CAR_COMMANDS for c in commands):
                raise ValueError(localizations['invalid_command_error'])
            return commands
        except ValueError:
            print(localizations['invalid_command_error'])
            continue


def handle_post_simulation_options(simulation: Simulation):
    """
    Handles the options after the simulation has run.


    Parameters:
    -----------
    simulation : Simulation
        The simulation object to reset or exit.
    """
    while True:
        option = input(localizations['post_simulation_prompt'])
        if option == '1':
            simulation.reset()
            main()  # Restart the main function
        elif option == '2':
            print(localizations['exit_message'])
            break
        else:
            logger.debug("Invalid option after simulation.")
            print(localizations['invalid_option_warning'])


def main():
    """
    Main function to run the car simulation.
    """
    print(localizations['welcome_message'])
    field = setup_field()
    simulation = Simulation(field)
    while True:
        option = input(localizations['simulation_option_prompt'])
        if option == '1':
            add_car_to_simulation(simulation)
        elif option == '2':
            if simulation.cars:
                simulation.run_simulation()
                break
            else:
                print(localizations['no_cars_error'])
                continue
        else:
            logger.debug("Invalid option.")
            print(localizations['invalid_option_warning'])
    handle_post_simulation_options(simulation)


if __name__ == "__main__":
    main()
