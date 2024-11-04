import pytest

from autoop.core.ml.feature import Feature


@pytest.fixture
def feature() -> Feature:
    """
    Fixture to create a sample Feature instance for testing.
    """
    return Feature(name="age", type="numerical")

def test_feature_creation(feature:Feature) -> None:
    """
    Test that a Feature instance is created with correct attributes.
    """
    assert feature.name == "age", "Feature name was not set correctly."
    assert feature.type == "numerical", "Feature type was not set correctly."

def test_feature_str(feature:Feature) -> None:
    """
    Test the __str__ method of the Feature class.
    """
    expected_str = "Feature(name='age', type='numerical')"
    assert str(feature) == expected_str, \
        "Feature __str__ method does not match expected output."

def test_feature_invalid_type() -> None:
    """
    Test that creating a Feature with an invalid type raises a ValueError.
    """
    with pytest.raises(ValueError):
        Feature(name="gender", type="invalid_type")

def test_feature_empty_name() -> None:
    """
    Test that creating a Feature with an empty name raises a ValueError.
    """
    with pytest.raises(ValueError):
        Feature(name="", type="categorical")
