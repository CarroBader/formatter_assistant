#!/usr/bin/python3
''' Creates a array '''

import logging
import tempfile
import subprocess

# Local
from src.form_ass.common import helpers, constants

logger = logging.getLogger(__name__)


def get_create_array(variable_name: str):

    logger.info('Setting up variables')
    processed_data = []
    helpers.set_temp_dir_path()

    with tempfile.TemporaryDirectory(
        prefix='temp_dir_',
    ) as temp_dir:
        temp_file = tempfile.NamedTemporaryFile(
            prefix='temp_file_', dir=temp_dir, delete=False
        )

        # Open file
        temp_data_file = open(temp_file.name, 'w')

        logger.info('Open Vim')
        # Open file in vim
        subprocess.call(['vim', temp_file.name])

        # Close file
        temp_data_file.close()

        # Open file to read
        temp_data_file = open(temp_file.name, 'r+')

        for data_row in temp_data_file:
            processed_data.append(f"{data_row}".strip().replace('\n', ''))

        formatted_data = f'''{variable_name} = {processed_data}'''

        # Create and open file
        finishing_file = open(constants.PATH_NAME, 'w')

        logger.info('Writing the formatted data to file')
        # Write finishing_file to file
        finishing_file.write(formatted_data)

        # Close file
        finishing_file.close()
