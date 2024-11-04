import pytest
from autoop.core.ml.artifact import Artifact
import base64


@pytest.fixture
def artifact() -> Artifact:
    """Fixture to create a test Artifact instance.

    This fixture initializes an Artifact object with predefined attributes
    that can be used across multiple test functions.

    Returns:
        Artifact: An instance of the Artifact class with test data.
    """
    return Artifact(
        name="test_artifact",
        asset_path="path/to/asset",
        data=b"test_data",
        metadata={"key": "value"},
        type="test_type",
        tags=["tag1", "tag2"]
    )


def test_id_generation(artifact:Artifact) -> None:
    """Test the generation of the Artifact's unique ID.

    This test verifies that the Artifact's `id` property correctly encodes
    the asset path and appends the version, ensuring the ID follows the expected format.

    Args:
        artifact (Artifact): The Artifact instance provided by the fixture.

    Raises:
        AssertionError: If the generated ID does not match the expected value.
    """
    encoded_path = base64.urlsafe_b64encode(
        artifact.asset_path.encode()
    ).decode()
    expected_id = f"{encoded_path}:{artifact.version}"
    assert artifact.id == expected_id, \
        "Artifact ID does not match the expected value."


def test_read(artifact:Artifact) -> None:
    """Test the read method of the Artifact.

    This test ensures that the `read` method returns the correct binary data
    stored within the Artifact.

    Args:
        artifact (Artifact): The Artifact instance provided by the fixture.

    Raises:
        AssertionError: If the read data does not match the expected value.
    """
    assert artifact.read() == b"test_data", \
        "Read method did not return the correct data."


def test_save(artifact:Artifact) -> None:
    """Test the save method of the Artifact.

    This test verifies that the `save` method correctly updates the Artifact's
    data and that the updated data can be retrieved accurately.

    Args:
        artifact (Artifact): The Artifact instance provided by the fixture.

    Raises:
        AssertionError: If the data is not updated correctly after saving.
    """
    new_data = b"new_test_data"
    artifact.save(new_data)
    assert artifact.read() == new_data, \
        "Save method did not update the data correctly."


def test_version_getter(artifact:Artifact) -> None:
    """Test the version getter of the Artifact.

    This test checks that the `version` property returns the correct initial version.

    Args:
        artifact (Artifact): The Artifact instance provided by the fixture.

    Raises:
        AssertionError: If the version does not match the expected value.
    """
    assert artifact.version == "1.0.0", \
        "Version getter did not return the correct version."


def test_version_setter_valid(artifact:Artifact) -> None:
    """Test setting a valid version for the Artifact.

    This test ensures that setting a new valid version updates the Artifact's
    version property and that the `id` property reflects this change.

    Args:
        artifact (Artifact): The Artifact instance provided by the fixture.

    Raises:
        AssertionError: If the version or ID does not update correctly.
    """
    new_version = "2.0.0"
    artifact.version = new_version
    assert artifact.version == new_version, \
        "Version setter did not update the version correctly."
    # Check if id is updated accordingly
    encoded_path = base64.urlsafe_b64encode(
        artifact.asset_path.encode()
    ).decode()
    expected_id = f"{encoded_path}:{new_version}"
    assert artifact.id == expected_id, \
        "Artifact ID did not update after version change."


def test_version_setter_invalid(artifact:Artifact) -> None:
    """Test setting an invalid version for the Artifact.

    This test verifies that setting an invalid version (empty string or non-string)
    raises a `ValueError`.

    Args:
        artifact (Artifact): The Artifact instance provided by the fixture.

    Raises:
        pytest.raises(ValueError): If the version is set to an invalid value.
    """
    with pytest.raises(ValueError):
        artifact.version = ""
    with pytest.raises(ValueError):
        artifact.version = 123  # Not a string
