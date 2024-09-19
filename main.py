import logging
from src.field import Field
from src.car import Car
from src.simulation import Simulation

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
            width, height = map(int, input("Enter width and height in x y format: ").split())
            if width <= 0 or height <= 0:
                raise ValueError("Width and height must be positive integers.")
            return Field(width, height)
        except ValueError as ve:
            logger.error("Invalid input: %s", ve)
            print(f"Invalid input: {ve}")


def add_car(simulation):
    """
    Prompts the user to input car details and adds the car to the simulation.

    Parameters:
    -----------
    simulation : Simulation
        The simulation object to which the car will be added.
    """
    try:
        name = input("Enter the name of the car: ")
        x, y, direction = input(f"Enter position and direction of {name} in x y Direction format: ").split()
        x, y = int(x), int(y)
        if direction not in ['N', 'E', 'S', 'W']:
            raise ValueError("Direction must be N, E, S, W.")
        car = Car(name, x, y, direction)
        commands = input(f"Enter commands for {name}: ")
        car.set_commands(commands)
        simulation.add_car(car)
    except ValueError as ve:
        logger.error("Invalid input: %s", ve)
        print(f"Invalid input: {ve}")


def handle_post_simulation(simulation):
    """
    Handles the options after the simulation has run.

    Parameters:
    -----------
    simulation : Simulation
        The simulation object to reset or exit.
    """
    while True:
        option = input("Choose from:\n[1] Start over\n[2] Exit\nYour input: ")
        if option == '1':
            simulation.reset()
            main()  # Restart the main function
        elif option == '2':
            print("Thank you for running the simulation. Goodbye!")
            break
        else:
            logger.warning("Invalid option after simulation.")
            print("Invalid option. Exiting.")


def main():
    """
        Main function to run the car simulation.
    """

    print("Welcome to Auto Driving Car Simulation!")
    field = setup_field()
    simulation = Simulation(field)
    while True:
        option = input("Choose an option:\n[1] Add a car\n[2] Run simulation\nYour input: ")
        if option == '1':
            add_car(simulation)
        elif option == '2' and simulation.cars:
            simulation.run_simulation()
            break
        else:
            logger.warning("Invalid option.")
            print("Invalid option. Choose 1 or 2.")
    # Handle post-simulation options
    handle_post_simulation(simulation)


if __name__ == "__main__":
    main()
