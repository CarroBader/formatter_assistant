#!/usr/bin/python3
''' Helper functions '''

import logging
import tempfile

# Local
from src.form_ass.common import constants

logger = logging.getLogger(__name__)


def set_temp_dir_path():
    # Sets tempdir to the folders path
    tempfile.tempdir = constants.CURRENT_FOLDER_PATH


def create_dict(key_data: list, value_data: list) -> dict:
    # Zip the lists to a dict
    return dict(zip(key_data, value_data))
