"""Module"""

# from subprocess import check_output

import pytest
from click.testing import CliRunner  # Usando CliRunner do click testing

from dundie.cli import load, main

from .constants import PEOPLE_FILE

cmd = CliRunner()
# @pytest.mark.integration
# @pytest.mark.medium
# def test_load():
#    """Test command load"""

#    out = (
#        check_output(["dundie", "load", PEOPLE_FILE])
#        .decode("utf-8")
#        #    .split("\n")
#    )
#     breakpoint()
#       assert len(out) == 3
#     assert len(out) - 1 == 3

#    assert "Dunder Mifflin Associates" in out


@pytest.mark.integration
@pytest.mark.medium
def test_load_positive_call_load_command():
    """Test command load"""

    out = cmd.invoke(load, PEOPLE_FILE)
    # (
    #         check_output(["dundie", "load", PEOPLE_FILE])
    #        .decode("utf-8")
    #    .split("\n")
    #    )
    # breakpoint()
    #    assert len(out) == 3
    # assert len(out) - 1 == 3

    assert "Dunder Mifflin Associates" in out.output


@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.parametrize("wrong_command", ["loady", "carrega", "start"])
def test_load_negative_call_load_command_with_wrong_params(wrong_command):
    """Test command load"""
    #    with pytest.raises(CalledProcessError) as error:
    #        check_output(["dundie", wrong_command, PEOPLE_FILE]).decode(
    #            "utf-8"
    #        ).split("\n")
    # breakpoint()
    #    assert len(out) == 3
    # assert len(out) - 1 == 3

    out = cmd.invoke(main, wrong_command, PEOPLE_FILE)  # out captura o erro

    #    assert "status 2" in str(error.getrepr())
    assert out.exit_code != 0
    assert f"No such command '{wrong_command}'." in out.output


#

# ***************************************************************
# * ERRO c/ return [line.strip() for line in file_.readlines()] *
# ***************************************************************
#
#    def test_load():
#        """Test command load"""
#
#        out = check_output(
#            ["dundie", "load", "tests/assets/people.csv"]
#            ).decode("utf-8").split("\n")
#        #).decode("utf-8").split("\n")
#        #breakpoint()
# >       assert len(out) == 3
# E       AssertionError: assert 1 == 3
# E        +  where 1 = len(
# ['Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com
# Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com
# Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com'])
#
# integration/test_load.py:14: AssertionError
#
#
#
# ************************************
# * ERRO c/ return file_.readlines() *
# ************************************
#
#    def test_load():
#        """Test command load"""
#
#        out = check_output(
#            ["dundie", "load", "tests/assets/people.csv"]
#            ).decode("utf-8").split("\n")
#        #).decode("utf-8").split("\n")
#        #breakpoint()
# >       assert len(out) == 3
# E       AssertionError: assert 4 == 3
# E        +  where 4 = len(
# ['Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com',
# ' Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com',
# ' Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com ', ''])

# integration/test_load.py:14: AssertionError

# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# ipython
# Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.

# In [1]: from subprocess import check_output

# In [3]: out = check_output(["dundie", "load", "tests/assets/people.csv"])

# In [5]: print(out)
# b'Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com
# Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com
# Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com\n'
#
# In [6]: out = check_output(["dundie", "load",
# "tests/assets/people.csv"]).decode("utf-8").split("\n")#
#
# In [7]: print(out)
# ['Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com
# Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com
# Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com', '']
#
# In [8]: check_output(["dundie", "load", "tests/assets/people.csv"]).decode()
# Out[8]: 'Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com
# Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com
# Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com\n'
#
# In [9]: check_output(
# ["dundie", "load", "tests/assets/people.csv"]).decode("utf-8")
# Out[9]: 'Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com
# Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com
# Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com\n'
#
# In [10]: check_output(
# ["dundie", "load", "tests/assets/people.csv"]).decode("utf-8").split("\n")
# Out[10]:
# ['Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com
# Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com
# Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com',
# '']
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# ipython --profile=d5p02 --logfile=/tmp/5p2.py
# Activating auto-logging. Current session state plus future input saved.
# Filename       : /tmp/5p2.py
# Mode           : backup
# Output logging : False
# Raw input log  : False
# Timestamping   : False
# State          : active
# Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.
#
# IPython profile: d5p02
#
# In [1]: from subprocess import check_output
#
# In [2]: check_output(["ls"])
# Out[2]: b'LICENSE\nMakefile\nREADME.md\n__pycache__\nassets\nbuild\ndocs\
# ndundie\ndundie.egg-info\ndundie.log\nintegration\nmodulo1.py\nmodulo2.py\
# nmodulo3.py\nrequirements.dev.txt\nrequirements.test.txt\
# nrequirements.txt\nsetup.py\ntests\n'
#
# In [3]: str(check_output(["ls"]))
# Out[3]: "b'LICENSE\\nMakefile\\nREADME.md\\n__pycache__\\nassets\\nbuild
# \\ndocs\\ndundie\\ndundie.egg-info\\ndundie.log\\nintegration\\nmodulo1.py
# \\nmodulo2.py\\nmodulo3.py\\nrequirements.dev.txt\\nrequirements.test.txt
# \\nrequirements.txt\\nsetup.py\\ntests\\n'"
#
# In [4]: check_output(["ls"]).decode()
# Out[4]: 'LICENSE\nMakefile\nREADME.md\n__pycache__\nassets\nbuild\ndocs\
# ndundie\ndundie.egg-info\ndundie.log\nintegration\nmodulo1.py\nmodulo2.py\
# nmodulo3.py\nrequirements.dev.txt\nrequirements.test.txt\nrequirements.txt\
# nsetup.py\ntests\n'
#
# In [6]: check_output(["ls"]).decode("utf-8").split("\n")
# Out[6]:
# ['LICENSE',
# 'Makefile',
# 'README.md',
# '__pycache__',
# 'assets',
# 'build',
# 'docs',
# 'dundie',
# 'dundie.egg-info',
# 'dundie.log',
# 'integration',
# 'modulo1.py',
# 'modulo2.py',
# 'modulo3.py',
# 'requirements.dev.txt',
# 'requirements.test.txt',
# 'requirements.txt',
# 'setup.py',
# 'tests',
# '']
#
# In [7]: check_output(["ls", "-a"]).decode("utf-8").split("\n")
# Out[7]:
# ['.',
# '..',
# '.git',
# '.github',
# '.gitignore',
# '.mypy_cache',
# '.pytest_cache',
# '.venv',
# '.vscodelocal',
# 'LICENSE',
# 'Makefile',
# 'README.md',
# '__pycache__',
# 'assets',
# 'build',
# 'docs',
# 'dundie',
# 'dundie.egg-info',
# 'dundie.log',
# 'integration',
# 'modulo1.py',
# 'modulo2.py',
# 'modulo3.py',
# 'pyproject.toml',
# 'requirements.dev.txt',
# 'requirements.test.txt',
# 'requirements.txt',
# 'setup.py',
# 'tests',
# '']
# In [8]: exit
#
# ******************************
# * Execucao usando subprocess *
# ******************************
#
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie load assets/people.csv
#
#                      Dunder Mifflin Associates
# ┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ name           ┃ dept      ┃ role     ┃ e-mail                     ┃
# ┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
# │ Jim Halpert    │ Sales     │ Salesman │ jim@dundlermifflin.com     │
# │ Dwight Schrute │ Sales     │ Manager  │ schrute@dundlermifflin.com │
# │ Gabe Lewis     │ Directory │ Manager  │ glewis@dundlermifflin.com  │
# └────────────────┴───────────┴──────────┴────────────────────────────┘
#
# ******************************************
# * Execucao apos alteracao para CliRunner *
# ******************************************
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie loady assets/people.csv
#
# Usage: dundie [OPTIONS] COMMAND [ARGS].
#
# Try 'dundie --help' for help
# ╭─ Error ─────────────────────────────────────────────────────────────╮
# │ No such command 'loady'.                                            │
# ╰─────────────────────────────────────────────────────────────────────╯
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# make test
# ============================ test session starts ======================
# platform darwin -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0 --
# /Users/albertosoares/Projetos/dundiee-rewardss/.venv/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/albertosoares/Projetos/dundiee-rewardss
# configfile: pyproject.toml
# testpaths: tests, integration
# plugins: forked-1.6.0
# collected 6 items
#
# tests/test_load.py::test_load_positive_has_2_people PASSED
# tests/test_load.py::test_load_positive_first_name_starts_with_b PASSED
# integration/test_load.py::test_load_positive_call_load_command PASSED
# integration/test_load.py::
# test_load_negative_call_load_command_with_wrong_params[loady] PASSED
# integration/test_load.py::
# test_load_negative_call_load_command_with_wrong_params[carrega] PASSED
# integration/test_load.py::
# test_load_negative_call_load_command_with_wrong_params[start] PASSED
#
# ============================ 3 passed in 0.11s =========================
