
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
        self.width = width
        self.height = height

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
