"""Module"""
# Parte 2  Importa a funcao say_hello do modulo2 que esta na mesma pasta
# import modulo2 # Evitar LOOP INFINITO pq a linha1domodulo2eimport modulo1

# Parte 1
NOME = "Alberto"


def say_hi(n):  # Recebe uma entrada
    """Module"""
    print(f"Hi {n}")

# *********************
# * Resultado Parte 1 *
# *********************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# python -i modulo1.py
# >>> say_hi(NOME)
# Hi Alberto
# >>> exit()

# modulo2.say_hello(NOME) ==> Nunca vai acontecer por conta do LOOP INFINITO

# ***************************************
# * Resultado Parte 2 ==> LOOP INFINITO *
# ***************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# python modulo2.py
# Traceback (most recent call last):
# File "/Users/albertosoares/Projetos/dundiee-rewardss/modulo2.py",
# line 1, in <module> import modulo1
# File "/Users/albertosoares/Projetos/dundiee-rewardss/modulo1.py",
# line 1, in <module> import modulo2
# File "/Users/albertosoares/Projetos/dundiee-rewardss/modulo2.py",
# line 6, in <module> modulo1.say_hi(modulo1.NOME)
# AttributeError: partially initialized module 'modulo1' has no attribute
# 'say_hi' (most likely due to a circular import)
#
