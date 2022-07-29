#!/usr/bin/python3
''' Helper functions '''

import logging
import tempfile

# Local
from src.form_ass.common import constants

logger = logging.getLogger(__name__)


def set_temp_dir_path():
    tempfile.tempdir = constants.CURRENT_FOLDER_PATH
