from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    Read the requirements file and return list of requirements
    '''
    Requirements = []
    with open(file_path, 'r') as f:
        Requirements = f.read().splitlines()
        if HYPHEN_E_DOT in Requirements:
            Requirements.remove(HYPHEN_E_DOT)
    return Requirements

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='Disease-Diagnosis-from-Symptoms',
   version='0.0.1',
   description='A package to predict disease from symptoms',
   license="MIT",
   long_description=long_description,
   author='Muhammad Talha',
   author_email='mtalhaasifshazad@gmail.com',
   packages=find_packages(),
   install_requires=get_requirements('requirements.txt')
)