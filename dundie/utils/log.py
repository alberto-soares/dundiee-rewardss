import logging
import os
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()  # Formato de constante

# log = logging.Logger("dundie", LOG_LEVEL) => cada chamada cria nova instancia

log = logging.getLogger("dundie")  # reaproveita instancia existente

# ***********
# * ipython *
# ***********
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto dundiee-rewardss %
# ipython --profile=d4p11
# Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.
#
# IPython profile: d4p11
#
# In [1]: import logging
#
# In [2]: logging.getLogger?
# Signature: logging.getLogger(name=None)
# Docstring:
# Return a logger with the specified name, >>>> creating it if necessary. <<<<<
#
# If no name is specified, return the root logger.
# File:      ~/anaconda3/lib/python3.11/logging/__init__.py
# Type:      function
#
#         ****************
# In [3]: logging.Logger?
#         ****************
# Init signature: logging.Logger(name, level=0)
# Docstring:
# Instances of the Logger class represent a single logging channel. A
# "logging channel" indicates an area of an application. Exactly how an
# "area" is defined is up to the application developer. Since an
# application can have any number of areas, logging channels are identified
# by a unique string. Application areas can be nested (e.g. an area
# of "input processing" might include sub-areas "read CSV files", "read
# XLS files" and "read Gnumeric files"). To cater for this natural nesting,
# channel names are organized into a namespace hierarchy where levels are
# separated by periods, much like the Java or Python package namespace. So
# in the instance given above, channel names might be "input" for the upper
# level, and "input.csv", "input.xls" and "input.gnu" for the sub-levels.
# There is no arbitrary limit to the depth of nesting.
# Init docstring: Initialize the logger with a name and an optional level.
# File:           ~/anaconda3/lib/python3.11/logging/__init__.py
# Type:           type
# Subclasses:     RootLogger
#
# In [4]:
#

fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s "
    "l:%(lineno)d f:%(filename)s: %(message)s"
)


def get_logger(logfile="dundie.log"):
    """Returns a configured logger."""
    # ch = logging.StreamHandler()  # Console/terminal/stderr
    # ch.setLevel(log_level)
    fh = handlers.RotatingFileHandler(
        logfile,
        maxBytes=300,  # 10**6
        backupCount=10,
    )
    fh.setLevel(LOG_LEVEL)
    # ch.setFormatter(fmt)
    fh.setFormatter(fmt)
    # log.addHandler(ch)
    log.addHandler(fh)
    return log
