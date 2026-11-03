from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class BaseVisionModel:
    """Base class for workshop image-processing models."""

    model_name: str = "base-vision-model"
    weights_path: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def predict(self, image: Any) -> Any:
        """Return a placeholder prediction for a new model implementation."""
        raise NotImplementedError(
            "Implement predict() in a concrete vision model for your pecan pipeline."
        )
