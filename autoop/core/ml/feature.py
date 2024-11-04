from typing import Literal

import numpy as np
from pydantic import BaseModel, Field

from autoop.core.ml.dataset import Dataset


class Feature(BaseModel):
    """
    Represents a feature (column) in a dataset.

    Attributes:
        name (str): The name of the feature. Must be a non-empty string.
        type (Literal['categorical', 'numerical']): The type of the feature.
    """
    name: str = Field(..., min_length=1)
    type: Literal['categorical', 'numerical']

    def __str__(self) -> str:
        """
        Returns a string representation of the Feature.

        Returns:
            str: The string representation.
        """
        return f"Feature(name='{self.name}', type='{self.type}')"
