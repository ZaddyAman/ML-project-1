from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads the requirements from the given file and returns a list of requirements.
    It also removes '-e .' from the requirements.
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newlines and any empty strings
        requirements = [req.strip() for req in requirements if req.strip()]
        # Remove '-e .' if it exists
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Aman',
    author_email='aman2003sayyad@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Fix the file name
)
