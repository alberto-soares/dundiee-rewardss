import pytest
from dundie.core import load
from .constants import PEOPLE_FILE

# A funcao precisa iniciar com a palavra test #

@pytest.mark.unit
@pytest.mark.high
def test_load(): 
    """Test function load"""
    assert len(load(PEOPLE_FILE)) == 3
#    breakpoint() 
    assert load(PEOPLE_FILE)[0][0] == 'B'
    
    
#
# *********************
# * pytest execucao 1 *
# *********************
#
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % pytest
#============================= test session starts ============================
#platform darwin -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0
#rootdir: /Users/albertosoares/Projetos/dundiee-rewardss
#plugins: anyio-3.5.0
#collected 1 item                                                               
#
#test_load.py .                                                         [100%]
#
#============================== 1 passed in 0.01s =============================
#
# *********************
# * pytest execucao 2 *
# *********************
#
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % 
#pytest -v
#============================= test session starts ============================
#platform darwin -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0 -- 
#/Users/albertosoares/anaconda3/bin/python
#cachedir: .pytest_cache
#rootdir: /Users/albertosoares/Projetos/dundiee-rewardss
#plugins: anyio-3.5.0
#collected 1 item                                                                                                
#
#test_load.py::test_load PASSED                                         [100%]
#
#============================== 1 passed in 0.01s =============================
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % 
#pytest -vv
#============================= test session starts ============================
#platform darwin -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0 -- 
#/Users/albertosoares/anaconda3/bin/python
#cachedir: .pytest_cache
#rootdir: /Users/albertosoares/Projetos/dundiee-rewardss
#plugins: anyio-3.5.0
#collected 1 item                                                                                                
#
#test_load.py::test_load PASSED                                          [100%]
#
#============================== 1 passed in 0.01s =============================
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % 
