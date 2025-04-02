import pytest
from dundie.core import load
from .constants import PEOPLE_FILE

# A funcao precisa iniciar com a palavra test #

#@pytest.mark.unit
#@pytest.mark.high
#def test_load(): 
#    """Test function load"""
#    assert len(load(PEOPLE_FILE)) == 3
#    breakpoint() 
#    assert load(PEOPLE_FILE)[0][0] == 'B'
    
    
#def setup_module():
#    print()
#    print("roda antes dos testes desse modulo\n")

#def teardown_module():
#    print()
#    print("roda apos os testes desse modulo\n")


# A funcao precisa iniciar com a palavra test #

# *************************************************
# * Exemplo de aplicacao pytest.fixture no modulo * 
# *************************************************

#@pytest.fixture(scope="function", autouse=True)
                 #|==> mudando para module roda antes e depois do modulo 
# @pytest.fixture(scope="function")#, autouse=True)# so a funcao cria o new_file
#def create_new_file(tmpdir):
    # ************************************************
    # * Simplesmente criando e escrevendo no arquivo *
    # ************************************************
    
    #tmpdir.join("new_file.txt").write("isso e sujeira...")
    
    # ********************************
    # * Criando e apagando o arquivo *
    # ********************************
#    file_ = tmpdir.join("new_file.txt") # cria o arquivo
#    file_.write("isso e sujeira...") # escreve no arquivo
#    yield
#    file_.remove()

# *********************************************************


@pytest.mark.unit
@pytest.mark.high
#def test_load(request):
#def test_load():
#def test_load(create_new_file): # so essa funcao cria o new_file
#    """Test function load"""
    
    #if x:   
        #request.addfinalizer(lambda: print("Terminou"))
    #else
    #   ...
    #     
    #with open("arquivo_indesejado.txt", "w") as file_: # side_effect 
    
    #with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as file_:
                # |==> nome dinamico
    
    #filepath = f"arquivo_indesejado-{uuid.uuid4()}.txt"
    #request.addfinalizer(lambda: os.unlink(filepath))


    #with open(filepath, "w") as file_:
       
    #    file_.write("dados uteis somente para o teste")

# *****************************************
# * Boas praticas relacionadas com assert *
# *****************************************
#    assert len(load(PEOPLE_FILE)) == 3
#    breakpoint() 
#    assert load(PEOPLE_FILE)[0][0] == 'B'

def test_load_positive_has_2_people(request):
    """Test function load"""
    assert len(load(PEOPLE_FILE)) == 3 # --junit.xml file erro em /tmp/erro.xml
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % 
#pytest -s -m "unit" --junitxml=/tmp/erro.xml
# --------------- generated xml file: /tmp/erro.xml --------------------------
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % 
#cat /tmp/erro.xml

@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_name_starts_with_b(request):
    """Test function load"""
    assert load(PEOPLE_FILE)[0][0] == 'B'



# ****************************************************
# * Boas praticas relacionadas a criacao de arquivos *
# ****************************************************

#def test_load2(): 
#    """Test function load"""
#    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as file_:
#        file_.write("dados uteis somente para o teste")
#
#    assert len(load(PEOPLE_FILE)) == 3
#    assert load(PEOPLE_FILE)[0][0] == 'B'


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
