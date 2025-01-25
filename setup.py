from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This Function will return a list of requirements
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt file not found")
    return requirement_lst
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Uday",
    author_email="udaybhaskar717@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)
# Call the function and print the result
if __name__ == "__main__":
    print(get_requirements())
