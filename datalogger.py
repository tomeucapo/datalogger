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
# Last Modified: 31/12/2006
# Use under terms of GNU public licence.

import string
import time
import serial
import re
import sys
from PyQt4 import QtCore, QtGui

# Moduls especifics de l'aplicació

import Recursos
import BaseDades

from frmPrincipal import Ui_Datalogger
from Estacions import *
from Configurador import *
from DataloggerServer import *
from grafica import * 


################################################################################
# Datalogger GUI

class Datalogger(QtGui.QMainWindow):

    n_dades = 0
    num_regs = 0
    telefon = ''
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.ui = Ui_Datalogger()
        self.ui.setupUi(self)
	    
        self.dConfig = Configurador()
        self.__llegeixConfig__()
                   
        self.connect(self.ui.actionGuardar, QtCore.SIGNAL("triggered()"), self.onCmdGuardar)
        self.connect(self.ui.actionConfigurar, QtCore.SIGNAL("triggered()"), self.onCmdConfig)
        self.connect(self.ui.actionLlibreta, QtCore.SIGNAL("triggered()"), self.onCmdEstacions)
        self.connect(self.ui.actionAbout, QtCore.SIGNAL("triggered()"), self.onCmdAbout)
        self.connect(self.ui.actionConnectar, QtCore.SIGNAL("triggered()"), self.onCmdConnectar)
        self.connect(self.ui.actionDesconnectar, QtCore.SIGNAL("triggered()"), self.onCmdDesonnectar)
        self.connect(self.ui.actionDescarregar, QtCore.SIGNAL("triggered()"), self.onDescarregarSig)
        self.connect(self.ui.actionBorrarDatalogger, QtCore.SIGNAL("triggered()"), self.onCmdBuidarDatalogger)
        self.connect(self.ui.actionAjustar_Data, QtCore.SIGNAL("triggered()"), self.onCmdAjustarData)
        self.connect(self.ui.actionSortir, QtCore.SIGNAL("triggered()"), self.onCmdSortir)
       
        self.ui.actionAjustar_Data.setEnabled(0)
        self.ui.actionBorrarDatalogger.setEnabled(0)
        
        self.ui.b_progres.setRange(0, 100)
        self.ui.statusbar.showMessage("Off-Line")
        
        # Instanciam el servidor de peticions
        
        self.hermesSrv = DataloggerThread()
        
        self.connect(self.hermesSrv, QtCore.SIGNAL("ActualitzaBarra(int)"), self.ActualitzaBarra)  
        self.connect(self.hermesSrv, QtCore.SIGNAL("Desconnectat()"), self.Desconnectat) 
        self.connect(self.hermesSrv, QtCore.SIGNAL("onDescarregarSig()"), self.onDescarregarSig) 
        self.connect(self.hermesSrv, QtCore.SIGNAL("PintarDadesNode(const QString &, const QString &, int)"), self.PintarDadesNode) 
        self.connect(self.hermesSrv, QtCore.SIGNAL("PintarResultats(int)"), self.PintarResultats) 
        self.connect(self.hermesSrv, QtCore.SIGNAL("MostraMissatge(const QString &, int)"), self.MostraMissatge) 

        # Obrim el port serie
        
        self.hermesSrv.ObrirPort(self.COM_DEF, self.COM_VEL)

        if not BaseDades.ConnectaDB():
           QtGui.QMessageBox.critical(self, "No puc carregar la base de dades", "Aquest programa necessita el driver de SQLITE!")
           sys.exit(1)
        
        self.dEstacions = Estacions()       
   
        self.l_estacions = self.dEstacions.Llista()
        self.ui.c_estacions.addItems(self.l_estacions[0])
        
        self.graf = FinestraGrafica()
        self.ui.vboxlayout.addWidget(self.graf)

        
    def onCmdSortir(self):
        sys.exit(0)
        
    def __llegeixConfig__(self):
        self.COM_DEF = str(self.dConfig.settings.value("device").toString())
        self.COM_VEL = str(self.dConfig.settings.value("baud").toString())
        self.entrades_analog = int(self.dConfig.settings.value("entAnalog").toString())-1
        self.entrades_digit = int(self.dConfig.settings.value("entDigital").toString())-1
        self.modem_init = str(self.dConfig.settings.value("strInit").toString())
        self.modem_dial = str(self.dConfig.settings.value("strDial").toString())
        self.defineixTaula()

    def MostraMissatge(self, msg, tipus):
        if tipus == 0:
           QtGui.QMessageBox.critical(self,self.tr("Error"),msg)
        else:
           QtGui.QMessageBox.warning(self,self.tr("Avis"),msg)
           
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
           
    def onCmdEstacions(self):
        self.dEstacions.show()
        
    def onCmdAbout(self):
        QtGui.QMessageBox.information(self, self.tr("Sobre el programa ..."),
                                                    "HERMES Datalogger 2.2\nUtilitat per descarregar-se les dades del datalogger d'HERMES\n\nTomeu Capó Capó 2006 (C)")     

    ################################################################################
    # Mètodes per iniciar o bé aturar la comunicació
    
    def onCmdConnectar(self):
        
        if self.ui.c_rmt.isChecked():
           est_id = self.ui.c_estacions.currentIndex()
           
           self.telefon = str(self.l_estacions[1][est_id])
           clau = str(self.ui.c_clau.text())
                    
           if self.telefon == "":
              QtGui.QMessageBox.critical(self,self.tr("Error"),"Falta el número de telèfon!")
              return
              
           if clau == "":
              QtGui.QMessageBox.critical(self,self.tr("Error"),"Falta la clau d'access")
              return
           
           self.hermesSrv.ModemSett(self.telefon,  self.modem_init,  self.modem_dial)
           self.hermesSrv.TipusConn(GSM_MODE, clau)
        else:
           self.hermesSrv.TipusConn(LOCAL_MODE, '')
           
        self.ui.actionGuardar.setDisabled(1)
        self.ui.actionDesconnectar.setEnabled(1)
        self.ui.actionConnectar.setDisabled(1)
        self.ui.actionAjustar_Data.setDisabled(1)
        
        self.ui.statusbar.showMessage("Connectant ...")
        
        self.hermesSrv.CanviEstat(INIT_CONNECTION)
  
    def onCmdDesonnectar(self):
        self.hermesSrv.AturarConnexio()
        
    ################################################################################
    # Opció de desar el Log

    def onCmdGuardar(self):
        nom_fitxer = QtGui.QFileDialog.getSaveFileName(self,
                                                      self.tr("Fitxer destí per guardar el log"),
                                                      "%(any)d%(mes)02d%(dia)02d_data.txt" % {"any": time.localtime()[0], "mes": time.localtime()[1], "dia": time.localtime()[2]},
                                                      self.tr("All Files (*);;Text Files (*.txt)"))
        if not nom_fitxer.isEmpty():
           outFile = QtCore.QFile(nom_fitxer)
           if not outFile.open(QtCore.QFile.WriteOnly | QtCore.QFile.Text):
              QtGui.QMessageBox.critical(self,self.tr("Error"),"No puc escriure el fitxer!")
              return

           out = QtCore.QTextStream(outFile)
           out.setCodec("UTF-8")
           
           for registre in self.l_valors:
               out << linia_log(registre) << "\n"
               
           outFile.close()
 
    ################################################################################
    # Metode per descarregar les dades del datalogger
    
    def descarregar_dades(self): 
        self.ui.c_num_regs.setText("%(#)d" % {"#": self.num_regs})
        
        self.ui.actionDescarregar.setEnabled(1)
        self.ui.actionAjustar_Data.setEnabled(1)

        if self.num_regs > 0:           
           self.ui.actionBorrarDatalogger.setEnabled(1)
             
           contesta = QtGui.QMessageBox.question(self, self.tr("Pregunta?"),
                                                               "Hi ha %(r_totals)d registres per descarregar, vols descarregar-los?" % {"r_totals": self.num_regs}, 
                                                               QtGui.QMessageBox.Yes,
                                                               QtGui.QMessageBox.No) 
           if contesta == QtGui.QMessageBox.Yes:                                                   
              self.ui.t_resultat.setRowCount(self.num_regs)
              self.ui.statusbar.showMessage("Descarregant datalogger ...")
              
              # Descarregam les dades dins memoria 
              
              self.hermesSrv.CanviEstat(DOWNLOAD_DATA) 
        else:
           QtGui.QMessageBox.warning(self,self.tr("Avis"),"El datalogger estava buid i no s'ha baixat res!")
           self.ui.t_resultat.setRowCount(0)
           

    def onCmdBuidarDatalogger(self):
        contesta = QtGui.QMessageBox.question(self, self.tr("Pregunta?"),
                                                            "Vol buidar el datalogger?", QtGui.QMessageBox.Yes,
                                                             QtGui.QMessageBox.No)
        if contesta == QtGui.QMessageBox.Yes:
           self.hermesSrv.CanviEstat(FLUSH_DATA)
           
    def onCmdAjustarData(self):
        contesta = QtGui.QMessageBox.question(self, self.tr("Pregunta?"),
                                                            "Vol ajustar la data del datalogger amb la data del ordinador?", QtGui.QMessageBox.Yes,
                                                             QtGui.QMessageBox.No)
        if contesta == QtGui.QMessageBox.Yes:
           self.hermesSrv.CanviEstat(ADJUST_DATE)
           
    ################################################################################
    # Metode que es crida una vegada s'han tornat els resultats descarregats 
    # del datalogger.
    
    def PintarResultats(self, n_dades):
        self.ui.c_num_dades.setText("%(#)d" % {"#": n_dades})
        
        i=0
        for valors in self.hermesSrv.l_valors:
            self.ui.t_resultat.setItem(i, 0, QtGui.QTableWidgetItem(QtCore.QString(valors['data'])))
            self.ui.t_resultat.setItem(i, 1, QtGui.QTableWidgetItem(QtCore.QString(valors['hora'])))
            col=2                
            for v in valors['valors']:
                self.ui.t_resultat.setItem(i, col, QtGui.QTableWidgetItem(v))
                col = col + 1
            i = i + 1
         
        self.l_valors = self.hermesSrv.l_valors
        self.graf.AssignaValors(self.l_valors)
        
        # Si s'ha descarregat tot aleshores demanam per buidar-ho! 
        
        if n_dades < self.num_regs:
           QtGui.QMessageBox.warning(self,self.tr("Avis"),"No s'han descarregat tots els registres!")
        
        self.ui.actionGuardar.setEnabled(1)
        self.ui.statusbar.showMessage("On-Line")
    
    ################################################################################
    
    def ActualitzaBarra(self, valor):
        self.ui.b_progres.setValue(valor)
        
    def PintarDadesNode(self, num_serie, ver_firmware, n_regs):   
        self.ui.c_nserie.setText(num_serie)
        self.ui.c_vfirmware.setText(ver_firmware)
        self.num_regs = n_regs
         
        id_estacio = self.dEstacions.IdTelefon(self.telefon)
        if id_estacio != -1:
           dades = [num_serie, ver_firmware, time.strftime('%Y-%m-%d %H:%M:%S')]
           self.dEstacions.Actualitza(id_estacio, dades)
        
        self.descarregar_dades()
        
    def onDescarregarSig(self):
         self.ui.statusbar.showMessage("Llegint l'estat de l'Hermes ...")
       
         # Determinam el nombre de registres existents dins el Hermes,
         # el nombre de sèrie i la versió del Firmware.
         
         self.hermesSrv.CanviEstat(ANSWER_STATUS)
        
    def Desconnectat(self):
        self.ui.statusbar.showMessage("Off-Line")    
        self.ui.actionDesconnectar.setEnabled(0)
        self.ui.actionConnectar.setEnabled(1)
        self.ui.actionDescarregar.setEnabled(0)
        self.ui.actionAjustar_Data.setEnabled(0)
        self.ui.actionBorrarDatalogger.setEnabled(0)
        self.ui.b_progres.setValue(0)
           
              
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    d = Datalogger()
    d.show()
    sys.exit(app.exec_())
