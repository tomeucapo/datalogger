#!/usr/bin/python

import serial
import time
import sys
from HermesComm import *
from HermesDrv import *


if __name__ == "__main__":
   try:
     portSerie = serial.Serial("/dev/tty.usbmodem1d11", "9600", timeout=2)
   except:
     print "Error al obrir el port serie!"
     sys.exit(-1)

   hermesC = HermesComm(portSerie)
   hermesD = HermesDrv(hermesC, "NEMOS")   
    
   if(hermesD.checkComm()):
      print "Hermes trobat"
   else:
      print "Error, no hem puc possar en contacte!"
      sys.exit(-1)

   if(hermesD.getInfo()):
      print "Llegida informacio ..."
      print hermesD.status
   else:
      print "Error al enviar la comanda getInfo!"
  

#   if(hermes.envia("3020081001000000")):
#      if(hermes.rebre()):
#        totOK = True
#        while ((hermes.lastResponse != "19") and (totOK)):
#              print hermes.lastResponse
#              totOK = hermes.rebre()
#
#        if(!totOK):
#          print "Hi ha hagut un error de transmissio!"
#
#      else:
#        print "Error al rebre la resposta!"
#   else:
#      print "Error al enviar la comanda!"

   portSerie.close()

   sys.exit(0)
