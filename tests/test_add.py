"""Module"""

import pytest

from dundie.core import add
from dundie.database import add_person, commit, connect


@pytest.mark.unit
def test_add_movement():
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

    add(-30, email="joe@doe.com")
    add(90, dept="Management")

    db_ = connect()
    assert db_["balance"]["joe@doe.com"] == 470
    assert db_["balance"]["jim@doe.com"] == 190


#
# ******************************
# " Execucao test_add_movement *
# ******************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# make test
# ============================== test session starts =========================
# platform darwin -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0 --
# /Users/albertosoares/Projetos/dundiee-rewardss/.venv/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/albertosoares/Projetos/dundiee-rewardss
# configfile: pyproject.toml
# testpaths: tests, integration
# plugins: forked-1.6.0
# collected 20 items
#
# tests/test_add.py::test_add_movement PASSED
# tests/test_database.py::test_database_schema PASSED
# tests/test_database.py::test_commit_to_database PASSED
# tests/test_database.py::test_add_person_for_the_first_time PASSED
# tests/test_database.py::test_negative_add_person_invalid_email PASSED
# tests/test_database.py::test_add_or_remove_points_for_person PASSED
# tests/test_load.py::test_load_positive_has_2_people PASSED
# tests/test_load.py::test_load_positive_first_name_starts_with_j PASSED
# tests/test_read.py::test_read_with_query PASSED
# tests/test_utils.py::test_positive_check_valid_email[bruno@rocha.com] PASSED
# tests/test_utils.py::test_positive_check_valid_email[joe@doe.com] PASSED
# tests/test_utils.py::test_positive_check_valid_email[a@b.pt] PASSED
# tests/test_utils.py::test_negative_check_valid_email[bruno@.com] PASSED
# tests/test_utils.py::test_negative_check_valid_email[@doe.com] PASSED
# tests/test_utils.py::test_negative_check_valid_email[a@b] PASSED
# tests/test_utils.py::test_generate_simple_password PASSED
# integration/test_load.py::test_load_positive_call_load_command PASSED
# integration/test_load.py::
# test_load_negative_call_load_command_with_wrong_params[loady] PASSED
# integration/test_load.py::
# test_load_negative_call_load_command_with_wrong_params[carrega] PASSED
# integration/test_load.py::
# test_load_negative_call_load_command_with_wrong_params[start] PASSED
#
