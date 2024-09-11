import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Simulation:
    """
    A class to represent the simulation of cars on a field.

    Attributes:
    -----------
    field : Field
        The field on which the simulation is run.
    cars : list
        The list of cars in the simulation.
    stopped_cars : set
        The set of cars that have stopped due to collisions.
    collisions : dict
        The dictionary of collisions that occurred during the simulation.
    """

    def __init__(self, field):
        """
        Constructs all the necessary attributes for the simulation object.

        Parameters:
        -----------
        field : Field
            The field on which the simulation is run.
        """
        self.field = field
        self.cars = []
        self.stopped_cars = set()  # Cars stopped due to collision or boundary
        self.collisions = {}  # Car-to-car collisions
        self.boundary_collisions = {}  # Keep track of cars that hit the boundary with step info

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
            logger.error("Car name '%s' is already in use.", car.name)
            raise ValueError(f"Car name '{car.name}' is already in use. Please choose a unique name.")
        self.cars.append(car)

    def reset(self):
        """Resets the simulation for a new run."""
        self.cars = []
        self.stopped_cars = set()
        self.collisions = {}
        self.boundary_collisions = {}

    def show_car_list_with_commands(self):
        """Displays the list of cars with their commands."""
        print("Your current list of cars are:")
        for car in self.cars:
            print(f"- {car.name}, ({car.x}, {car.y}), {car.direction}, {car.commands}")

    def show_car_list_after_simulation(self):
        """Displays the list of cars after the simulation."""
        print("After simulation, the result is:")
        if self.collisions:
            for step, (car1, car2, pos) in self.collisions.items():
                print(f"- {car1} collides with {car2} at {pos} at step {step}")
        for car in self.cars:
            if car.name in self.boundary_collisions:
                step = self.boundary_collisions[car.name]
                print(f"- {car.name} stopped at ({car.x}, {car.y}) due to hitting the field boundary at step {step}.")
            else:
                print(f"- {car.name} , ({car.x}, {car.y}), {car.direction}")

    def report_collision(self, car1, car2, pos, step):
        """
        Reports a collision between two cars.

        Parameters:
        -----------
        car1 : str
            The name of the first car.
        car2 : str
            The name of the second car.
        pos : tuple
            The position where the collision occurred.
        step : int
            The step at which the collision occurred.
        """
        self.collisions[step] = (car1, car2, pos)
        logger.warning("Collision reported: %s and %s at %s at step %d", car1, car2, pos, step)

    def check_collisions(self, step):
        """
        Checks for collisions between cars.

        Parameters:
        -----------
        step : int
            The current step of the simulation.
        """
        positions = {}
        for car in self.cars:
            if car.name not in self.stopped_cars:
                pos = (car.x, car.y)
                if pos in positions:
                    other_car = positions[pos]
                    self.report_collision(car.name, other_car, pos, step)
                    self.stopped_cars.add(car.name)
                    self.stopped_cars.add(other_car)
                else:
                    positions[pos] = car.name

    def run_simulation(self):
        """Runs the simulation."""
        self.show_car_list_with_commands()
        max_steps = max(len(car.commands) for car in self.cars)
        for step in range(max_steps):
            for car in self.cars:
                if car.name in self.stopped_cars:
                    continue
                if step < len(car.commands):
                    command = car.commands[step]
                    if command == 'L':
                        car.turn_left()
                    elif command == 'R':
                        car.turn_right()
                    elif command == 'F':
                        previous_x, previous_y = car.x, car.y
                        try:
                            car.move_forward(self.field)
                            # Check if the car has hit the boundary
                            if car.x == previous_x and car.y == previous_y:
                                self.stopped_cars.add(car.name)
                                self.boundary_collisions[car.name] = step + 1
                        except ValueError as ve:
                            logger.error("Error moving car %s: %s", car.name, ve)
            self.check_collisions(step + 1)
        self.show_car_list_after_simulation()
