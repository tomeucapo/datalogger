#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import sys
from PyQt4 import QtCore, QtGui
from frmConfigurador import Ui_frmConfigurador

class Configurador(QtGui.QDialog):
    
    val_conf = {}
    defaults = {"device":     "COM1",
                "baud":       "9600",
                "strInit":    "",
                "strDial":    "ATD",
                "entAnalog":  4,
                "entDigital": 8
               }
    
    def __init__(self):
        QtGui.QDialog.__init__(self)

        self.ui = Ui_frmConfigurador()
        self.ui.setupUi(self)

        self.settings = QtCore.QSettings("Can Botilla", "Datalogger")
        if not self.settings.contains("device"):
           for key in self.defaults.keys():
               self.settings.setValue(key, QtCore.QVariant(self.defaults[key]))
           QtGui.QMessageBox.information(self, self.tr("Benvingut"), "Es la primera vegada que possau en marxa aquesta aplicaci—\nhaur’a de revistar les preferncies")
           
        self.__carregar_camps__()
        
    def __carregar_camps__(self):
        self.ui.c_port.setEditText(self.settings.value("device").toString())
        self.ui.c_vel.setEditText(self.settings.value("baud").toString())
        self.ui.c_init.setText(self.settings.value("strInit").toString())
        self.ui.c_dial.setText(self.settings.value("strDial").toString())
        self.ui.c_analog.setText(self.settings.value("entAnalog").toString())
        self.ui.c_digit.setText(self.settings.value("entDigital").toString())
        
    def guardar(self):
        self.settings.setValue("device", QtCore.QVariant(self.ui.c_port.currentText()))
        self.settings.setValue("baud", QtCore.QVariant(self.ui.c_vel.currentText()))
        self.settings.setValue("strInit", QtCore.QVariant(self.ui.c_init.displayText()))
        self.settings.setValue("strDial", QtCore.QVariant(self.ui.c_dial.displayText()))
        self.settings.setValue("entAnalog", QtCore.QVariant(self.ui.c_analog.displayText()))
        self.settings.setValue("entDigital", QtCore.QVariant(self.ui.c_digit.displayText()))
