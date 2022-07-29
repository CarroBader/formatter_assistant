#!/usr/bin/python3
from src.form_ass.modules.create_array import get_create_array
from src.form_ass.modules.create_dict import get_create_dict

import logging
import argparse
from argparse import ArgumentParser

logger = logging.getLogger(__name__)


def create_array():
    logger.info('Start creating array')
    description = '''Start creating array'''
    logger.info(description)
    parser = ArgumentParser(prog='create_array.py', description=description)
    parser.add_argument(
        '--variable_name', '-vn', required=True, help='Name of the finished array'
    )

    args = parser.parse_args()
    get_create_array(args.variable_name)
    logger.info('Done')


def create_dict():
    logger.info('Start creating dict')
    description = '''Start creating dict'''
    logger.info(description)
    parser = ArgumentParser(prog='create_dict.py', description=description)
    parser.add_argument(
        '--variable_name', '-vn', required=True, help='Name of the finished dict'
    )
    parser.add_argument(
        '--sorted_lists',
        '-sorted',
        '-s',
        default=False,
        action=argparse.BooleanOptionalAction,
    )

    args = parser.parse_args()
    get_create_dict(args.variable_name, args.sorted_lists)
    logger.info('Done')
