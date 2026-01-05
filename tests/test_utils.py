"""Module"""

import pytest

from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


@pytest.mark.unit
@pytest.mark.parametrize(
    "address", ["bruno@rocha.com", "joe@doe.com", "a@b.pt"]
)  # parametrize ==> usado para substituir acoes repetidas
def test_positive_check_valid_email(address):
    """Ensure email is valid."""
    #    assert check_valid_email("bruno@rocha.com") is True
    #    assert check_valid_email("joe@doe.com") is True
    assert check_valid_email(address) is True


@pytest.mark.unit
@pytest.mark.parametrize(
    "address", ["bruno@.com", "@doe.com", "a@b"]
)  # parametrize ==> usado para substituir acoes repetidas
def test_negative_check_valid_email(address):
    """Ensure email is invalid."""
    #    assert check_valid_email("bruno@.com") is False
    #    assert check_valid_email("@doe.com") is False
    assert check_valid_email(address) is False


@pytest.mark.unit
def test_generate_simple_password():
    """Test generation of random simple password.
    TODO: Generate hashed complex passwords, encrypit it
    """
    passwords = []
    for _ in range(100):
        passwords.append(generate_simple_password(8))

    #    print(passwords)
    assert len(set(passwords)) == 100


# ***************************************************
# * Execucao apos alteracao para Regular Expression *
# ***************************************************
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# make test
# ============================= test session starts ==========================
# platform darwin -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
# -- /Users/albertosoares/Projetos/dundiee-rewardss/.venv/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/albertosoares/Projetos/dundiee-rewardss
# configfile: pyproject.toml
# testpaths: tests, integration
# plugins: forked-1.6.0
# collected 8 items
# ts/test_load.py::test_load_positive_has_2_people PASSED
# tests/test_load.py::test_load_positive_first_name_starts_with_b PASSED
# tests/test_utils.py::test_positive_check_valid_email PASSED
# tests/test_utils.py::test_negative_check_valid_email PASSED
# integration/test_load.py::test_load_positive_call_load_command PASSED
# integration/test_load.py::
# test_load_negative_call_load_command_with_wrong_params[loady] PASSED
# integration/test_load.py::
# test_load_negative_call_load_command_with_wrong_params[carrega] PASSED
# integration/test_load.py::
# test_load_negative_call_load_command_with_wrong_params[start] PASSED
#
# ======================= 8 passed, 1 warning in 0.13s =======================
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
#
#
# ********************************************
# * Execucao apos alteracao para parametrize *
# ********************************************
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# make test
# ============================= test session starts ==========================
# platform darwin -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
# -- /Users/albertosoares/Projetos/dundiee-rewardss/.venv/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/albertosoares/Projetos/dundiee-rewardss
# configfile: pyproject.toml
# testpaths: tests, integration
# plugins: forked-1.6.0
# collected 12 items
#
# tests/test_load.py::test_load_positive_has_2_people PASSED
# tests/test_load.py::test_load_positive_first_name_starts_with_b PASSED
# tests/test_utils.py::test_positive_check_valid_email[bruno@rocha.com] PASSED
# tests/test_utils.py::test_positive_check_valid_email[joe@doe.com] PASSED
# tests/test_utils.py::test_positive_check_valid_email[a@b.pt] PASSED
# tests/test_utils.py::test_negative_check_valid_email[bruno@.com] PASSED
# tests/test_utils.py::test_negative_check_valid_email[@doe.com] PASSED
# tests/test_utils.py::test_negative_check_valid_email[a@b] PASSED
# integration/test_load.py::test_load_positive_call_load_command PASSED
# integration/test_load.py::
# test_load_negative_call_load_command_with_wrong_params[loady] PASSED
# integration/test_load.py::
# test_load_negative_call_load_command_with_wrong_params[carrega] PASSED
# integration/test_load.py::
# test_load_negative_call_load_command_with_wrong_params[start] PASSED
#
# ======================= 12 passed, 1 warning in 0.13s =======================
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
#
# ************************************
# * Execucao  para gerar as password *
# ************************************
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
# collected 13 items
#
# tests/test_load.py::test_load_positive_has_2_people PASSED
# tests/test_load.py::test_load_positive_first_name_starts_with_b PASSED
# tests/test_utils.py::test_positive_check_valid_email[bruno@rocha.com] PASSED
# tests/test_utils.py::test_positive_check_valid_email[joe@doe.com] PASSED
# tests/test_utils.py::test_positive_check_valid_email[a@b.pt] PASSED
# tests/test_utils.py::test_negative_check_valid_email[bruno@.com] PASSED
# tests/test_utils.py::test_negative_check_valid_email[@doe.com] PASSED
# tests/test_utils.py::test_negative_check_valid_email[a@b] PASSED
# tests/test_utils.py::test_generate_simple_password ['nlxGQZ1w', '6tMj74JV',
#  '67DJCmEs', '8VteE9gu', 'umhjQ15e', 'JOFkeDGX', 'rgcbJTSx', 'boj1lPs5',
#  'cV6F751e', '1bRKvsh2', 'VG5Z1j3v', 'oWwi3sD7', 'YzJBdoWj', 'tUEFrAvB',
#  'Gk7sqcFC', '2R95S6CO', 'x7Ln5yhK', 'Xpd7wG8f', '7GZnP1oR', 'AIKbm0oO',
#  '2EVFrw34', 'tFMKqedR', 'kzBW9c7H', 'iWJuEN7M', 'wyqaZASU', 'tzOA9TfC',
#  '1jmcIAXC', 'cXufQthW', 'RZ1jCwIx', 'gB8ojbch', 'DGOpcv35', 'zB0ecoOM',
#  'ydKV1pBL', 'pylAOCXP', '1ni9fNtv', '0MpyGYzA', 'sGUXTz3D', '21qM5Q3B',
#  'oDwYGqfj', '5Jf6DMTW', 'hX9J2dwi', 'M8B7yWZ1', 'wHTidcV4', 'k7ZymGRa',
#  '8ciaYgqV', 'qjUEonbs', 'DqgHMyzk', 'ePOZ6UY1', 'ZATmaQdC', 'nrQv9F7L',
#  'd9ObijNK', 'KFnE9wjO', 'lNLPfQva', '8fgXDO41', 'LDRATdcf', 'Wv6OXiM9',
#  '7cwq8UC9', 'J381uayP', '6Fuq2m9c', 'BLNaWyfe', 'sXh862v0', 'Uyn3tWb0',
#  'MOW0siXg', 'GIqAtXVl', 'VotG3zAp', 'auVZ6xUX', 'S5lsze6O', '2pU5wou8',
#  'xEaTHo7u', 'AvD7Zrd0', 't5kVHXfb', '3b8CLk0c', 'AJeM7Rkf', '0NAYk5iV',
#  'iJzcYbZ6', 'rsUqCR8u', 'qD8izlck', '5WkwJvSd', '0XPFHY5T', 'HyBecEwG',
#  'FxrzEkCN', 'EukPMO5Q', 'Gdjz5Oa6', 'bBGUqZWs', '7MiCcrG2', 'bidYhksR',
#  'JzhAOViM', 'NOsz1JeB', 'coSmWuN9', 'on3Jyk8W', 'jzbyWl9X', 'DFOmCpXn',
#  'fjWhvOUg', 'uTNM4hUg', '3emt0EcM', '7Pfpm1Rg', 'vZLq5Sgp', 'eCUVoEHn',
#  'alTMHgDm', 'HFztbMO7'] PASSED
# integration/test_load.py::test_load_positive_call_load_command PASSED
# integration/test_load.py::
# test_load_negative_call_load_command_with_wrong_params[loady] PASSED
# integration/test_load.py::
# test_load_negative_call_load_command_with_wrong_params[carrega] PASSED
# integration/test_load.py::
# test_load_negative_call_load_command_with_wrong_params[start] PASSED
#
# ======================= 13 passed, 1 warning in 0.13s =======================
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
#
