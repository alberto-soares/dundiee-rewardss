"""Module"""

# ***********
# * Etapa 1 *
# ***********

import json

import pkg_resources  # captura a versao do projeto

# import argparse
import rich_click as click
from rich.console import Console

# from rich import print
from rich.table import Table

# from dundie.core import load as coreload  # import absoluto
from dundie import core

# print("Executing entry point for dundie... nova informacao")
# import sys
# sys.argv # Recebe os parametros enviados do terminal
# from .core import load # import relativo


click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True


@click.group()  # sai argparse e import click
@click.version_option(pkg_resources.get_distribution("dundie").version)
def main():
    """Dunder Mifflin Rewards System.

    This cli application control Dunder Mifflin Rewards
    """


#    parser = argparse.ArgumentParser(
#        description="Dunder Mifflin Rewards CLI",
#        epilog="Enjoy and use with cautions.",
#    )
#    parser.add_argument(
#        "subcommand",
#        type=str,
#        help="The subcommand to run",
#        choices=("load", "show", "send"),
#        default="help",
#    )
#    parser.add_argument(
#        "filepath", type=str, help="File path to load", default=None
#    )
#    args = parser.parse_args()

# try:
# globals()[args.subcommand](args.filepath)
#    print(*globals()[args.subcommand](args.filepath), end="")
# |--> alteracao para corrigir o return no core.py

# except KeyError:
#    print("Subcommand is invalid.")

# print(args)


@main.command()
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):  # injecao de dependencia
    """Loads the file to the database.

    ## Features

    - Validates data
    - Parses the file
    - Loads to database
    """
    #    if args.subcommand == "load":
    #    result = core.load(filepath)
    #
    # ************************
    # * Alteracao para Table *
    # ************************
    #
    table = Table(title="Dunder Mifflin Associates")
    headers = ["name", "dept", "role", "created", "e-mail"]
    for header in headers:
        table.add_column(header, style="magenta")

    result = core.load(filepath)
    for person in result:
        #  print("-" * 50)
        #  for key, value in zip(header, person.split(",")):
        #  print(f"[red]{key}[/] -> [magenta]{value.strip()}[/]")
        # table.add_row(*[field.strip() for field in person.split(",")])  # lereg
        table.add_row(*[str(value) for value in person.values()])  # lereg

    console = Console()
    console.print(table)


@main.command()
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.option("--output", default=None)
def show(output, **query):
    """Shows informatio about users"""
    result = core.read(**query)
    if output:
        with open(output, "w") as output_file:
            output_file.write(json.dumps(result))

    if not result:
        print("Nothing to show")

    table = Table(title="Dunder Mifflin Report")
    for key in result[0]:
        table.add_column(key.title(), style="magenta")

    for person in result:
        table.add_row(*[str(value) for value in person.values()])  # lereg

    console = Console()
    console.print(table)


@main.command()
@click.argument("value", type=click.INT, required=True)
@click.option(
    "--operation", default="add", type=click.Choice(["add", "subtract"])
)
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.pass_context
def add(ctx, value, operation, **query):
    """Add or subtract points to the user or dept"""
    if operation == "subtract":
        value = -value

    core.add(value, **query)
    ctx.invoke(show, **query)


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
#
# ****************************************************************************
# * Execucao com o print(*globals()[args.subcommand](args.filepath), end="") *
# ****************************************************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie load assets/people.csv
# Jim Halpert, Sales, Salesman, jim@dundlermifflin.com
# Dwight Schrute, Sales, Manager, schrute@dundlermifflin.com
# Gabe Lewis, Directory, Manager, glewis@dundlermifflin.com
#
# *************************************************************
# * Execucao apos alteracao para substituir o                 *
# * print(*globals()[args.subcommand](args.filepath), end="") *
# *************************************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie load assets/people.csv
#
# --------------------------------------------------
# name -> Jim Halpert
# dept -> Sales
# role -> Salesman
# e-mail -> jim@dundlermifflin.com
# --------------------------------------------------
# name -> Dwight Schrute
# dept -> Sales
# role -> Manager
# e-mail -> schrute@dundlermifflin.com
# --------------------------------------------------
# name -> Gabe Lewis
# dept -> Directory
# role -> Manager
# e-mail -> glewis@dundlermifflin.com
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
#
# ****************************************************
# * Execucao apos alteracao do argparse para o click *
# ****************************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie load assets/people.csv
# --------------------------------------------------
# name -> Jim Halpert
# dept -> Sales
# role -> Salesman
# e-mail -> jim@dundlermifflin.com
# --------------------------------------------------
# name -> Dwight Schrute
# dept -> Sales
# role -> Manager
# e-mail -> schrute@dundlermifflin.com
# --------------------------------------------------
# name -> Gabe Lewis
# dept -> Directory
# role -> Manager
# e-mail -> glewis@dundlermifflin.com
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# *********************************************************************
# * Execucao apos alteracao do argparse para o click que cria um HELP *
# *********************************************************************
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % dundie
# Usage: dundie [OPTIONS] COMMAND [ARGS]...
#
#  Dunder Mifflin Rewards System.
#
#  This cli application control Dunder Mifflin Rewards
#
# Options:
#  --help  Show this message and exit.
#
# Commands:
#  load  Module
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# *********************************************************************
# * Execucao apos alteracao do argparse para o click que cria um HELP *
# *********************************************************************
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss  %
# dundie load --help
# Usage: dundie load [OPTIONS] FILEPATH
#
#  Loads the file to the database.
#
# Options:
#  --help  Show this message and exit.
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# ***********************************************
# * Execucao apos import do rich_click colorido *
# ***********************************************
#
# .venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss % dundie
#
# Usage: dundie [OPTIONS] COMMAND [ARGS]...
#
# Dunder Mifflin Rewards System.
# This cli application control Dunder Mifflin Rewards
#
# ╭─ Options ────────────────────────────────────────────────────────────────╮
# │ --version    Show the version and exit.                                  │
# │ --help       Show this message and exit.                                 │
# ╰──────────────────────────────────────────────────────────────────────────╯
# ╭─ Commands ───────────────────────────────────────────────────────────────╮
# │ load  Loads the file to the database.                                    │
# ╰──────────────────────────────────────────────────────────────────────────╯
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie load --help
#
# Usage: dundie load [OPTIONS] FILEPATH
#
# Loads the file to the database.
#
# ╭─ Options ────────────────────────────────────────────────────────────────╮
# │ *  FILEPATH    (PATH) [required]                                         │
# │    --help      Show this message and exit.                               │
# ╰──────────────────────────────────────────────────────────────────────────╯
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie sdfghi
#
# Usage: dundie [OPTIONS] COMMAND [ARGS]...
#
# Try 'dundie --help' for help
# ╭─ Error ──────────────────────────────────────────────────────────────────╮
# │ No such command 'sdfghi'.                                                │
# ╰──────────────────────────────────────────────────────────────────────────╯
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie load --help
#
# Usage: dundie load [OPTIONS] FILEPATH
#
# Loads the file to the database
#
#                                               Features
#
#  • Validates data
#  • Parses the file
#  • Loads to database
#
# ╭─ Options ─────────────────────────────────────────────────────────────────╮
# │ *  FILEPATH    (PATH) [required]                                          │
# │    --help      Show this message and exit.                                │
# ╰───────────────────────────────────────────────────────────────────────────╯
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
#
# **********************************************
# * Execucao apos alteracao para formato Table *
# **********************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie load assets/people.csv
#
#                      Dunder Mifflin Associates
# ┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ name           ┃ dept      ┃ role     ┃ e-mail                     ┃
# ┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
# │ Jim Halpert    │ Sales     │ Salesman │ jim@dundlermifflin.com     │
# │ Dwight Schrute │ Sales     │ Manager  │ schrute@dundlermifflin.com │
# │ Gabe Lewis     │ Directory │ Manager  │ glewis@dundlermifflin.com  │
# └────────────────┴───────────┴──────────┴────────────────────────────┘
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
#
# **********************************************************************
# * Execucao apos alteracao para impressao dos dados do BD no terminal *
# **********************************************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie load assets/people.csv
# /Users/albertosoares/Projetos/dundiee-rewardss/dundie/cli.py:7:
# UserWarning: pkg_resources is deprecated as an API.
# See https://setuptools.pypa.io/en/latest/pkg_resources.html.
# The pkg_resources package is slated for removal as early as 2025-11-30.
# Refrain from using this package or pin to Setuptools<81.
# import pkg_resources  # captura a versao do projeto
#                    Dunder Mifflin Associates
# ┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ name           ┃ dept      ┃ role   ┃ created ┃ e-mail                   ┃
# ┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
# │ Jim Halpert    │ Sales     │Salesman│ True    │jim@dundlermifflin.com    │
# │ Dwight Schrute │ Sales     │ Manager│ True    │schrute@dundlermifflin.com│
# │ Gabe Lewis     │ Directory │ Manager│ True    │glewis@dundlermifflin.com │
# └────────────────┴───────────┴────────┴─────────┴──────────────────────────┘
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
#
# **********************************************************************
# * Execucao apos alteracao do registro do Gabe Lewis no BD de entrada *
# **********************************************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie load assets/people.csv
# /Users/albertosoares/Projetos/dundiee-rewardss/dundie/cli.py:7:
# UserWarning: pkg_resources is deprecated as an API.
# See https://setuptools.pypa.io/en/latest/pkg_resources.html.
# The pkg_resources package is slated for removal as early as 2025-11-30.
# Refrain from using this package or pin to Setuptools<81.
# import pkg_resources  # captura a versao do projeto
#                    Dunder Mifflin Associates
# ┏━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ name           ┃ dept    ┃ role     ┃ created ┃ e-mail                    ┃
# ┡━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
# │ Jim Halpert    │ Sales   │ Salesman │ False   │ jim@dundlermifflin.com    │
# │ Dwight Schrute │ Sales   │ Manager  │ False   │ schrute@dundlermifflin.com│
# │ Gabe Lewis     │ C-Level │ CEO.     │ False   │ glewis@dundlermifflin.com │
# └────────────────┴─────────┴──────────┴─────────┴─────────────────────────━─┘
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
