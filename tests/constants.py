#PEOPLE_FILE = 'tests/assets/people.csv' # antes das alteracoes pytest.fixture

import os  # necessario importar pq o file vem de uma pasta temporaria
TEST_PATH = os.path.dirname(__file__) 
                        #|    |==> captura o nome do arquivo atual
                        #|==> captura o diretorio do arquivo
PEOPLE_FILE = os.path.join(TEST_PATH, 'assets/people.csv')

