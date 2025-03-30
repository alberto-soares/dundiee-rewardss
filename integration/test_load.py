import pytest
from subprocess import check_output


@pytest.mark.integration
@pytest.mark.medium
def test_load():
    """Test command load"""

    out = check_output(
        ["dundie", "load", "tests/assets/people.csv"]
    ).decode("utf-8").split("\n")
    #breakpoint()
    assert len(out) - 1 == 3
#

# ***************************************************************
# * ERRO c/ return [line.strip() for line in file_.readlines()] *
# ***************************************************************
#
#    def test_load():
#        """Test command load"""
#
#        out = check_output(
#            ["dundie", "load", "tests/assets/people.csv"]
#            ).decode("utf-8").split("\n")
#        #).decode("utf-8").split("\n")
#        #breakpoint()
#>       assert len(out) == 3
#E       AssertionError: assert 1 == 3
#E        +  where 1 = len(['Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com'])
#
#integration/test_load.py:14: AssertionError
#
#
#
# ************************************
# * ERRO c/ return file_.readlines() *
# ************************************
#
#    def test_load():
#        """Test command load"""
#    
#        out = check_output(
#            ["dundie", "load", "tests/assets/people.csv"]
#            ).decode("utf-8").split("\n")
#        #).decode("utf-8").split("\n")
#        #breakpoint()
#>       assert len(out) == 3
#E       AssertionError: assert 4 == 3
#E        +  where 4 = len(['Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com', ' Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com', ' Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com ', ''])

#integration/test_load.py:14: AssertionError



#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % ipython
#Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]
#Type 'copyright', 'credits' or 'license' for more information
#IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.

#In [1]: from subprocess import check_output

#In [3]: out = check_output(["dundie", "load", "tests/assets/people.csv"])

#In [5]: print(out)
#b'Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com\n'
#
#In [6]: out = check_output(["dundie", "load", "tests/assets/people.csv"]).decode("utf-8").split("\n")#
#
#In [7]: print(out)
#['Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com', '']
#
# In [8]: check_output(["dundie", "load", "tests/assets/people.csv"]).decode()
#Out[8]: 'Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com\n'
#
#In [9]: check_output(["dundie", "load", "tests/assets/people.csv"]).decode("utf-8")
#Out[9]: 'Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com\n'
#
#In [10]: check_output(["dundie", "load", "tests/assets/people.csv"]).decode("utf-8").split("\n")
#Out[10]: 
#['Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com',
# '']
# 
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % ipython --profile=d5p02 --logfile=/tmp/5p
#2.py
#Activating auto-logging. Current session state plus future input saved.
#Filename       : /tmp/5p2.py
#Mode           : backup
#Output logging : False
#Raw input log  : False
#Timestamping   : False
#State          : active
#Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]
#Type 'copyright', 'credits' or 'license' for more information
#IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.
#
#IPython profile: d5p02
#
#In [1]: from subprocess import check_output
#
#In [3]: check_output(["ls"])
#Out[3]: b'LICENSE\nMakefile\nREADME.md\n__pycache__\nassets\nbuild\ndocs\ndundie\ndundie.egg-info\ndundie.log\nintegration\nmodulo1.py\nmodulo2.py\nmodulo3.py\nrequirements.dev.txt\nrequirements.test.txt\nrequirements.txt\nsetup.py\ntests\n'
#
#In [4]: str(check_output(["ls"]))
#Out[4]: "b'LICENSE\\nMakefile\\nREADME.md\\n__pycache__\\nassets\\nbuild\\ndocs\\ndundie\\ndundie.egg-info\\ndundie.log\\nintegration\\nmodulo1.py\\nmodulo2.py\\nmodulo3.py\\nrequirements.dev.txt\\nrequirements.test.txt\\nrequirements.txt\\nsetup.py\\ntests\\n'"
#
#In [5]: check_output(["ls"]).decode()
#Out[5]: 'LICENSE\nMakefile\nREADME.md\n__pycache__\nassets\nbuild\ndocs\ndundie\ndundie.egg-info\ndundie.log\nintegration\nmodulo1.py\nmodulo2.py\nmodulo3.py\nrequirements.dev.txt\nrequirements.test.txt\nrequirements.txt\nsetup.py\ntests\n'
#
#In [6]: check_output(["ls"]).decode("utf-8").split("\n")
#Out[6]: 
#['LICENSE',
# 'Makefile',
# 'README.md',
# '__pycache__',
# 'assets',
# 'build',
# 'docs',
# 'dundie',
# 'dundie.egg-info',
# 'dundie.log',
# 'integration',
# 'modulo1.py',
# 'modulo2.py',
# 'modulo3.py',
# 'requirements.dev.txt',
# 'requirements.test.txt',
# 'requirements.txt',
# 'setup.py',
# 'tests',
# '']
# 
#  In [7]: exit
