######################################
# Script per la creació de la dist
# per win32 amb py2exe.
#
# Tomeu Capó 2007 (C)
#
# cmd:
# python setup.py py2exe --includes sip

from py2exe.build_exe import py2exe
from distutils.core import setup

setup(
      #windows =  ["datalogger.py"],
      console=[{"script": "datalogger.py"}],
      data_files = [("", ["datalogger.db",]),
                    ("sqldrivers", ["qsqlite.dll",])],
      )
