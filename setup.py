# setuptools
from setuptools import setup , find_packages

setup(
    name="dundie",
    version="0.1.0",
           # x MAJOR
             # y MINOR
               # z PATCH
    description="Reward Point System for Dunder Mifflin",
    author="Alberto Luiz",
    #packages=["dundie"],
    packages=find_packages(),
)
# pyproject

# external build tools (poetry, flit)