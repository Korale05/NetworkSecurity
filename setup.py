"""
Docstring for setup
setup file is an essential part of packeging and distributing the python project 
"""

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This Function return list of requirements
    """
    requirement_lst : List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #Read line from file
            lines = file.readlines()
            #process each line
            for line in lines:
                requirement = line.strip()
                #ignore the empty line and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)


    except FileNotFoundError:
        print("requirements.txt file is not found")

    return requirement_lst 

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Onkar Korale",
    author_email = "onkarkorale03@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)