"""Module"""

MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: High Priority
medium: Medium Priority
low: Low Priority
"""


def pytest_configure(config):
    """Module"""
    #    1 / 0 INTERNALERROR> ZeroDivisionError: division by zero
    for line in MARKER.split("\n"):
        config.addinivalue_line("markers", line)
