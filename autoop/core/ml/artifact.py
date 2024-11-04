from pydantic import BaseModel
from typing import Optional
import base64


class Artifact(BaseModel):
    """Represents a machine learning artifact with associated metadata and data.

    The `Artifact` class encapsulates the details of a machine learning artifact,
    including its name, version, asset path, binary data, metadata, type, and tags.
    It provides properties to access and modify these attributes,
    ensuring data integrity and consistency.

    Attributes:
        name (str): The name of the artifact.
        _version (str): The version of the artifact. Defaults to "1.0.0".
        _asset_path (str): The file system path where the artifact is stored.
        _data (bytes): The binary data of the artifact.
        metadata (Optional[dict]): Additional metadata associated with the artifact.
        type (str): The type/category of the artifact.
        tags (Optional[list]): A list of tags associated with the artifact.
    """

    name: str
    _version: str = "1.0.0"
    _asset_path: str
    _data: bytes
    metadata: Optional[dict] = {}
    type: str
    tags: Optional[list] = []

    def __init__(self, **data) -> None:
        """Initializes a new instance of the Artifact class.

        This constructor initializes the `Artifact` instance by setting up its
        attributes based on the provided data. It ensures that private attributes
        such as `_asset_path`, `_data`, and `_version` are properly initialized.

        Args:
            **data: Arbitrary keyword arguments corresponding
            to the artifact's attributes.

        Raises:
            ValueError: If required attributes are missing or invalid.
        """
        super().__init__(**data)
        # Initialize private attributes
        self._asset_path = data.get('asset_path')
        self._data = data.get('data')
        self._version = data.get('version', "1.0.0")

    @property
    def asset_path(self) -> str:
        """Gets the asset path.

        Returns:
            str: The path where the artifact is stored.
        """
        return self._asset_path

    @property
    def version(self) -> str:
        """Gets the version of the artifact.

        Returns:
            str: The version string.
        """
        return self._version

    @version.setter
    def version(self, new_version: str) -> None:
        """Sets a new version for the artifact.

        Args:
            new_version (str): The new version string.

        Raises:
            ValueError: If the new_version format is invalid.
        """
        if not isinstance(new_version, str) or not new_version:
            raise ValueError("Version must be a non-empty string.")
        self._version = new_version

    @property
    def id(self) -> str:
        """Generates a unique ID for the artifact.

        The ID is a base64-encoded string combining the asset path and version.

        Returns:
            str: A base64 encoded ID based on asset_path and version.
        """
        encoded_path = base64.urlsafe_b64encode(
            self._asset_path.encode()
        ).decode()
        return f"{encoded_path}:{self._version}"

    def read(self) -> bytes:
        """Returns the data of the artifact.

        Returns:
            bytes: The data stored in the artifact.
        """
        return self._data

    def save(self, data: bytes) -> None:
        """Updates the artifact's data.

        Args:
            data (bytes): The new data to be saved.
        """
        self._data = data
