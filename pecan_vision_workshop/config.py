from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class WorkshopConfig:
    """Configuration for a workshop deployment pipeline."""

    model_name: str = "base-vision-model"
    input_shape: tuple[int, int] = (224, 224)
    confidence_threshold: float = 0.5
    preprocessing: dict[str, Any] = field(
        default_factory=lambda: {"normalize": True, "resize_mode": "bilinear"}
    )
    output_dir: str = "artifacts"

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "WorkshopConfig":
        return cls(
            model_name=payload.get("model_name", cls.model_name),
            input_shape=tuple(payload.get("input_shape", cls.input_shape)),
            confidence_threshold=float(
                payload.get("confidence_threshold", cls.confidence_threshold)
            ),
            preprocessing=payload.get("preprocessing", cls.preprocessing),
            output_dir=payload.get("output_dir", cls.output_dir),
        )


def load_config(path: str | Path) -> WorkshopConfig:
    """Load a configuration file from JSON or YAML.

    YAML support is optional and will be used when PyYAML is installed.
    """
    config_path = Path(path)
    text = config_path.read_text(encoding="utf-8")

    if config_path.suffix.lower() in {".json"}:
        return WorkshopConfig.from_dict(json.loads(text))

    try:
        import yaml  # type: ignore
    except ModuleNotFoundError as exc:  # pragma: no cover - depends on optional dependency
        raise RuntimeError(
            "YAML configuration requires PyYAML to be installed: pip install pyyaml"
        ) from exc

    return WorkshopConfig.from_dict(yaml.safe_load(text) or {})
