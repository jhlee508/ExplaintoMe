"""
Paths to data, paths to saved models should be saved here
"""
from pathlib import Path
from os import path

# the directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = path.join(PROJECT_ROOT, "data")
SAVED_DIR = path.join(DATA_DIR, "saved")


# the files.
REVDICT_DATASET_TSV = path.join(DATA_DIR, "revdict_dataset_ver2.tsv")


# the models
MONO_EN_CKPT = path.join(DATA_DIR, "lightning_logs/version_1/checkpoints/mono_en_epoch=05_train_loss=0.00.ckpt") ### Change Checkpoint file
CROSS_CKPT = path.join(DATA_DIR, "lightning_logs/version_0/checkpoints/cross_epoch=27_train_loss=0.64.ckpt")
