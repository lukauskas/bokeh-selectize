from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='bokehselectize',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1',

    description='Selectize.js integration with Bokeh',
    long_description='Selectize.js integration with Bokeh',

    # The project's main homepage.
    url='https://github.com/lukauskas/bokeh-selectize',

    # Author details
    author='Saulius Lukauskas',
    author_email='saulius.lukauskas13@imperial.ac.uk',

    # Choose your license
    license='BSD-3',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['bokeh'],

    extras_require={
        'test': ['nose'],
    },
    package_data={
    },
    entry_points={
    },
)