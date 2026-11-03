# Configuration guidance

This repository is designed as a foundation for deploying computer-vision models in a pecan post-processing pipeline. Use the configuration files in the `configs/` directory as a starting point for workshop deployments.

## Recommended structure

- `configs/example_config.yaml` for environment-specific settings
- `pecan_vision_workshop/config.py` for configuration validation and loading
- `pecan_vision_workshop/model.py` for model interfaces and inference hooks

## Example settings

The example configuration includes:

- the model name
- expected image input shape
- confidence threshold for post-processing decisions
- preprocessing steps such as resize and normalization
- the artifact output directory

## Deployment notes

1. Keep model weights outside version control when they are large.
2. Add deployment-specific values in a local config file instead of editing tracked defaults.
3. Validate your input size and threshold values before running inference on pecan images.
4. Write trained model artifacts to a dedicated output directory for reproducibility.
