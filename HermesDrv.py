# -*- coding: iso-8859-1 -*-
#!/usr/bin/python


cmds = {"NEMOS": {"CHK_COMM": "40", "ASK_INFO": "43", "ASK_STATUS": "24",
                  "ASK_PASSWD": "55", "ASK_GETLOG": "30", "ASK_DELLOG": "57", "ADJ_DATEHO": "5C"},

        "TCR":   {"CHK_COMM": "", "ASK_INFO": ["54","52"], "ASK_STATUS": ["5D", "5F", "51"],
                  "ASK_PASSWD": "55", "ASK_GETLOG": "56", "ASK_DELLOG": "57", "ADJ_DATEHO": "5C"}}

RSP_COMM_ACK = "BF"
RSP_PASSWD_OK = "AA1"
RSP_PASSWD_ERR = "AA0"
RSP_SETDATEHO_OK = "A3"
RSP_DELLOG_ACK = "A81"
RSP_DELLOG_OK = "A80"

class HermesDrv:
      def __init__(self, hermesComm, tipus):
          self.equip = hermesComm
          self.info = []
          self.status = []
          self.tipus = tipus
          self.lastResult = []

      def __consulta__(self, peticions):
          self.lastResult = []
          retval = True

          for peticio in peticions:     
             if self.equip.envia(peticio):
                if self.equip.rebre():
                   if self.tipus == "TCR":
                      self.lastResult.append(self.equip.lastResponse)
                   else:
                      self.lastResult = self.equip.lastResponse.split(",") 
                else:
                   retval = False
             else:
                retval = False

          return(retval)

      # Comprova si hi ha comunicació amb l'equip

      def checkComm(self):
          retval = True

          if self.tipus == "TCR":
             pass          
          else:  
             if self.equip.envia(CHK_COMM):
                if self.equip.rebre():
                   retval = (self.equip.lastResponse == RSP_COMM_ACK)
                else:
                   retval = False
             else:
                retval = False

          return(retval)

      # Demana l'estat del dispositiu: Data/Hora, N. de registres del log, Tensió bateria, Cobertura GSM.

      def getStatus(self):
          retval = True
       
#          peticions = [ASK_STATUS]
     
#          if self.tipus == "TCR":
#             peticions = [ASK_DATEHO, ASK_NREGSD, ASK_GSMSTATUS]

          peticions = cmds[self.tipus]["ASK_STATUS"]
         
          if self.__consulta__(peticions):
             self.status = self.lastResult
          else: 
             retval = False

          return(retval)
 
      # Demana informació del dispositiu: Ver. Firmware, N. serie, ...

      def getInfo(self):
          retval = True
       
          peticions = cmds[self.tipus]["ASK_INFO"]
           
          if self.__consulta__(peticions):
             self.info = self.lastResult
          else: 
             retval = False

          return(retval)

      def setDateTime(self, data, hora):
          retval = True

          if self.equip.envia(ADJ_DATEHO+data+hora):
             if self.equip.rebre():
                retval=(self.equip.lastResponse == RSP_SETDATEHO_OK)
             else:
                retval=False
          else:
             retval=False

          return(retval)

      # Descarrega l'historic de l'equip.
          
      def downloadLog(self, data, hora):
          
          if self.tipus == "TCR":
             pass
             
          return(retval)

      def autenticate(self, passwd):
          retval = True

          if self.equip.envia(ASK_PASSWD+passwd):
             if self.equip.rebre():
                retval=(self.equip.lastResponse == RSP_PASS_OK)
             else:
                retval=False
          else:
             retval = False

          return(retval)


      
