.PHONY: install virtualenv ipython clean test pflake8


install:
	
#	echo "Hello installing"

# *************************
# * Resultado da execucao * 
# *************************
#
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % 
#make install
#echo "Hello installing"
#Hello installing
#

#	@echo "Hello installing"

# *******************************
# * Resultado da execucao com @ * 
# *******************************
#
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % 
#make install
#Hello installing

	@echo "Installing for dev environment"
#	@pip install -e '.[dev]'
	@.venv/bin/python -m pip install -e '.[dev]'


virtualenv:
# Cria a virtual env caso ela nao exista
	@.venv/bin/python -m pip -m venv .venv 


ipython:
	@.venv/bin/ipython


lint: 
	@.venv/bin/pflake8

fmt:
	@.venv/bin/isort dundie tests integration
	@.venv/bin/black dundie tests integration

test:
#	@.venv/bin/pytest -vv -s tests/ ==> antes da configuracao do pytest
	@.venv/bin/pytest -s

#testci:
#	 @pytest -v --junitxml=test-result.xml
#	@.venv/bin/pytest -v --junitxml=test-result.xml 
#                              |=> cria arquivo .xml no github
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % 
#make testci
#------- generated xml file: 
#/Users/albertosoares/Projetos/dundiee-rewardss/test-result.xml -----------

watch:
#	@ls **/*.py | entr pytest
#	@.venv/bin/ptw -- -vv -s tests/ ==> antes da configuracao do pytest
	@.venv/bin/ptw -- -vv -s
# *******************************************************
# * Apos alteracao para @.venv/bin/ptw -- -vv -s tests/ *
# *******************************************************
#
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# make watch
#
#[Tue Oct 22 12:31:34 2024] Running: py.test -vv -s tests/
#=========== test session starts ============
#platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0 -- /Users/albertosoares/Projetos/python_dundie_rewardss/.venv/bin/python
#cachedir: .pytest_cache
#rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
#collected 1 item                           
#
#tests/test_load.py::test_load PASSED
#
#============ 1 passed in 0.01s =============
#
# ***************************************************
# * Apos a criacao do project.toml erro ao executar *
# ***************************************************
#
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % make watch
#Traceback (most recent call last):
#  File "/Users/albertosoares/Projetos/python_dundie_rewardss/.venv/bin/ptw", 
#line 8, in <module> sys.exit(main())
#  File "/Users/albertosoares/Projetos/python_dundie_rewardss/.venv/lib/
#python3.11/site-packages/pytest_watch/command.py", line 83, in main
#    if not merge_config(args, pytest_args, verbose=args['--verbose']):
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#  File "/Users/albertosoares/Projetos/python_dundie_rewardss/.venv/lib/
#  python3.11/site-packages/pytest_watch/config.py", line 95, in merge_config
#   config.read(config_path)
#  File "/Users/albertosoares/anaconda3/lib/python3.11/configparser.py", 
#  line 713, in read
#    self._read(fp, filename)
#  File "/Users/albertosoares/anaconda3/lib/python3.11/configparser.py",
# line 1132, in _read
#    raise e
#configparser.ParsingError: Source contains parsing errors: 
#'/Users/albertosoares/Projetos/python_dundie_rewardss/pyproject.toml'
#        [line  7]: ']\n'
#make: *** [watch] Error 1
# ***********************************************************
# * Rodei o ipython e executei o pip install pytest-watcher *
# ***********************************************************
#
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
#ipython
#Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]
#Type 'copyright', 'credits' or 'license' for more information
#IPython 8.25.0 -- An enhanced Interactive Python. Type '?' for help.
#[TerminalIPythonApp] WARNING | File not found: 
#'/Users/albertosoares/.vscode/extensions/
#ms-python.python-2024.12.3-darwin-arm64/python_files/pythonrc.py'
#
#In [1]: pip install pytest-watcher
#Collecting pytest-watcher
#  Downloading pytest_watcher-0.4.3-py3-none-any.whl.metadata (6.5 kB)
#Requirement already satisfied: watchdog>=2.0.0 in 
#./.venv/lib/python3.11/site-packages (from pytest-watcher) (5.0.3)
#Downloading pytest_watcher-0.4.3-py3-none-any.whl (11 kB)
#Installing collected packages: pytest-watcher
#Successfully installed pytest-watcher-0.4.3
#
#[notice] A new release of pip is available: 24.1 -> 24.3.1
#[notice] To update, run: pip install --upgrade pip
#Note: you may need to restart the kernel to use updated packages.
#
# ****************************************************************
# * Apos rodar o ipython e executar o pip install pytest-watcher *
# ****************************************************************
#
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
#make watch                                               
#pytest-watcher version 0.4.3
#Runner command: pytest
#Waiting for file changes in 
#/Users/albertosoares/Projetos/python_dundie_rewardss/-vv[pytest-watcher]
#Current runner args: [-s]
#
#Controls:
#> Enter : Invoke test runner
#> r     : reset all runner args
#> c     : change runner args
#> f     : run only failed tests (--lf)
#> p     : drop to pdb on fail (--pdb)
#> v     : increase verbosity (-v)
#> e     : Erase terminal screen
#> q     : quit pytest-watcher
#
# **********************************************************************
# * Apos rodar make watch alterei o arquivo e pressionei a tecla Enter *
# **********************************************************************
#
#
#
#=============== test session starts ===============
#platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0 --
# /Users/albertosoares/Projetos/python_dundie_rewardss/.venv/bin/python
#cachedir: .pytest_cache
#rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
#configfile: pyproject.toml
#testpaths: tests, integration
#collected 2 items                                 
#
#tests/test_load.py::test_load PASSED
#integration/test_load.py::test_load PASSED
#
#================ 2 passed in 0.04s ================
#[pytest-watcher]
#Current runner args: [-s]
#Press w to show menu=============== test session starts ===============
#platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0 -- 
#/Users/albertosoares/Projetos/python_dundie_rewardss/.venv/bin/python
#cachedir: .pytest_cache
#rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
#configfile: pyproject.toml
#testpaths: tests, integration
#collected 2 items                                 
#
#tests/test_load.py::test_load PASSED
#integration/test_load.py::test_load PASSED
#
#================ 2 passed in 0.03s ================
#[pytest-watcher]
#Current runner args: [-s -v]
#Press w to show menu ==> pressionei q para sair
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
#


clean:         ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/build

