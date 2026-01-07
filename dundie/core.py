# ***********
# * Etapa 2 *
# ***********

"""Core module of dundie"""
import os
from csv import reader  # cria um objeto para carregar o arquivo

from dundie.database import add_movement, add_person, commit, connect
from dundie.utils.log import get_logger  # import absoluto

# from .utils.log import get_logger  # import relativo
log = get_logger()


def load(filepath):
    """Loads data from filepath to the database

    >>> len(load('assets/people.csv'))
    3
    >>> load('assets/people.csv')[0][0]
    'B'
    """
    # **********************************************
    # * Acima exemplo usando o comando doctest >>> *
    # * len(load('assets/people.csv' * * ))3       *
    # **********************************************
    try:
        #        with open(filepath) as file_:
        #            return file_.readlines()
        # return [line.strip() for line in file_.readlines()]
        csv_data = reader(open(filepath))  # funcao reader recebe dados do .csv
    except FileNotFoundError as efo:
        log.error(str(efo))
        raise efo

    db_ = connect()
    people = []
    headers = ["name", "dept", "role", "email"]
    for line in csv_data:
        person_data = dict(zip(headers, [item.strip() for item in line]))
        pk = person_data.pop("email")
        person, created = add_person(db_, pk, person_data)
        #        commit(db_)
        #        person["created"] = created
        #        person["email"] = pk
        return_data = person.copy()
        return_data["created"] = created
        return_data["email"] = pk
        people.append(return_data)

    commit(db_)
    return people


def read(**query):
    """Read data from db and filters using query

    read(email="joe@doe.com")
    """
    db_ = connect()
    return_data = []
    for pk, data in db_["people"].items():

        dept = query.get("dept")
        if dept and dept != data["dept"]:
            continue

        # WALRUS / Assigment Expression - a partir do python 3.8
        if (email := query.get("email")) and email != pk:
            continue

        return_data.append(
            {
                "email": pk,
                "balance": db_["balance"][pk],
                "last_movement": db_["movement"][pk][-1]["date"],
                **data,
            }
        )
    return return_data


def add(value, **query):
    """Add value to each record on query"""
    people = read(**query)
    #    breakpoint()
    if not people:
        raise RuntimeError("Not Found")

    db_ = connect()
    user = os.getenv("USER")
    for person in people:
        add_movement(db_, person["email"], value, user)
    commit(db_)


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
# ***********************************************************************
# * Execucao usando o exemplo do doctest para lenght = 3 e [0][0] = 'X' *
# ***********************************************************************
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
#    'X'
# **********************************************************************
# File "/Users/albertosoares/Projetos/dundiee-rewardss/dundie/core.py",
# line 17, in core.load
# Failed example:
#    load('assets/people.csv')[0][0]
# Expected:
#    'X'
# Got:
#    'B'
# 1 items had no tests:
#    core
# **********************************************************************
# 1 items had failures:
#   1 of   2 in core.load
# 2 tests in 2 items.
# 1 passed and 1 failed.
# ***Test Failed*** 1 failures.
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
#
# ********************************
# * ipython para a funcao reader *
# ********************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# ipython --profile=d5p08
# Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.
#
# IPython profile: d5p08
#
# In [1]: from csv import reader
#
# In [2]: reader(open("assets/people.csv"))
# Out[2]: <_csv.reader at 0x10745fd80>
#
# In [3]: list(reader(open("assets/people.csv")))
# Out[3]:
# [['Jim Halpert', ' Sales', ' Salesman', ' jim@dundlermifflin.com'],
#  ['Dwight Schrute', ' Sales', ' Manager', ' schrute@dundlermifflin.com'],
#  ['Gabe Lewis', ' Directory', ' Manager', ' glewis@dundlermifflin.com ']]
#
# In [4]: exit
#
# *****************************************************************************
# * Execucao da apresentacao dos dados do BD no terminal apos criacao do SHOW *
# *****************************************************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie show --email=jim@dundlermifflin.com
# /Users/albertosoares/Projetos/dundiee-rewardss/dundie/cli.py:7:
# UserWarning: pkg_resources is deprecated as an API.
# See https://setuptools.pypa.io/en/latest/pkg_resources.html.
# The pkg_resources package is slated for removal as early as
# 2025-11-30. Refrain from using this package or pin to Setuptools<81.
#  import pkg_resources  # captura a versao do projeto
#
#                          Dunder Mifflin Report
# ┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━┳━━━━━━━━┓
# ┃ Email                ┃ Balance ┃ Last_Movement┃ Name      ┃ Dept┃ Role   ┃
# ┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━╇━━━━━━━━┩
# │jim@dundlermifflin.com│ 500     │ 2026-01-05...│Jim Halpert│Sales│Salesman│
# └──────────────────────┴─────────┴──────────────┴───────────┴─────┴────────┘
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie show
# /Users/albertosoares/Projetos/dundiee-rewardss/dundie/cli.py:7:
# UserWarning: pkg_resources is deprecated as an API.
# See https://setuptools.pypa.io/en/latest/pkg_resources.html.
# The pkg_resources package is slated for removal as early as
# 2025-11-30. Refrain from using this package or pin to Setuptools<81.
#  import pkg_resources  # captura a versao do projeto
#
#                          Dunder Mifflin Report
# ┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━┳━━━━━━━━┓
# ┃ Email                ┃ Balance ┃ Last_Movement┃ Name      ┃ Dept┃ Role   ┃
# ┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━╇━━━━━━━━┩
# │jim@dundlermiffli...  │ 500     │ 2026-01-05...│Jim Halpert│Sales│Salesman│
# │schrute@dundlermi...  │ 100     │ 2026-01-05...│Dwight Sc..│Sales│Manager │
# │glewis@dundlermi...   │ 100     │ 2026-01-05...│Gabe Lewis │C-L..│CEO     │
# └──────────────────────┴─────────┴──────────────┴───────────┴─────┴────────┘
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie show --dept=Sales
#
#                          Dunder Mifflin Report
# ┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━┳━━━━━━━━┓
# ┃ Email                ┃ Balance ┃ Last_Movement┃ Name      ┃ Dept┃ Role   ┃
# ┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━╇━━━━━━━━┩
# │jim@dundlermiffli...  │ 500     │ 2026-01-05...│Jim Halpert│Sales│Salesman│
# │schrute@dundlermi...  │ 100     │ 2026-01-05...│Dwight Sc..│Sales│Manager │
# └──────────────────────┴─────────┴──────────────┴───────────┴─────┴────────┘
