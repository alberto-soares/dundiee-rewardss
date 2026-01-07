"""Module"""

import pytest

from dundie.core import read
from dundie.database import add_person, commit, connect


@pytest.mark.unit
def test_read_with_query():
    """Module"""
    db_ = connect()

    pk = "joe@doe.com"
    data = {"name": "Joe Doe", "role": "Saleman", "dept": "Sales"}
    _, created = add_person(db_, pk, data)
    assert created is True

    pk = "jim@doe.com"
    data = {"name": "Jim Doe", "role": "Manager", "dept": "Management"}
    _, created = add_person(db_, pk, data)
    assert created is True

    commit(db_)

    #    breakpoint()

    response = read()
    assert len(response) == 2

    response = read(dept="Management")
    assert len(response) == 1
    assert response[0]["name"] == "Jim Doe"

    response = read(email="joe@doe.com")
    assert len(response) == 1
    assert response[0]["name"] == "Joe Doe"


#
# *********************************************
# * Execucao breakpoint para verificar o erro *
# *********************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# pytest -s -m  "unit" -k read
# ========================== test session starts =============================
# platform darwin -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0 --
# /Users/albertosoares/Projetos/dundiee-rewardss/.venv/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/albertosoares/Projetos/dundiee-rewardss
# configfile: pyproject.toml
# testpaths: tests, integration
# plugins: forked-1.6.0
# collected 19 items / 18 deselected / 1 selected
#
# tests/test_read.py::test_read_with_query >
# /Users/albertosoares/Projetos/dundiee-rewardss/tests/test_read.py(30)
# test_read_with_query()
#     29
# ---> 30     response = read()
#     31     assert len(response) == 2
#
# ipdb> read()
# []
# ipdb> read(dept="Sales")
# *** KeyError: 'email'
# db_
# {'people': {'joe@doe.com': {'name': 'Joe Doe', 'role': 'Saleman',
#  'dept': 'Sales'}, 'jim@doe.com': {'name': 'Jim Doe', 'role': 'Manager',
# 'dept': 'Management'}}, 'balance': {'joe@doe.com': 500, 'jim@doe.com': 100},
# 'movement': {'joe@doe.com': [{'date': '2026-01-05T21:34:27.925900', 'actor':
#  'system', 'value': 500}], 'jim@doe.com': [
# {'date': '2026-01-05T21:34:27.928320', 'actor': 'system', 'value': 100}]},
#  'users': {'joe@doe.com': {'password': 'CpLhxGWX'}, 'jim@doe.com':
#  {'password': 'RIrU0Caj'}}}
# ipdb> db_["people"].items()
# dict_items([('joe@doe.com', {'name': 'Joe Doe',
# 'role': 'Saleman', 'dept': 'Sales'}),
# ('jim@doe.com', {'name': 'Jim Doe', 'role': 'Manager',
# 'dept': 'Management'})])
# ipdb> q
#
# *********************************************************************
# * Execucao breakpoint apos verificar o erro e alterar usando WALRUS *
# *********************************************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# pytest -s -m  "unit" -k read
# ========================== test session starts =============================
# platform darwin -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0 --
# /Users/albertosoares/Projetos/dundiee-rewardss/.venv/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/albertosoares/Projetos/dundiee-rewardss
# configfile: pyproject.toml
# testpaths: tests, integration
# plugins: forked-1.6.0
# collected 19 items / 18 deselected / 1 selected
#
# tests/test_read.py::test_read_with_query >
# /Users/albertosoares/Projetos/dundiee-rewardss/tests/test_read.py(30)
# test_read_with_query()
#     29
# ---> 30     response = read()
#     31     assert len(response) == 2
#
# ipdb> read()
# [{'email': 'joe@doe.com', 'balance': {'joe@doe.com':
# [{'date': '2026-01-05T22:15:54.911133', 'actor': 'system', 'value': 500}],
#  'jim@doe.com': [{'date': '2026-01-05T22:15:54.914118', 'actor': 'system',
#  'value': 100}]}, 'last_movement': '2026-01-05T22:15:54.911133',
# 'name': 'Joe Doe', 'role': 'Saleman', 'dept': 'Sales'},
# {'email': 'jim@doe.com', 'balance': {'joe@doe.com':
# [{'date': '2026-01-05T22:15:54.911133', 'actor': 'system'
# 'value': 500}], 'jim@doe.com': [{'date': '2026-01-05T22:15:54.914118',
# 'actor': 'system', 'value': 100}]}
# 'last_movement': '2026-01-05T22:15:54.914118', 'name': 'Jim Doe'
# 'role': 'Manager', 'dept': 'Management'}]
# ipdb> read(dept="Sales")
# [{'email': 'joe@doe.com', 'balance': {'joe@doe.com':
# [{'date': '2026-01-05T22:15:54.911133', 'actor': 'system', 'value': 500}],
#  'jim@doe.com': [{'date': '2026-01-05T22:15:54.914118', 'actor': 'system',
# 'value': 100}]}, 'last_movement': '2026-01-05T22:15:54.911133',
# 'name': 'Joe Doe', 'role': 'Saleman', 'dept': 'Sales'}]
# ipdb> q
#
