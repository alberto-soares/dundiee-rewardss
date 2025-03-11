# setuptools
import os
from setuptools import setup , find_packages

def read(*paths): #Recebe uma lista com todos argumentos passados
    """Read the contents of a text file safely.
    >>> read("dundie", "VERSION") 
    '0.1.0'
    >>> read("README.md")
    ...
    """
    rootpath = os.path.dirname(__file__) # indica o caminho do arquivo
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip() #remove linha em branco a mais do editor


def read_requirements(path):
    """Return a list of requirements from a text file"""
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(("#", "git+", '"', '-'))
    ]

setup(
    name="dundie",
    version="0.1.0",
           # x MAJOR
             # y MINOR
               # z PATCH
    description="Reward Point System for Dunder Mifflin",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Alberto Luiz",
    python_requires=">=3.8",
    #packages=["dundie"],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dundie = dundie.__main__:main"
            #   |        | > nome do modulo callable apontado no programa
            #   | > nome do binario     
        ]
    },
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "test": read_requirements("requirements.test.txt"),
           # "pytest"
           # pip install -e '.[dev]' p/ terminal zsh
        "dev": read_requirements("requirements.dev.txt")
           # "ipython",#e possivel indicar versao Ex.: <=8.32.0 pinar a versao
           # "ipdb",
           # "pudb"
        
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
# *****************************************************
# * Resultado apos executar pip install -e '.[dev]'   * 
# *****************************************************
# 
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % 
# pip install -e '.[dev]'
#Obtaining file:///Users/albertosoares/Projetos/dundiee-rewardss
#  Installing build dependencies ... done
#  Checking if build backend supports build_editable ... done
#  Getting requirements to build editable ... done
#  Preparing editable metadata (pyproject.toml) ... done
#Requirement already satisfied: ipython<=8.32.0,>=7.0.0 in 
#./.venv/lib/python3.11/site-packages (from dundie==0.1.0) (8.32.0)
#Requirement already satisfied: ipdb in ./.venv/lib/python3.11/site-packages 
#(from dundie==0.1.0) (0.13.13)
#Requi...
#Successfully built dundie
#Installing collected packages: dundie
#  Attempting uninstall: dundie
#    Found existing installation: dundie 0.1.0
#    Uninstalling dundie-0.1.0:
#      Successfully uninstalled dundie-0.1.0
#Successfully installed dundie-0.1.0
#
# *****************************************************
# * Resultado apos executar pip install -e '.[test]'  * 
# *****************************************************
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % 
# pip install -e '.[test]'
#Obtaining file:///Users/albertosoares/Projetos/dundiee-rewardss
#  Installing build dependencies ... done
#  Checking if build backend supports build_editable ... done
#  Getting requirements to build editable ... done
#  Preparing editable metadata (pyproject.toml) ... done
#Requirement already satisfied: ipython in 
# ./.venv/lib/python3.11/site-packages (from dundie==0.1.0) (8.32.0)
#Requirement already satisfied: decorator in 
#./.venv/lib/python3.11/site-packages (from ipython->dundie==0.1.0) (5.1.1)
#Requi...
#Successfully built dundie
#Installing collected packages: dundie
#  Attempting uninstall: dundie
#    Found existing installation: dundie 0.1.0
#    Uninstalling dundie-0.1.0:
#      Successfully uninstalled dundie-0.1.0
#Successfully installed dundie-0.1.0
#
# *****************************************************************
# * Resultado apos executar pip install -r requirements.test.txt  * 
# *****************************************************************
#
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % 
# pip install -r requirements.test.txt
#Requirement already satisfied: ipython in 
#./.venv/lib/python3.11/site-packages (from -r requirements.test.txt (line 1)) 
#(8.32.0)
#Requirement already satisfied: decorator in 
#./.venv/lib/python3.11/site-packages (from ipython->-r requirements.test.txt 
#(line 1)) (5.1.1)
#Requi...
#
#
# *****************************************************************
# * Resultado apos executar pip install -r requirements.dev.txt   * 
# *****************************************************************
#
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % 
#pip install -r requirements.dev.txt
#Obtaining file:///Users/albertosoares/Projetos/dundiee-rewardss 
# (from -r requirements.dev.txt (line 7))
#  Installing build dependencies ... done
#  Checking if build backend supports build_editable ... done
#  Getting requirements to build editable ... done
#  Preparing editable metadata (pyproject.toml) ... done
#Requirement already satisfied: ipython<=8.32.0,>=7.0.0 in 
# ./.venv/lib/python3.11/site-packages (from -r requirements.dev.txt 
# (line 2)) (8.32.0)
#Requirement already satisfied: ipdb in 
# ./.venv/lib/python3.11/site-packages (from -r requirements.dev.txt (line 3)) 
# (0.13.13)
#Requi...
#Building wheels for collected packages: dundie
#  Building editable for dundie (pyproject.toml) ... done
#  Created wheel for dundie: filename=dundie-0.1.0-0.editable-py3-none-any.whl 
# size=3907 
# sha256=1d2d8038a568b1998a0e1dcfd47e744418ed0301916366577f4cec8da7c50f67
#  Stored in directory: 
# /private/var/folders/_c/1fx8bz0s6818_7_k_2sb3w440000gn/T/pip-ephem-wheel-
# cache-zwxid12y/wheels/b8/b8/c9/
# 05e4bdb02a91d9bf55363b2734cdb6b5adb15bb656df24e46f
#Successfully built dundie
#Installing collected packages: dundie
#  Attempting uninstall: dundie
#    Found existing installation: dundie 0.1.0
#    Uninstalling dundie-0.1.0:
#      Successfully uninstalled dundie-0.1.0
#Successfully installed dundie-0.1.0


# pyproject

# external build tools (poetry, flit)
