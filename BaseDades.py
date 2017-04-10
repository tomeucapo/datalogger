# -*- coding: iso-8859-1 -*-

from PyQt4 import QtCore, QtSql, QtGui

def ConnectaDB():
    if not QtSql.QSqlDatabase.drivers().contains("QSQLITE"):
       return False
    else:
       db = QtSql.QSqlDatabase = QtSql.QSqlDatabase.addDatabase("QSQLITE")
       db.setDatabaseName("datalogger.db")
          
    if not db.open():
       return False
    else:
       return True
    
    
