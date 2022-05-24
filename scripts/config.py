from pathlib import Path


class Config:
  RANDOM_SEED = 42
  ASSETS_PATH = Path("../")
  REPO = "D:\10 Academy\Test\Pharmaceutical-Sales-Prediction"
  DATASET_FILE_PATH = "data/AdSmartABdata.csv"
  DATASET_PATH = ASSETS_PATH / "data"
  FEATURES_PATH = ASSETS_PATH / "features"
  MODELS_PATH = ASSETS_PATH / "models"
  METRICS_FILE_PATH = ASSETS_PATH / "metrics"