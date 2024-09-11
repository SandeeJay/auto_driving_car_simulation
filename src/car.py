import logging
from src.field import Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
    DIRECTIONS = ['N', 'E', 'S', 'W']

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
        self._validate_car_name(name)
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = []

    @staticmethod
    def _validate_car_name(name: str):
        """
        Validates the car name.

        Parameters:
        -----------
        name : str
            The name of the car.

        Raises:
        -------
        ValueError
            If the name is not a valid string.
        """
        if not name or not isinstance(name, str):
            logger.error("Invalid car name: %s", name)
            raise ValueError("Car must have a valid name.")

    def set_commands(self, commands: str):
        """
        Sets the commands for the car.

        Parameters:
        -----------
        commands : str
            The commands for the car to execute.
        """
        if not all(c in 'LRF' for c in commands):
            logger.error("Invalid commands: %s", commands)
            raise ValueError("Commands must be a combination of 'L', 'R', and 'F'.")
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
            logger.error("Move out of field boundaries for car %s", self.name)
            raise ValueError("Move out of field boundaries.")
