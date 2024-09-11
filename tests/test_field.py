import pytest
from src.field import Field


def test_field_initialization():
    """
    Test the initialization of a Field object.
    """
    field = Field(5, 5)
    assert field.width == 5
    assert field.height == 5


def test_is_within_boundaries():
    """
    Test the is_within_boundaries method of the Field class.
    """
    field = Field(5, 5)
    assert field.is_within_boundaries(0, 0) == True
    assert field.is_within_boundaries(5, 5) == False
    assert field.is_within_boundaries(-1, 0) == False
    assert field.is_within_boundaries(0, -1) == False
