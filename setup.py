from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT= "-e ."

def get_requirements(path:str) -> List[str]:
    "This function returns a list of required packagaes."
    requirements = []
    with open(path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", "") for req in requirements] # Delete "\"

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements

setup(name= "egeml",
      version= "0.0.1",
      author= "Ege Ebiller",
      author_email= "egeebiller96@gmail.com",
      packages= find_packages(),
      install_requires= get_requirements("requirements.txt"))