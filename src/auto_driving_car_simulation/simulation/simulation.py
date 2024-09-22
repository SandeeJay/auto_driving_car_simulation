from ..localize.localize import localizations
from ..utils.logger import Logger
from .car import Car


class Simulation:
    """
    Represents the simulation of cars on a field.

    Attributes:
    -----------
    field : Field
        The field on which the simulation runs.
    cars : list
        The list of cars in the simulation.
    stopped_cars : set
        The set of cars that have stopped.
    collisions : dict
        The dictionary of collisions with step as key and (cars, position) as value.
    boundary_collisions : dict
        The dictionary of boundary collisions with car name as key and steps as value.
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
        self.logger = Logger.setup_logger('Simulation')

    def add_car(self, car: Car):
        """
        Adds a car to the simulation.

        Parameters:
        -----------
        car : Car
            The car to be added to the simulation.
        """
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

    def process_step(self, step: int):
        """
        Processes a single step of the simulation.

        Parameters:
        -----------
        step : int
            The current step of the simulation.
        """
        for car in self.cars:
            self.check_collisions(step)
            if car.name in self.stopped_cars:
                continue
            if step < len(car.commands):
                self.execute_car_command(car, step)
                self.check_collisions(step)

    def execute_car_command(self, car: Car, step: int):
        """
        Executes a command for a car at a given step.

        Parameters:
        -----------
        car : Car
            The car to execute the command.
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
                if car.name in self.boundary_collisions:
                    self.boundary_collisions[car.name].append(step + 1)
                else:
                    self.boundary_collisions[car.name] = [step + 1]
                self.stopped_cars.add(car.name)

    def check_collisions(self, step: int):
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
                    positions[position].append(car.name)
                else:
                    positions[position] = [car.name]

        for position, cars in positions.items():
            if len(cars) > 1:
                self.report_collision(cars, position, step)

    def report_collision(self, cars: list, pos: tuple, step: int):
        """
        Reports a collision between two cars.

        Parameters:
        -----------
        cars : list
            The list of cars involved in the collision.
        pos : tuple
            The position of the collision.
        step : int
            The step at which the collision occurred.
        """
        self.logger.debug("Collision: %s at %s at step %d", ', '.join(cars), pos, step + 1)
        self.collisions[step + 1] = (cars, pos)
        self.stopped_cars.update(cars)

    def display_initial_car_positions(self):
        """
        Displays the initial positions of all cars in the simulation.
        """
        print(localizations['current_car_list'])
        for car in self.cars:
            print(f"- {car.name}, ({car.x}, {car.y}), {car.direction},  {car.commands}")

    def display_final_results(self):
        """
        Displays the final results of the simulation, including collisions and final positions of cars.
        """
        print(localizations['simulation_results'])

        collision_names = set()
        for step, (cars, pos) in self.collisions.items():
            for car in cars:
                print(localizations['collides_with_car'].format(step=step, car1=car,
                                                                car2=', '.join(c for c in cars if c != car), pos=pos))
                collision_names.add(car)

        for car in self.cars:
            if car.name not in collision_names:
                if car.name in self.boundary_collisions:
                    steps = self.boundary_collisions[car.name]
                    print(localizations['out_of_bounds_warning'].format(car=car.name, x=car.x, y=car.y,
                                                                        direction=car.direction,
                                                                        step=', '.join(str(c) for c in steps)))
                else:
                    print(f"- {car.name} , ({car.x}, {car.y}), {car.direction}")
