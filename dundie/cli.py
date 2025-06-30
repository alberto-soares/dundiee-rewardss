"""Module"""  # pylint: disable=unused-import

# ***********
# * Etapa 1 *
# ***********

import argparse

from dundie.core import load  # noqa

# print("Executing entry point for dundie... nova informacao")

# import sys
# sys.argv # Recebe os parametros enviados do terminal


#                    |==> import absoluto
# from .core import load # import relativo


def main():
    """Module"""
    parser = argparse.ArgumentParser(
        description="Dunder Mifflin Rewards CLI",
        epilog="Enjoy and use with cautions.",
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="The subcommand to run",
        choices=("load", "show", "send"),
        default="help",
    )
    parser.add_argument(
        "filepath", type=str, help="File path to load", default=None
    )
    args = parser.parse_args()
    #    try:
    # globals()[args.subcommand](args.filepath)
    print(*globals()[args.subcommand](args.filepath), end="")


# |--> alteracao para corrigir o return no core.py


#
# except KeyError:
#    print("Subcommand is invalid.")
#
# print(args)
#
#
# ********************************************************
# * Execucao alteracao para corrigir o return no core.py *
# ********************************************************
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie load assets/people.csv
# Bruna Polliana, Presi, Presidente, bruna@dundlermifflin.com
# Arthur Santos, Presi, Vice-Presidente, arthur@dundlermifflin.com
# Victor Santos, Presi, Vice-Presidente, victor@dundlermifflin.com
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
#
# ********************
# * Execucao Etapa 1 *
# ********************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie load people.csv
# hello initializing dundie...
# Namespace(subcommand='load', filepath='people.csv')
# print("Executing dundie from entry point.")
