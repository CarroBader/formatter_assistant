from importlib.metadata import entry_points
from setuptools import setup, find_packages

PACKAGE_NAME = 'form_ass'
SOURCE_DIRECTORY = 'src'

setup(
    name=PACKAGE_NAME,
    packages=find_packages(),
    version='0.1',
    include_package_data=True,
    entry_points='''
    [console_scripts]
    create_array=src.form_ass.main:create_array
    create_dict=src.form_ass.main:create_dict
        ''',
)
