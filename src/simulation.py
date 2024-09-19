import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Simulation:
    """
    Represents the simulation of cars on a field.

    Attributes:
    -----------
    field : Field
        The field on which the simulation runs.
    cars : list
        List of cars in the simulation.
    stopped_cars : set
        Set of cars that have stopped.
    collisions : dict
        Dictionary of collisions that occurred during the simulation.
    boundary_collisions : dict
        Dictionary of boundary collisions that occurred during the simulation.
    """

    def __init__(self, field):
        """
        Initializes the Simulation with a field.

        Parameters:
        -----------
        field : Field
            The field on which the simulation runs.
        """
        self.field = field
        self.cars = []
        self.stopped_cars = set()
        self.collisions = {}
        self.boundary_collisions = {}

    def add_car(self, car):
        """
        Adds a car to the simulation.

        Parameters:
        -----------
        car : Car
            The car to be added to the simulation.

        Raises:
        -------
        ValueError
            If a car with the same name already exists in the simulation.
        """
        if any(existing_car.name == car.name for existing_car in self.cars):
            error_message = f"Car name '{car.name}' is already in use. Choose a unique name."
            logger.error(error_message)
            raise ValueError(error_message)
        self.cars.append(car)

    def reset(self):
        """
        Resets the simulation by clearing all cars, stopped cars, collisions, and boundary collisions.
        """
        self.cars = []
        self.stopped_cars = set()
        self.collisions = {}
        self.boundary_collisions = {}

    def run_simulation(self):
        """
        Runs the simulation by processing each step and checking for collisions.
        """
        self.display_initial_car_positions()
        max_steps = max((len(car.commands) for car in self.cars), default=0)
        for step in range(max_steps):
            self.process_step(step)
        self.display_final_results()

    def process_step(self, step):
        """
        Processes a single step of the simulation.

        Parameters:
        -----------
        step : int
            The current step of the simulation.
        """
        for car in self.cars:
            if car.name in self.stopped_cars:
                continue
            if step < len(car.commands):
                self.execute_car_command(car, step)
        self.check_collisions(step)

    def execute_car_command(self, car, step):
        """
        Executes a command for a car at a given step.

        Parameters:
        -----------
        car : Car
            The car for which the command is executed.
        step : int
            The current step of the simulation.
        """
        command = car.commands[step]
        previous_position = (car.x, car.y)
        if command == 'L':
            car.turn_left()
        elif command == 'R':
            car.turn_right()
        elif command == 'F':
            car.move_forward(self.field)
            if (car.x, car.y) == previous_position:
                self.stopped_cars.add(car.name)
                self.boundary_collisions[car.name] = step

    def check_collisions(self, step):
        """
        Checks for collisions between cars at the current step.

        Parameters:
        -----------
        step : int
            The current step of the simulation.
        """
        positions = {}
        for car in self.cars:
            if car.name not in self.stopped_cars:
                position = (car.x, car.y)
                if position in positions:
                    other_car_name = positions[position]
                    self.report_collision(car.name, other_car_name, position, step)
                positions[position] = car.name

    def report_collision(self, car1, car2, pos, step):
        """
        Reports a collision between two cars.

        Parameters:
        -----------
        car1 : str
            The name of the first car involved in the collision.
        car2 : str
            The name of the second car involved in the collision.
        pos : tuple
            The position where the collision occurred.
        step : int
            The step at which the collision occurred.
        """
        logger.warning("Collision: %s and %s at %s at step %d", car1, car2, pos, step)
        self.collisions[step] = (car1, car2, pos)
        self.stopped_cars.update({car1, car2})

    def display_initial_car_positions(self):
        """
        Displays the initial positions of all cars in the simulation.
        """
        print("Your current list of cars are:")
        for car in self.cars:
            print(f"- {car.name}, ({car.x}, {car.y}), {car.direction},  {car.commands}")

    def display_final_results(self):
        """
        Displays the final results of the simulation, including collisions and final positions of cars.
        """
        print("After simulation, the result is:")
        for step, (car1, car2, pos) in self.collisions.items():
            print(f"- Step {step}: {car1} collides with {car2} at {pos}")
        for car in self.cars:
            if car.name in self.stopped_cars:
                print(f"- {car.name} stopped at ({car.x}, {car.y})")
            else:
                print(f"- {car.name} , ({car.x}, {car.y}), {car.direction}")

