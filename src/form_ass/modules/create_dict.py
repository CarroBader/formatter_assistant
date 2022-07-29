#!/usr/bin/python3
''' Creates a dict from two lists '''

import logging
import tempfile
import subprocess

# Local
from src.form_ass.common import helpers, constants

logger = logging.getLogger(__name__)


def get_create_dict(
    variable_name: str,
    sorted_lists: bool,
):
    logger.info('Setting up variables')
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

        # Alternatives based on what the data looks like, is choosen in the menu
        if sorted_lists:
            formatted_data = format_sorted_lists(temp_data_file, variable_name)

        # Create and open file
        finishing_file = open(constants.PATH_NAME, 'w')

        logger.info('Writing the formatted data to file')
        # Write finishing_file to file
        finishing_file.write(formatted_data)

        # Close file
        finishing_file.close()


def format_sorted_lists(unread_data: list, variable_name: str) -> str:
    unformated_dict = {}
    key_data = []
    value_data = []

    data_content = unread_data.readlines()

    i = 0
    for data_row in data_content:
        # Seperate the two lists with the blank row
        if data_row == '\n':
            i += 1
            continue

        # The top list becomes the key
        if i % 2 == 0:
            key_data.append(f"{data_row}".strip())
        # The bottom list becomes the value
        elif i % 2 == 1:
            value_data.append(f"{data_row}".strip())

    # Zip the lists to a dict
    unformated_dict = dict(zip(key_data, value_data))

    formatted_data = f'''{variable_name} = {unformated_dict}'''

    return formatted_data
