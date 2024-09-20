from .field import Field
from ..localize.localize import localizations
from ..config.config import Config
from ..utils.logger import Logger


class Car:
    """
    A class to represent a car in the simulation.

    Attributes:
    -----------
    name : str
        The name of the car.
    x : int
        The x-coordinate of the car's position.
    y : int
        The y-coordinate of the car's position.
    direction : str
        The direction the car is facing ('N', 'E', 'S', 'W').
    commands : list
        The list of commands for the car to execute.
    """
    DIRECTIONS = Config.CAR_DIRECTIONS

    def __init__(self, name: str, x: int, y: int, direction: str):
        """
        Constructs all the necessary attributes for the car object.

        Parameters:
        -----------
        name : str
            The name of the car.
        x : int
            The x-coordinate of the car's position.
        y : int
            The y-coordinate of the car's position.
        direction : str
            The direction the car is facing ('N', 'E', 'S', 'W').
        """
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = []
        self.logger = Logger.setup_logger('CAR')

    @staticmethod
    def validate_car_name(name: str, simulation):
        """
        Validates the car name.

        Parameters:
        -----------
        name : str
            The name of the car.
        simulation : Simulation
            The simulation object to check for duplicate names.

        Raises:
        -------
        ValueError
            If the name is not a valid string or is a duplicate.
        """
        logger = Logger.setup_logger('CAR')
        if not name or not isinstance(name, str) or len(name) < 1:
            logger.debug("Invalid car name: %s", name)
            print(localizations['invalid_car_name_error'])
            raise ValueError(localizations['invalid_car_name_error'])

        if any(existing_car.name == name for existing_car in simulation.cars):
            logger.debug("Car name '%s' is already in use. Choose a unique name.", name)
            print(localizations['duplicate_car_name_error'].format(name=name))
            raise ValueError(localizations['duplicate_car_name_error'].format(name=name))

    def set_commands(self, commands: str):
        """
        Sets the commands for the car.

        Parameters:
        -----------
        commands : str
            The commands for the car to execute.

        Raises:
        -------
        ValueError
            If the commands contain invalid characters.
        """
        if not all(c in 'LRF' for c in commands):
            self.logger.debug("Invalid commands: %s", commands)
            raise ValueError(localizations['invalid_command_error'])
        self.commands = commands

    def turn_left(self):
        """Turns the car to the left."""
        current_idx = Car.DIRECTIONS.index(self.direction)
        self.direction = Car.DIRECTIONS[(current_idx - 1) % 4]

    def turn_right(self):
        """Turns the car to the right."""
        current_idx = Car.DIRECTIONS.index(self.direction)
        self.direction = Car.DIRECTIONS[(current_idx + 1) % 4]

    def move_forward(self, field: Field):
        """
        Moves the car forward in the direction it is facing.

        Parameters:
        -----------
        field : Field
            The field in which the car is moving.
        """
        if self.direction == 'N' and field.is_within_boundaries(self.x, self.y + 1):
            self.y += 1
        elif self.direction == 'E' and field.is_within_boundaries(self.x + 1, self.y):
            self.x += 1
        elif self.direction == 'S' and field.is_within_boundaries(self.x, self.y - 1):
            self.y -= 1
        elif self.direction == 'W' and field.is_within_boundaries(self.x - 1, self.y):
            self.x -= 1
        else:
            self.logger.debug("Move out of field boundaries for car %s", self.name)
