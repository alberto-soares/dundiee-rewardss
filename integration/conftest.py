MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: High Priority
medium: Medium Priority
low: Low Priority
"""

def pytest_configure(config):
#    1 / 0 INTERNALERROR> ZeroDivisionError: division by zero
    map(
        lambda line: config.addinivalue_line('markers', line), 
        MARKER.split("\n"))
