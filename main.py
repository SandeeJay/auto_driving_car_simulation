import logging
from src.field import Field
from src.car import Car
from src.simulation import Simulation

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Main function to run the car simulation."""
    while True:
        print("Welcome to Auto Driving Car Simulation!")

        # Input for field dimensions
        try:
            width, height = map(int, input("Please enter the width and height of the simulation field in x y format: ").split())
            if width <= 0 or height <= 0:
                raise ValueError("Width and height must be positive integers.")
        except ValueError as ve:
            logger.error("Invalid input for field dimensions: %s", ve)
            print(f"Invalid input for field dimensions: {ve}")
            continue

        field = Field(width, height)
        print(f"You have created a field of {width} x {height}.\n")

        simulation = Simulation(field)

        while True:
            option = input("Please choose from the following options:\n[1] Add a car to field\n[2] Run simulation\nYour input: ")
            if option == '1':
                try:
                    name = input("Please enter the name of the car: ")
                    x, y, direction = input(f"Please enter initial position of car {name} in x y Direction format: ").split()
                    x, y = int(x), int(y)
                    if direction not in ['N', 'E', 'S', 'W']:
                        raise ValueError("Direction must be one of 'N', 'E', 'S', 'W'.")
                    car = Car(name, x, y, direction)
                    commands = input(f"Please enter the commands for car {name}: ")
                    car.set_commands(commands)
                    simulation.add_car(car)
                except ValueError as ve:
                    logger.error("Invalid input for car details: %s", ve)
                    print(f"Invalid input for car details: {ve}")
            elif option == '2':
                if not simulation.cars:
                    logger.warning("No cars added to the simulation.")
                    print("No cars added to the simulation. Please add at least one car.")
                    continue
                simulation.run_simulation()
                break
            else:
                logger.warning("Invalid option selected: %s", option)
                print("Invalid option. Please choose either '1' or '2'.")

        # Post-simulation options
        option_after_simulation = input("Please choose from the following options:\n[1] Start over\n[2] Exit\nYour input: ")
        if option_after_simulation == '1':
            simulation.reset()  # Reset the simulation
        elif option_after_simulation == '2':
            print("Thank you for running the simulation. Goodbye!")
            break
        else:
            logger.warning("Invalid option selected after simulation: %s", option_after_simulation)
            print("Invalid option. Exiting the simulation.")
            break


if __name__ == "__main__":
    main()

