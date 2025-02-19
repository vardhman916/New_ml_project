from setuptools import find_packages,setup
from typing import List

hypen_e = '-e .'
def get_requirements(file_path:str)-> List[str]:
    """thi will return the requirements"""
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n", "") for i in requirements]
        if hypen_e  in requirements:
            requirements.remove(hypen_e)


    return requirements



setup(
name = 'NEW_ml_project', # package name
version = '0.0.2',  # Version
author = 'Vardhman ajmera', # Your name
author_email = 'vardhmanajmera76@gmail.com',
packages = find_packages(), # Automatically finds packages find_packages() detects it only if __init__.py is present.
install_requires=get_requirements('requirements.txt') 
)