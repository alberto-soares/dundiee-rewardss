# ***********
# * Etapa 2 *
# ***********

"""Core module of dundie"""

from dundie.utils.log import get_logger

log = get_logger()


def load(filepath):
    """Loads data from filepath to the database

    >>> len(load('assets/people.csv'))
    3
    >>> load('assets/people.csv')[0][0]
    'B'
    """

# *****************************************************************************
# * Acima exemplo usando o comando doctest >>> len(load('assets/people.csv')) *
# * 3                                                                         *
# *****************************************************************************
    try:        
        with open(filepath) as file_:
            return file_.readlines()
            # return [line.strip() for line in file_.readlines()]
    except FileNotFoundError as e:
        log.error(str(e))
        raise e

# subcommands = {
#    "load": load
# }
# ********************
# * Execucao Etapa 2 *
# ********************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie load assets/people.csv
# hello initializing dundie...
# Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com
#
# Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com
#
# Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com
#
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# python -m dundie load assets/people.csv
# hello initializing dundie...
# Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com
#
# Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com
#
# Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com
#
#
# ************************************************************************
# * Execucao chamada teste unitario usando o ipython modo iterativo (-i) *
# ************************************************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# ipython -i dundie/core.py
# Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.
#
# In [1]: load
# Out[1]: <function __main__.load(filepath)>
#
# In [2]: load("assets/people.csv")
# Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com
#
# Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com
#
# Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com
#
#
# In [3]: exit
# ********************************************************************
# * Execucao de funcao testavel usando o ipython modo iterativo (-i) *
# ********************************************************************
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# ipython -i dundie/core.py
# Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.
#
# In [1]: load
# Out[1]: <function __main__.load(filepath)>
#
# In [2]: load("assets/people.csv")
# Out[2]:
# ['Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com\n',
# 'Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com\n',
# 'Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com \n']
#
# In [3]: retorno = load("assets/people.csv")
#
# In [4]: len(retorno)
# Out[4]: 3
#
# In [5]: assert len(retorno) == 3
#
# In [6]: assert len(retorno) == 2
# ---------------------------------------------------------------------------
# AssertionError                            Traceback (most recent call last)
# Cell In[6], line 1
# ----> 1 assert len(retorno) == 2
#
# AssertionError:
#
# In [7]: exit
#
# ************************************************
# * Execucao usando o exemplo do doctest len = 3 *
# ************************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# python -m doctest -v dundie/core.py
# Trying:
#    len(load('assets/people.csv'))
# Expecting:
#    3
# ok
# 1 items had no tests:
#    core
#  items passed all tests:
#   1 tests in core.load
# 1 tests in 2 items.
# 1 passed and 0 failed.
# Test passed.
#
#
# ************************************************
# * Execucao usando o exemplo do doctest len = 2 *
# ************************************************
#
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# python -m doctest -v dundie/core.py
# Trying:
#    len(load('assets/people.csv'))
# Expecting:
#    2
# **********************************************************************
# File "/Users/albertosoares/Projetos/dundiee-rewardss/dundie/core.py",line14,
# in core.load
# Failed example:
#    len(load('assets/people.csv'))
# Expected:
#    2
# Got:
#    3
# 1 items had no tests:
#    core
# **********************************************************************
# 1 items had failures:
#   1 of   1 in core.load
# 1 tests in 2 items.
# 0 passed and 1 failed.
# ***Test Failed*** 1 failures.
#
#
# ***********************************************************************
# * Execucao usando o exemplo do doctest para lenght = 3 e [0][0] = 'B' *
# ***********************************************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# python -m doctest -v dundie/core.py
# Trying:
#    len(load('assets/people.csv'))
# Expecting:
#    3
# ok
# Trying:
#    load('assets/people.csv')[0][0]
# Expecting:
#    'B'
# ok
# 1 items had no tests:
#    core
# 1 items passed all tests:
#   2 tests in core.load
# 2 tests in 2 items.
# 2 passed and 0 failed.
# Test passed.
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
#
#
#
#
