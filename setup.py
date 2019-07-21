# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='pokedex',  # Required
    version='1.0.0',  # Required
    packages=find_packages(),  # Required
    include_package_data=True,
    install_requires=[
        # "tabulate==0.8.2",
        # "Click==7.0",
    ],
    entry_points={  # Optional
        'console_scripts': [
            'pokedex=pokedex:run',
        ],
    },
)
