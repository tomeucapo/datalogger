#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
############################################################################
#
# datalogger.py
# Utilitat per descarregar el registre del datalogger de l'HERMES
#
# GUI API......: PyQt4. http://www.riverbankcomputing.co.uk/pyqt/index.php
# Serial API...: PySerial. http://pyserial.sourceforge.net/
#
# Author.......: Tomeu Capó Capó 2006 (C)
# Last Modified: 05/11/2006
# Use under terms of GNU public licence.

import string
import time
import serial
import re
import sys
from PyQt4 import QtCore, QtGui, QtSql

# Moduls especifics de l'aplicació

from frmPrincipal import Ui_Datalogger
from Configurador import *
from Hermes import *

import Recursos

class Datalogger(QtGui.QMainWindow):

    n_dades = 0
    num_regs = 0
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.ui = Ui_Datalogger()
        self.ui.setupUi(self)
	    
        self.dConfig = Configurador()
        self.__llegeixConfig__()
        
        if not QtSql.QSqlDatabase.drivers().contains("QSQLITE"):
           QtGui.QMessageBox.critical(self, "No puc carregar la base de dades", "Aquest programa necessita el driver de SQLITE!")
        else:
           db = QtSql.QSqlDatabase = QtSql.QSqlDatabase.addDatabase("QSQLITE")
           db.setDatabaseName("datalogger.db")
           if not db.open():
              QtGui.QMessageBox.critical(0, QtGui.qApp.tr("No puc obrir la base de dades"),
              QtGui.qApp.tr("Unable to establish a database connection.\n"
                            "This example needs SQLite support. Please read "
                            "the Qt SQL driver documentation for information "
                            "how to build it.\n\nClick Cancel to exit."),
              QtGui.QMessageBox.Cancel, QtGui.QMessageBox.NoButton)
              return False
           
           #query = QtSql.QSqlQuery()
           #query.exec_(" ")
           
        self.connect(self.ui.actionGuardar, QtCore.SIGNAL("triggered()"), self.onCmdGuardar)
        self.connect(self.ui.actionConfigurar, QtCore.SIGNAL("triggered()"), self.onCmdConfig)
        self.connect(self.ui.actionAbout, QtCore.SIGNAL("triggered()"), self.onCmdAbout)
        self.connect(self.ui.actionConnectar, QtCore.SIGNAL("triggered()"), self.connectar)
        self.connect(self.ui.actionDesconnectar, QtCore.SIGNAL("triggered()"), self.desconnectar)
        self.connect(self.ui.actionDescarregar, QtCore.SIGNAL("triggered()"), self.descarregar_dades)
	     
        self.ui.statusbar.showMessage("Off-Line")

        

    def __llegeixConfig__(self):
        self.COM_DEF = str(self.dConfig.settings.value("device").toString())
        self.COM_VEL = str(self.dConfig.settings.value("baud").toString())
        self.entrades_analog = int(self.dConfig.settings.value("entAnalog").toString())-1
        self.entrades_digit = int(self.dConfig.settings.value("entDigital").toString())-1
        self.modem_init = str(self.dConfig.settings.value("strInit").toString())
        self.modem_dial = str(self.dConfig.settings.value("strDial").toString())
        self.defineixTaula()
	    
    def defineixTaula(self):
        self.ui.t_resultat.setColumnCount(2+(self.entrades_analog+self.entrades_digit))
        self.ui.t_resultat.setRowCount(0)
        
        titols = ['Data', 'Hora']
        for ea in range(self.entrades_analog+1):
            titols.append('Analog. %(#)d' % {"#": ea})
       
        for ed in range(self.entrades_digit+1):
            titols.append('Digit. %(#)d' % {"#": ed})
       
        self.ui.t_resultat.setHorizontalHeaderLabels(titols)
            
    def onCmdConfig(self):
        if self.dConfig.exec_():
           self.dConfig.guardar()
           self.__llegeixConfig__()
           
    def onCmdAbout(self):
        QtGui.QMessageBox.information(self, self.tr("Sobre el programa ..."), "HERMES Datalogger 2.1\nUtilitat per descarregar-se les dades del datalogger d'HERMES\n\nTomeu Capó Capó 2006 (C)")     

    ################################################################################
    # Opció de desar el Log

    def onCmdGuardar(self):
        nom_fitxer = QtGui.QFileDialog.getSaveFileName(self,
                                                      self.tr("Fitxer destí per guardar el log"),
                                                      "%(any)d%(mes)02d%(dia)02d_data.txt" % {"any": time.localtime()[0], "mes": time.localtime()[1], "dia": time.localtime()[2]},
                                                      self.tr("All Files (*);;Text Files (*.txt)"))
        if not nom_fitxer.isEmpty():
           f = open(nom_fitxer,'w')
           
           for registre in self.l_valors:
               f.write(linia_log(registre)+"\n")
             
           f.close()

    ################################################################################
    # Mètodes per la connexió i la descarrega del datalogger

    def volcar_logger(self):
              
        inst_download = instruccio('560001%(analog)04x' % {"digit": self.entrades_digit, "analog": self.entrades_analog})
        try:
           self.ser.write(inst_download)
        except:
           QtGui.QMessageBox.critical(self, self.tr("Error"), "Error al enviar la petició de lectura del DataLogger")
 
        inst = rebre_instruccio(self.ser)
        i=0
        self.l_valors = []
        
        while inst != '#7A;A9':
              valors = interpreta_log(inst)
              self.ui.t_resultat.setItem(i, 0, QtGui.QTableWidgetItem(QtCore.QString(valors['data'])))
              self.ui.t_resultat.setItem(i, 1, QtGui.QTableWidgetItem(QtCore.QString(valors['hora'])))
              col=2
              for v in valors['valors']:
                  self.ui.t_resultat.setItem(i, col, QtGui.QTableWidgetItem(v))
                  col = col + 1

              self.l_valors.append(valors) 
              self.ui.b_progres.setValue(i*100/self.num_regs)
              self.ui.l_inst.setText(inst)
              
              inst = rebre_instruccio(self.ser)
              i = i + 1
        
        self.ui.b_progres.setValue(100)  
        return i
 
    def descarregar_dades(self):
        self.ui.statusbar.showMessage("Llegint dades ...")
        
        self.num_regs = num_registres(self.ser) 
        self.ui.c_num_regs.setText("%(#)d" % {"#": self.num_regs})
        
        if self.num_regs > 0:
           self.ui.actionDescarregar.setEnabled(1)
           
           contesta = QtGui.QMessageBox.question(self, self.tr("Pregunta?"),
                                                               "Hi ha %(r_totals)d registres per descarregar, vols descarregar-los?" % {"r_totals": self.num_regs}, QtGui.QMessageBox.Yes,
                                                               QtGui.QMessageBox.No,
                                                               QtGui.QMessageBox.Cancel) 
           if contesta == QtGui.QMessageBox.Yes:                                                   
              self.ui.t_resultat.setRowCount(self.num_regs)
              
              # Descarregam les dades dins memoria 
              self.n_dades = self.volcar_logger()
              self.ui.c_num_dades.setText("%(#)d" % {"#": self.n_dades})
               
              # Si s'ha descarregat tot aleshores demanam per buidar-ho! 
              if self.n_dades < self.num_regs:
                 QtGui.QMessageBox.warning(self,self.tr("Avis"),"No s'han descarregat tots els registres!")
              else:
                 self.ui.actionGuardar.setEnabled(1)
                 #QtGui.QMessageBox.information(self,self.tr("Info"),"S'han baixat %(r_baixat)d registre(s) de %(r_totals)d" % {"r_baixat": self.n_dades, "r_totals": self.num_regs})
                 contesta = QtGui.QMessageBox.question(self, self.tr("Pregunta?"),
                                                                     "Vol buidar el datalogger?", QtGui.QMessageBox.Yes,
                                                                     QtGui.QMessageBox.No,
                                                                     QtGui.QMessageBox.Cancel)
                 if contesta == QtGui.QMessageBox.Yes:
                    self.ser.write(instruccio('57'))
                    inst_resp = rebre_instruccio(self.ser)

                    if inst_resp == instruccio("A81"):
                       QtGui.QMessageBox.warning(self,self.tr("Avis"),"El datalogger s'ha buidat!")
                       self.ui.actionDescarregar.setEnabled(0)
                    else:
                       QtGui.QMessageBox.critical(self, self.tr("Error"),"No he pogut buidar-lo!")
        else:
           QtGui.QMessageBox.warning(self,self.tr("Avis"),"El datalogger estava buid i no s'ha baixat res!")
           self.ui.actionDescarregar.setEnabled(0)


    def connectar(self):
        if self.ui.c_rmt.isChecked():
           self.tipus_conn = 1
        else:
           self.tipus_conn = 2
           
        self.ui.actionGuardar.setDisabled(1)
        self.ui.b_progres.setRange(0, 100)
        telefon = str(self.ui.c_telef.displayText())
        
        try:
           self.ser = serial.Serial(self.COM_DEF, self.COM_VEL, timeout=2)
        except:
           QtGui.QMessageBox.critical(self, self.tr("Error"),"Error al obrir el port "+self.COM_DEF)
        else: 
           self.ui.actionConnectar.setDisabled(1)
           self.ui.statusbar.showMessage("Connectant ...")
           self.cont = False
           if self.tipus_conn == 2:
              for i in range(10):
                  self.ui.b_progres.setValue(i*100/10)
                  time.sleep(0.02)
                  linia = self.ser.readline()
                  if re.findall(r'GsmReady',linia):
                     self.cont = True
                     break
                  else:
                     if re.findall(r'GsmSimNotPresent',linia):
                        self.cont = True
                        QtGui.QMessageBox.warning(self,self.tr("Alerta!"),"L'Hermes no te la tarja SIM del GSM intal·lada!")
                        break
           else:
              if telefon == '':
                 QtGui.QMessageBox.critical(self,self.tr("Error"),"No ha possat un nombre de telèfon")
              else:
                 self.ui.statusbar.showMessage("Inicialitzant ...")
                 
                 self.ser.write(self.modem_init+"\r\n") 
                 print self.ser.readline()
		 
                 self.ui.statusbar.showMessage("Marcant "+telefon+" ...")
                 print "Marcant: "+self.modem_dial+telefon

                 try:
		            self.ser.write(self.modem_dial+telefon+"\r\n")
                 except:
	                print "Error enviant comanda AT al MODEM"
                 else:
                    self.ui.statusbar.showMessage("Esperant connexió ...");  
                    for i in range(30):
                        self.ui.b_progres.setValue(i*100/29)
                        if re.findall(r'CONNECT',self.ser.readline()):
                           self.ui.b_progres.setValue(100)
                           print "Connectat ..."
                           self.cont = True
                           break
                        else:
                           if re.findall(r'CARRIER',self.ser.readline()):
                              QtGui.QMessageBox.critical(self,self.tr("Error"),"No hi ha tò de marcatge") 
                              break
                    if self.cont:
                       self.ui.statusbar.showMessage("Autenticant ...");
                       print str(self.ui.c_clau.text())
                       
                       if not autenticar(self.ser, str(self.ui.c_clau.text())):
                          QtGui.QMessageBox.critical(self,self.tr("Error"),"La contrasenya no és correcte!")
                          self.cont = False
                    
           if self.cont: 
              self.ui.actionDesconnectar.setEnabled(1)
              self.ui.statusbar.showMessage("Llegint estat ...")
              
              # Determinam el nombre de registres existents dins el Hermes,
              # el nombre de sèrie i la versió del Firmware.
              
              self.ui.c_nserie.setText(numero_serie(self.ser))
              self.ui.c_vfirmware.setText(firmware_version(self.ser))
                            
              self.descarregar_dades()
              
           else:
              QtGui.QMessageBox.critical(self, self.tr("Error"),"No hem puc possar en contacte amb l'Hermes!")
              self.ser.close()
              self.ui.statusbar.showMessage("Off-Line")
              self.ui.actionConnectar.setEnabled(1)

           self.ui.b_progres.setValue(0)  
      
    def desconnectar(self):
        if self.cont:
           if self.tipus_conn == 2: 
              self.ser.write("+++\r")
              time.sleep(1)
              self.ser.write("ATH\r\n")
              
           self.ui.actionDesconnectar.setEnabled(0)
           self.ui.actionConnectar.setEnabled(1)
           self.ui.actionDescarregar.setEnabled(0)
           self.ui.b_progres.setValue(0)
           self.ser.close()
           
              
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    d = Datalogger()
    d.show()
    sys.exit(app.exec_())
