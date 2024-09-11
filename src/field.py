import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Field:
    """
    A class to represent the field in the simulation.

    Attributes:
    -----------
    width : int
        The width of the field.
    height : int
        The height of the field.
    """

    def __init__(self, width: int, height: int):
        """
        Constructs all the necessary attributes for the field object.

        Parameters:
        -----------
        width : int
            The width of the field.
        height : int
            The height of the field.
        """
        self._validate_field_dimensions(width, height)
        self.width = width
        self.height = height

    @staticmethod
    def _validate_field_dimensions(width: int, height: int):
        """
        Validates the field dimensions.

        Parameters:
        -----------
        width : int
            The width of the field.
        height : int
            The height of the field.

        Raises:
        -------
        ValueError
            If the width or height is not a positive integer.
        """
        if width <= 0 or height <= 0:
            logger.error("Invalid field dimensions: width=%d, height=%d", width, height)
            raise ValueError("Width and height must be positive integers.")

    def is_within_boundaries(self, x: int, y: int) -> bool:
        """
        Checks if the given coordinates are within the field boundaries.

        Parameters:
        -----------
        x : int
            The x-coordinate to check.
        y : int
            The y-coordinate to check.

        Returns:
        --------
        bool
            True if the coordinates are within boundaries, False otherwise.
        """
        within_boundaries = 0 <= x < self.width and 0 <= y < self.height
        return within_boundaries

