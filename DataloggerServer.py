# -*- coding: iso-8859-1 -*-
############################################################################
#
# DataloggerServer.py
# Thread que gestiona de manera concurrent les petions del programa al HERMES
#
# Author.......: Tomeu Capó Capó 2006 (C)
# Last Modified: 29/03/2007
# Use under terms of GNU public licence.

import string
import time
import serial
import re
import sys
from PyQt4 import QtCore
from Hermes import *

# Els estats del thread

INIT_CONNECTION  = 1     # Iniciar la comunicació
DOWNLOAD_DATA    = 3     # Descarregar les dades del datalogger
ANSWER_STATUS    = 4     # Demanar l'estat del Hermes
FLUSH_DATA       = 5     # Buidar el datalogger
ADJUST_DATE      = 6


LOCAL_MODE       = 1
GSM_MODE         = 2

class DataloggerThread(QtCore.QThread):


      def __init__(self, parent=None):
          QtCore.QThread.__init__(self, parent)

          self.mutex = QtCore.QMutex()
          self.condition = QtCore.QWaitCondition()
          self.restart = False
          self.abort = False      
          self.estat = 99
          self.max_regs = 0
          self.port_obert = False
		  
      def __del__(self):
          self.mutex.lock()
          self.conn = True
          self.condition.wakeOne()
          self.mutex.unlock()

          self.wait()

      def ObrirPort(self, dsp, vel):
          try:
             self.ser = serial.Serial(dsp, vel, timeout=2)
             self.port_obert = True
          except:
             self.emit(QtCore.SIGNAL("MostraMissatge(const QString &, int)"), "Error al obrir el port "+dsp,0)
             self.emit(QtCore.SIGNAL("Desconnectat()"))
                     
      def TipusConn(self, tipus_con, clau):
          self.tipus_conn = tipus_con
          self.clau_access = clau
      
      def ModemSett(self, telefon, str_init, str_dial):
          self.modem_init = str_init
          self.modem_dial = str_dial
          self.telefon = telefon
          
      #########################################################################
      # Metode que serveix per dir el que ha de fer el thread
      
      def CanviEstat(self, estat):
          locker = QtCore.QMutexLocker(self.mutex)

          self.estat = estat

          if not self.isRunning():
             self.start(QtCore.QThread.LowPriority)
          else:
             self.restart = True
             self.condition.wakeOne()

      ########################################################################
      # Mètode per a la descarrega de l'historic del datalogger
      
      def __Descarregar__(self):          
          inst_download = instruccio('5600010003')
          try:
              self.ser.write(inst_download)
          except:
              self.emit(QtCore.SIGNAL("MostraMissatge(const QString &, int)"), "Error al enviar la petici— de lectura del DataLogger",0)
              return
              
          inst = rebre_instruccio(self.ser)
          i=0
          self.l_valors = []
        
          while inst != '#7A;A9':
                if self.abort: 
                   self.abort = False
                   self.emit(QtCore.SIGNAL("MostraMissatge(const QString &, int)"), "Descarrega abortada",0)
                   return 0
                    
                valors = interpreta_log(inst)
                self.emit(QtCore.SIGNAL("ActualitzaBarra(int)"), i*100/self.num_regs)
                self.l_valors.append(valors) 

                inst = rebre_instruccio(self.ser)
                i = i + 1
          
          self.emit(QtCore.SIGNAL("ActualitzaBarra(int)"), 100)
          return i

      ########################################################################
      # Metode per iniciar la comunicació amb l'Hermes
      # tant local com a remota, depenent del atribut tipus_conn
      
      def __IniciarComunicacio__(self):
          # Mirar el tipus de commucacio que hem d'establir 
          # local o bŽ per GSM

          estat_conn = False

          if self.tipus_conn == LOCAL_MODE:
             print "Connectant ..."
                  
             self.mutex.lock()
             self.abort = False
             self.mutex.unlock()
             
             ##################################################################
             # Detecció d'Hermes en local (timeout = 10*2us)
                      
             for i in range(10): 
                 if self.abort: 
                    self.abort = False
                    print "Abortat!"
                    return
                 else:
                    self.usleep(2)
                             
                 self.emit(QtCore.SIGNAL("ActualitzaBarra(int)"), i*100/10)
                          
                 linia = self.ser.readline()
                 if re.findall(r'(GsmInit|GsmReady|GsmSimNotPresent)',linia):
                    estat_conn = True
                    break                 
          else:                      
             ##################################################################
             # Connexió via modem GSM (timeout = 30sec aprox)
             
             self.ser.write(self.modem_init+"\r\n")
             print self.ser.readline()
             
             print "Marcant: "+self.modem_dial+self.telefon

             try:
                 self.ser.write(self.modem_dial+self.telefon+"\r\n")
             except:
                 print "Error enviant comanda AT al MODEM"
             else:
                 #self.ui.statusbar.showMessage("Esperant connexi— ...");  
                 for i in range(40):
                     linia = self.ser.readline()
                     if re.findall(r'CONNECT',linia):
                        self.emit(QtCore.SIGNAL("ActualitzaBarra(int)"), 100)
                        print "Connectat ..."
                        estat_conn = True
                        break
                     else:
                        if re.findall(r'CARRIER',linia):
                           self.emit(QtCore.SIGNAL("MostraMissatge(const QString &, int)"), "No hi ha tò de marcatge", 0)
                           self.emit(QtCore.SIGNAL("Desconnectat()")) 
                           break

                     if self.abort: 
                        self.abort = False
                        print "Abortat!"
                        return
                             
                     self.emit(QtCore.SIGNAL("ActualitzaBarra(int)"), i*100/39)
            
                 if estat_conn:
                    print "Autenticant ..."
                    print self.clau_access
                    if not autenticar(self.ser, self.clau_access):
                       self.emit(QtCore.SIGNAL("MostraMissatge(const QString &, int)"), "La contrasenya no és correcte!", 0)
                       self.emit(QtCore.SIGNAL("Desconnectat()")) 
                       estat_conn = False      

          return estat_conn
      
      ###################################################################
      # Metode que atura de connexió actual
      
      def AturarConnexio(self):
          if self.isRunning() and self.port_obert:             
             if self.tipus_conn == GSM_MODE:
                self.ser.write("+++\r\n")
                print "Desconnectant ..."
                for i in range(10):
                    linia = self.ser.readline()
                    if re.findall(r'OK',linia):
                       self.ser.write("ATH\r\n")
                       linia = self.ser.readline()
                       break
                  
             self.mutex.lock()
             self.abort = True
             self.mutex.unlock()

             self.emit(QtCore.SIGNAL("Desconnectat()")) 
             
      def __InitConnection__(self):
          # Detecció de l'Hermes
          self.cont = self.__IniciarComunicacio__()
 
          if self.cont:
             self.emit(QtCore.SIGNAL("ActualitzaBarra(int)"), 100)
             self.emit(QtCore.SIGNAL("onDescarregarSig()"), 0)
             print "Connectat!"
          else:
             self.emit(QtCore.SIGNAL("MostraMissatge(const QString &, int)"), "No hem puc possar en contacte amb l'Hermes", 0)
             self.emit(QtCore.SIGNAL("Desconnectat()")) 
             print "No contesta!" 
             
      def __DownloadData__(self):
          print "Descarregant ..."
          self.n_dades = self.__Descarregar__()
          self.emit(QtCore.SIGNAL("PintarResultats(int)"), self.n_dades)    
          
      def __AnswerStatus__(self):
          print "*** Demanant estat ..."
          n_serie = numero_serie(self.ser)
          v_firmw = firmware_version(self.ser)
          self.num_regs = num_registres(self.ser) 
          print "*** Numero de registres %(#)d" % {"#": self.num_regs}                            
          self.emit(QtCore.SIGNAL("PintarDadesNode(const QString &, const QString &, int)"), n_serie, v_firmw, self.num_regs)
                            
          print "*** Demanant data i hora del Hermes"
          any_actual = str(time.localtime()[0])
          data_actual = "%(dia)02d/%(mes)02d/%(any)s" % {"any": any_actual[2:4], "mes": time.localtime()[1], "dia": time.localtime()[2]}
                            
          data_hermes = demana_data(self.ser)
          print data_hermes, data_actual
          if data_hermes != data_actual:
             print "Les dates del sistema i de l'Hermes són diferents!"
			             
      def __FlushData__(self):
          print "Buidar datalogger"
          self.ser.write(instruccio('57'))
          inst_resp = rebre_instruccio(self.ser)
          if inst_resp[4:7] == "A80":
             self.sleep(1)
             inst_resp = rebre_instruccio(self.ser)
             if inst_resp[4:7] == "A81":
                self.emit(QtCore.SIGNAL("MostraMissatge(const QString &, int)"), "El datalogger s'ha buidat!", 1)
      
      def __AdjustDate__(self):
          print "Ajustar el rellotge del Hermes"
          data_sistema = time.strftime('%y%m%d%H%M%S')
          adjustar_data(self.ser, data_sistema)
          
          
      ###################################################################
      # Metode principal d'execució del thread que processa les peticions
      
      def errorestat(self):
          print "[SRV] Estat incorrecte"
      
      
      d_accions = {INIT_CONNECTION: __InitConnection__,
                   DOWNLOAD_DATA: __DownloadData__,
                   ANSWER_STATUS: __AnswerStatus__,
                   FLUSH_DATA: __FlushData__,
                   ADJUST_DATE: __AdjustDate__}
                   
      def run(self):
          while True:
                if not self.port_obert:
                   self.emit(QtCore.SIGNAL("MostraMissatge(const QString &, int)"), "El port de comunicacions no esta obert!",0)
                   self.emit(QtCore.SIGNAL("Desconnectat()"))  
                   return
                 
                print "[SRV] Rebuda ordre => "+str(self.estat)

                self.d_accions.get(self.estat, self.errorestat)(self)
                           
                self.mutex.lock()
                if not self.restart:
                   self.condition.wait(self.mutex)
                self.restart = False
                self.mutex.unlock()
