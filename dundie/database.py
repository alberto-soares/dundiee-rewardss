"""Module"""

import json
from datetime import datetime

from dundie.settings import DATABASE_PATH, EMAIL_FROM
from dundie.utils.email import check_valid_email, send_email
from dundie.utils.user import generate_simple_password

EMPTY_DB = {
    "people": {},
    "balance": {},
    "movement": {},
    "users": {},
}  #  estado inicial do BD


def connect() -> dict:  # retorna um dicionario
    """Connects to the database, returns dict data."""
    try:
        with open(DATABASE_PATH, "r") as database_file:
            return json.loads(database_file.read())
    except (json.JSONDecodeError, FileNotFoundError):
        return EMPTY_DB


def commit(db_):
    """Save db back to the database file."""

    if db_.keys() != EMPTY_DB.keys():
        raise RuntimeError("Database Schema is invalid.")

    with open(DATABASE_PATH, "w") as database_file:
        database_file.write(json.dumps(db_, indent=4))


def add_person(db_, pk, data):
    """Saves person data to database:

    - Email is unique (resolved by dictionary has table);
    - If exists, update, else create;
    - Set initial balance (managers = 100, others = 500);
    - Generate a password if user is new and send_email
    """

    if not check_valid_email(pk):
        raise ValueError(f"{pk} is not a valid email")

    table = db_["people"]
    person = table.get(pk, {})
    created = not bool(person)
    person.update(data)
    table[pk] = person
    if created:
        set_initial_balance(db_, pk, person)
        # password = generate_simple_password(8)
        password = set_initial_password(db_, pk)  # salva password BD
        send_email(EMAIL_FROM, pk, "Your dundie password", password)
        # TODO: Encrypt and send only line not password
    return person, created


def set_initial_password(db_, pk):
    """Generated and saves password."""
    db_["users"].setdefault(pk, {})
    db_["users"][pk]["password"] = generate_simple_password(8)
    return db_["users"][pk]["password"]


def set_initial_balance(db_, pk, person):
    """Add movement and set initial balance."""
    value = 100 if person["role"] == "Manager" else 500
    add_movement(db_, pk, value)


def add_movement(db_, pk, value, actor="system"):
    """Module"""
    #    try:
    #        movements = db_["movement"][pk]
    #    except KeyError:

    movements = db_["movement"].setdefault(pk, [])
    movements.append(
        {"date": datetime.now().isoformat(), "actor": actor, "value": value}
    )
    db_["balance"][pk] = sum([item["value"] for item in movements])


# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# ipython --profile=d5p08
# Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.
#
# IPython profile: d5p08
#
# In [1]: open("assets/database.json").read()
# Out[1]: '{\n    "people": {        \n        "joe@doe.com"
# {\n            "name": "Joe",\n            "role": "Salesman",\n
#             "dept": "Sales",\n            "active": true\n        },\n
#         "outro@usuario.com": {\n            "name": "Outro",\n
# "role": "Maneger",\n            "dept": "Sales",\n            "active": true
# \n        }\n    },\n
# "balance": {\n        "joe@doe.com": 500\n    },\n
#  "movement": {\n        "joe@doe.com": [\n            {"date": "",
# "value": 0}\n        ]\n    },\n    "user": {\n        "joe@doe.com": {\n
#             "password": "sdjfbsdjhfbsjhd",\n            "is_admin": false
# \n        }            \n    }\n}\n'
#
# In [2]: import json
#
# In [3]: json.loads(open("assets/database.json").read())
# Out[3]:
# {'people': {'joe@doe.com': {'name': 'Joe',
#   'role': 'Salesman',
#   'dept': 'Sales',
#   'active': True},
#  'outro@usuario.com': {'name': 'Outro',
#   'role': 'Maneger',
#   'dept': 'Sales',
#   'active': True}},
# 'balance': {'joe@doe.com': 500},
# 'movement': {'joe@doe.com': [{'date': '', 'value': 0}]},
# 'user': {'joe@doe.com': {'password': 'sdjfbsdjhfbsjhd', 'is_admin': False}}}
#
# In [4]: json.loads(open("assets/database.json").read())["people"]
# Out[4]:
# {'joe@doe.com': {'name': 'Joe',
#  'role': 'Salesman',
#  'dept': 'Sales',
#  'active': True},
# 'outro@usuario.com': {'name': 'Outro',
#  'role': 'Maneger',
#  'dept': 'Sales',
#  'active': True}}
#
# In [5]: json.loads(open("assets/database.json").read())["people"]["joe@doe.com"]
# Out[5]: {'name': 'Joe', 'role': 'Salesman', 'dept': 'Sales', 'active': True}
#
# In [6]: #  connect
#
# In [7]: db = json.loads(open("assets/database.json").read())
#
# In [8]: db
# Out[8]:
# {'people': {'joe@doe.com': {'name': 'Joe',
#   'role': 'Salesman',
#   'dept': 'Sales',
#   'active': True},
#  'outro@usuario.com': {'name': 'Outro',
#   'role': 'Maneger',
#   'dept': 'Sales',
#   'active': True}},
# 'balance': {'joe@doe.com': 500},
# 'movement': {'joe@doe.com': [{'date': '', 'value': 0}]},
# 'user': {'joe@doe.com': {'password': 'sdjfbsdjhfbsjhd', 'is_admin': False}}}
#
# In [9]: db["people"]["joe@doe.com"]
# Out[9]: {'name': 'Joe', 'role': 'Salesman', 'dept': 'Sales', 'active': True}
#
# In [10]: db["people"]["joe@doe.com"]["name"] = "Joe Doe"
#
# In [11]: db
# Out[11]:
# {'people': {'joe@doe.com': {'name': 'Joe Doe',
#   'role': 'Salesman',
#   'dept': 'Sales',
#   'active': True},
#  'outro@usuario.com': {'name': 'Outro',
#   'role': 'Maneger',
#   'dept': 'Sales',
#   'active': True}},
# 'balance': {'joe@doe.com': 500},
# 'movement': {'joe@doe.com': [{'date': '', 'value': 0}]},
# 'user': {'joe@doe.com': {'password': 'sdjfbsdjhfbsjhd', 'is_admin': False}}}
#
# In [12]: #  save, update
#
# In [13]: json.dumps(db)
# Out[13]: '{"people": {"joe@doe.com": {"name": "Joe Doe", "role": "Salesman",
#  "dept": "Sales", "active": true},
# "outro@usuario.com": {"name": "Outro", "role": "Maneger", "dept": "Sales",
# "active": true}}, "balance": {"joe@doe.com": 500},
# "movement": {"joe@doe.com": [{"date": "", "value": 0}]},
# "user": {"joe@doe.com": {"password": "sdjfbsdjhfbsjhd", "is_admin": false}}}'
#
# In [14]: json.dumps(db, indent=4)
# Out[14]: '{\n    "people": {\n        "joe@doe.com": {\n
#  "name": "Joe Doe",\n            "role": "Salesman",\n
#  "dept": "Sales",\n            "active": true\n        },\n
#  "outro@usuario.com": {\n            "name": "Outro",\n
#  "role": "Maneger",\n            "dept": "Sales",\n
#  "active": true\n        }\n    },\n    "balance": {\n
#  "joe@doe.com": 500\n    },\n    "movement": {\n        "joe@doe.com": [
#  \n            {\n                "date": "",\n                "value": 0\n
#             }\n        ]\n    },\n    "user": {\n        "joe@doe.com": {\n
#             "password": "sdjfbsdjhfbsjhd",\n            "is_admin": false\n
#         }\n    }\n}'
#
# In [15]: open("assets/database.json", "w").write(json.dumps(db, indent=4))
# Out[15]: 660
#
# In [17]: exit
#
# ******************************************************************
# * Testando dundie add --dept|--to --value=100 antes de criar add *
# ******************************************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie add 100 --email=jim@dundlermifflin.com
# /Users/albertosoares/Projetos/dundiee-rewardss/dundie/cli.py:7:
# UserWarning: pkg_resources is deprecated as an API.
# See https://setuptools.pypa.io/en/latest/pkg_resources.html.
# The pkg_resources package is slated for removal as early as
# 2025-11-30. Refrain from using this package or pin to Setuptools<81.
#  import pkg_resources  # captura a versao do projeto
#
# Usage: dundie [OPTIONS] COMMAND [ARGS]...
#
# Try 'dundie --help' for help
# ╭─ Error ─────────────────────────────────────────────────────────────╮
# │ No such command 'add'.                                              │
# ╰─────────────────────────────────────────────────────────────────────╯
#
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie add 100 --dept=Sales
# /Users/albertosoares/Projetos/dundiee-rewardss/dundie/cli.py:7:
# UserWarning: pkg_resources is deprecated as an API.
# See https://setuptools.pypa.io/en/latest/pkg_resources.html.
# The pkg_resources package is slated for removal as early as
# 2025-11-30. Refrain from using this package or pin to Setuptools<81.
#  import pkg_resources  # captura a versao do projeto
#
# Usage: dundie [OPTIONS] COMMAND [ARGS]...
#
# Try 'dundie --help' for help
# ╭─ Error ─────────────────────────────────────────────────────────────╮
# │ No such command 'add'.                                              │
# ╰─────────────────────────────────────────────────────────────────────╯
#
# ********************************************************************
# * Testando dundie show --dept|--to --value=100 antes de criar show *
# ********************************************************************
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# dundie show --dept=Sales
# /Users/albertosoares/Projetos/dundiee-rewardss/dundie/cli.py:7:
# UserWarning: pkg_resources is deprecated as an API.
# See https://setuptools.pypa.io/en/latest/pkg_resources.html.
# The pkg_resources package is slated for removal as early as
# 2025-11-30. Refrain from using this package or pin to Setuptools<81.
#  import pkg_resources  # captura a versao do projeto
#
# Usage: dundie [OPTIONS] COMMAND [ARGS]...
#
# Try 'dundie --help' for help
# ╭─ Error ─────────────────────────────────────────────────────────────╮
# │ No such command 'show'.                                             │
# ╰─────────────────────────────────────────────────────────────────────╯
#
