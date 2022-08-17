#!/usr/bin/python3
''' Helper functions '''
import os
from dotenv import load_dotenv
import logging
import tempfile

load_dotenv()
CURRENT_FOLDER_PATH = os.getenv("current_folder_path")

logger = logging.getLogger(__name__)


def set_temp_dir_path():
    # Sets tempdir to the folders path
    tempfile.tempdir = CURRENT_FOLDER_PATH


def create_dict(key_data: list, value_data: list) -> dict:
    # Zip the lists to a dict
    return dict(zip(key_data, value_data))
