

from setuptools import setup, find_packages


setup(

    name='d2gc',
    version='0.0.0',
    description='Correcting names in d3g.',
    license='Apache-2.0',
    author='David McClure',
    author_email='dclure@stanford.edu',
    scripts=['bin/d2gc'],
    packages=find_packages(),

    install_requires=[],

)
