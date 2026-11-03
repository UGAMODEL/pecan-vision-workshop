import json
import tempfile
import unittest
from pathlib import Path

from pecan_vision_workshop import BaseVisionModel, WorkshopConfig, __version__, load_config


class TestWorkshopFoundation(unittest.TestCase):
    def test_package_exports(self):
        self.assertEqual(__version__, "0.1.0")
        self.assertTrue(issubclass(BaseVisionModel, object))
        self.assertTrue(hasattr(WorkshopConfig, "from_dict"))

    def test_load_config_from_json(self):
        payload = {
            "model_name": "demo-model",
            "input_shape": [256, 256],
            "confidence_threshold": 0.75,
            "preprocessing": {"normalize": False, "resize_mode": "nearest"},
            "output_dir": "demo-artifacts",
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"
            config_path.write_text(json.dumps(payload), encoding="utf-8")

            config = load_config(config_path)

        self.assertEqual(config.model_name, "demo-model")
        self.assertEqual(config.input_shape, (256, 256))
        self.assertEqual(config.confidence_threshold, 0.75)
        self.assertEqual(config.output_dir, "demo-artifacts")

    def test_model_contract(self):
        model = BaseVisionModel(model_name="stub-model")
        with self.assertRaises(NotImplementedError):
            model.predict("sample-image")


if __name__ == "__main__":
    unittest.main()
