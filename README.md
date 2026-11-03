# pecan-vision-workshop

This repository contains sample code, base models, and configuration guidance for deploying deep-learning computer vision algorithms in a pecan post-processing context as part of a workshop hosted by UGA Manufacturing Living Labs and the MODEL Group.

## Project foundation

This repository provides a minimal Python package scaffold for workshop participants to build on. It includes:

- a reusable workspace package: `pecan_vision_workshop/`
- a configuration loader and dataclass-based defaults
- a base model interface for computer-vision inference experiments
- example configuration guidance for pecan deployment workflows
- tests covering the initial project contract

## Quick start

```bash
python -m pip install -e .
python -m pytest
```

## Example usage

```python
from pecan_vision_workshop import WorkshopConfig, load_config

config = WorkshopConfig(model_name="demo-model", confidence_threshold=0.7)
print(config.model_name)

loaded = load_config("configs/example_config.yaml")
print(loaded.output_dir)
```

## Repository layout

- `pecan_vision_workshop/` — Python package scaffold
- `configs/` — example deployment settings
- `docs/` — configuration notes and guidance
- `tests/` — focused validation tests
