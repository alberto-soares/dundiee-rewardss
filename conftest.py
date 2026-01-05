"""Module"""

import pytest
from unittest.mock import patch


MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: High Priority
medium: Medium Priority
low: Low Priority
"""


def pytest_configure(config):
    """Module"""
    for line in MARKER.split("\n"):
        config.addinivalue_line("markers", line)


@pytest.fixture(autouse=True)
def go_to_tmpdir(request):  # injecao de dependencias diretorio temporario diferente
    """Module"""
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield  # protocolo de generators


@pytest.fixture(autouse=True, scope="function")
def setup_testing_database(request):  # banco de dados diferente
    """For each test, create a database file om tmpdir
    force database.py to use that filepath. 
    """
    tmpdir = request.getfixturevalue("tmpdir")
    test_db = str(tmpdir.join("database.test.json"))
    with patch("dundie.database.DATABASE_PATH", test_db):
        yield

#
# ************************************************************************
# * Execucao teste BD apos mudanca do conftest.py para a raiz do projeto *
# ************************************************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# make test
# ============================== test session starts =========================
# platform darwin -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0 --
#  /Users/albertosoares/Projetos/dundiee-rewardss/.venv/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/albertosoares/Projetos/dundiee-rewardss
# configfile: pyproject.toml
# testpaths: tests, integration
# plugins: forked-1.6.0
# collected 14 items
#
# tests/test_database.py::test_database_schema PASSED
# tests/test_load.py::test_load_positive_has_2_people PASSED
# tests/test_load.py::test_load_positive_first_name_starts_with_b PASSED
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
# ======================= 14 passed, 1 warning in 0.13s =======================
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
#
