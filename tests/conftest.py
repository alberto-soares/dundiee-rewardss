"""Module"""
import pytest

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
        config.addinivalue_line('markers', line)

@pytest.fixture(autouse=True)
def go_to_tmpdir(request):  # injecao de dependencias
    """Module"""
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield  # protocolo de generators

# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# ipython --profile=d5p03
# Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.
# IPython profile: d5p03
# In [1]: def numero(n):
#   ...:     return n + 1
#   ...: 
# In [2]: numero(5)
# Out[2]: 6
# In [3]: def numero(n):
#   ...:     return n + 1
#   ...:     print("nunca vai rodar")
#   ...: 
# In [4]: numero(5)
# Out[4]: 6
# In [5]: numero(5)
# Out[5]: 6
# In [6]: numero(5)
# Out[6]: 6
# In [7]: def numero(n):
#   ...:     yield n + 1
#   ...:     print("com yield agora vai rodar")
#   ...:     yield n + 2
#  ...:     yield n + 3
#   ...:     yield n + 4
#   ...: 
# In [8]: resultado = numero(5)
# In [9]: resultado
# Out[9]: <generator object numero at 0x107a1c5f0>
# In [10]: next(resultado)
# Out[10]: 6
# In [11]: next(resultado)
# com yield agora vai rodar
# Out[11]: 7
# In [12]: next(resultado)
# Out[12]: 8
# In [13]: next(resultado)
# Out[13]: 9
# In [14]: next(resultado)
# ---------------------------------------------------------------------------
# StopIteration                             Traceback (most recent call last)
# Cell In[14], line 1
# ----> 1 next(resultado)
# StopIteration: 
# In [15]: resultado = numero(5)
# In [16]: resultado
# Out[16]: <generator object numero at 0x107f068e0>
# In [17]: for n in resultado:  # como resultado e um generator usamos o for
#    ...:     print(n)
#    ...: 
# 6
# com yield agora vai rodar
# 7
# 8
# 9
# In [18]: exit