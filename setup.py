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
    entry_points={
        "console_scripts": [
            "dundie = dundie.__main__:main"
            #   |        | > nome do modulo callable apontado no programa
            #   | > nome do binario     
        ]
    }
)

# *****************************************************
# * Resultado apos executar python -m dundie e dundie * 
# *****************************************************
# 
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % 
# python -m dundie
# hello initializing dundie...
# Executing entry point for dundie... nova informacao
#
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % dundie
# hello initializing dundie...
# Executing dundie from entry point.
#   


# pyproject

# external build tools (poetry, flit)
 
