# -*- coding: iso-8859-1 -*-
############################################################################
#
# HermesComm.py
# Classe per comunicarse amb els equips de Microcom, implementa el protocol
# de comunicacions. Per comunicar-se fa falta el HermesComm+HermesDrv.
#
# Tomeu Capó 2008 (C)
#

import time
import serial

TOUT_RX = 2
E_OK = 0
E_NOT_RESPONSE = 1
E_CHKSUM_ERROR = 2
E_SND_ERROR = 3

STX = "#"
ETX = "\r"

class HermesComm:
      def __init__(self, dspSerie):
          self.serie = dspSerie
          self.lastCmd = ''
          self.lastResponse = ''
          self.lastError = E_OK

      def envia(self, cmd):
          retval = True

          if self.serie.isOpen():
             chksum = reduce(lambda x,y:x+y, [ord(c) for c in cmd])%256
             sndtxt = STX+"%(chk)02X;%(cmd)s%(etx)s" % {"chk": chksum, "cmd": cmd, "etx": ETX}
 
             try:
                print "[ TX ] "+sndtxt[:-1]
                self.serie.write(sndtxt)
                self.lastCmd = cmd
                self.lastError = E_OK
             except:
                retval = False
                self.lastError = E_SND_ERROR
          else:
             self.lastError = E_SND_ERROR

          return(retval)

      def rebre(self):
         retval = True

         if self.serie.isOpen():
            c = self.serie.read()

            sTime = time.time()
            while c != STX:
                  if time.time()-sTime < TOUT_RX:
                     c = self.serie.read()
                  else:
                     self.lastError = E_NOT_RESPONSE
                     return False

            inst = ''
            chkRx = ''
            while c != ETX:
                  inst += c
                  c = self.serie.read()             

            chkRx = int("0x"+inst[1:3],16)
            frameRx = inst[4:]
            chkCa = reduce(lambda x,y: x+y, [ord(c) for c in frameRx])%256

            if chkRx != chkCa:
               retval = False
               self.lastError = E_CHKSUM_ERROR
            else:
               self.lastResponse = frameRx
               self.lastError = E_OK
         
            print "[ RX ] "+inst
         else:
            retval = False

         return(retval)
             
