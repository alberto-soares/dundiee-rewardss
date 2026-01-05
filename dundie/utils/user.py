"""Module"""

from random import sample
from string import ascii_letters, digits


def generate_simple_password(size=8):  # size => password com oito caracteres
    """Generate a simple random password
    [A-Z][a-z][0-9]
    """
    password = sample(ascii_letters + digits, size)
    return "".join(password)


# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# ipython --profile=d5p07
# Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.
#
# IPython profile: d5p07
#
# In [1]: from random import sample
#
# In [2]: letras = "ABCDEFG"
#
# In [3]: sample(letras, 3)
# Out[3]: ['B', 'C', 'F']
#
# In [4]: sample(letras, 3)
# Out[4]: ['C', 'E', 'D']
#
# In [5]: sample(letras, 3)
# Out[5]: ['F', 'A', 'G']
#
# In [6]: sample(letras, 3)
# Out[6]: ['D', 'F', 'E']
#
# In [7]: sample(letras, 3)
# Out[7]: ['F', 'E', 'C']
#
# In [8]: sample(letras, 3)
# Out[8]: ['B', 'F', 'D']
#
# In [9]: sample(letras, 3)
# Out[9]: ['F', 'D', 'G']
#
# In [10]: sample(letras, 3)
# Out[10]: ['B', 'C', 'D']
#
# In [11]: sample(letras, 3)
# Out[11]: ['F', 'B', 'A']
#
# In [12]: sample(letras, 3)
# Out[12]: ['A', 'G', 'D']
#
# In [13]: sample(letras, 3)
# Out[13]: ['B', 'A', 'D']
#
# In [14]: sample(letras, 3)
# Out[14]: ['E', 'F', 'G']
#
# In [15]: sample(letras, 3)
# Out[15]: ['E', 'A', 'B']
#
# In [16]: sample(letras, 3)
# Out[16]: ['C', 'E', 'A']
#
# In [17]: sample(letras, 3)
# Out[17]: ['F', 'A', 'C']
#
# In [18]: sample(letras, 3)
# Out[18]: ['F', 'D', 'E']
#
# In [19]: from random import sample
#
# In [20]: letras = "ABCDEFG"
#
# In [21]: sample(letras, 3)
# Out[21]: ['A', 'B', 'C']
#
# In [22]: "".join(sample(letras, 3))
# Out[22]: 'ADB'
#
# In [23]: "".join(sample(letras, 3))
# Out[23]: 'BGA'
#
# In [24]: "".join(sample(letras, 3))
# Out[24]: 'CAD'
#
# In [25]: "".join(sample(letras, 3))
# Out[25]: 'FAE'
#
# In [26]: from string import ascii_letters
#
# In [27]: ascii_letters
# Out[27]: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# In [28]: from string import digits
#
# In [29]: digits
# Out[29]: '0123456789'
#
# In [30]: from string import punctuation
#
# In [31]: punctuation
# Out[31]: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#
# In [32]: exit
