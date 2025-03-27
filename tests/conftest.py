import pytest

MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: High Priority
medium: Medium Priority
low: Low Priority
"""


def pytest_configure(config):
#    1 / 0 INTERNALERROR> ZeroDivisionError: division by zero
    for line in MARKER.split("\n"):
        config.addinivalue_line('markers', line)

@pytest.fixture(autouse=True)   # dados fixos
def go_to_tmpdir(request):  # injecao de dependencias
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd(): # cwd==> changing work directory
        yield  # generator protocol
                        
                