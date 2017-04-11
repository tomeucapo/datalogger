############################################################################
# Classe per operar amb el Hermes de Microcom
#
# Tomeu Cap— Cap— 2006 (C)

import serial

class Hermes:
      buffer = '';
      
      def __init__(self, device, baud):
          self.device = device
          self.baud = baud
          self.buffer = ''
          self.online = False

      def Connectar(self, tipus):
          try:
             self.ser = serial.Serial(self.device, self.baud, timeout=2)
             conectat = True
          except:
             conectat = False

          retval = False
          
          if conectat:
             if tipus == 2:
                for i in range(10):
                    time.sleep(0.02)
                    if re.findall(r'GsmReady',ser.readline()):
                       retval = True
                       break
             else:
                print "Inicialitzant ..."
                
                self.ser.write(self.modem_init+"\r\n");
                
                print self.ser.readline() 
                print "Marcant ... (Fins a 30 segons d'espera mˆxima)"
           
                self.ser.write(self.modem_dial+self.telef+"\r\n")
                 
                for i in range(30):
                    if re.findall(r'CONNECT',self.ser.readline()):
                       print "Connectat ..."
                       retval = True
                       break
                    else:
                       if re.findall(r'CARRIER',self.ser.readline()): 
                          break
                          
          self.online = retval
          return retval
          
      def Desconnectar(self):
          if(self.online)
             self.ser.close()
      
      # Ens formata la instruccio que nosaltres volguem enviar
      # calculant el seu checksum.
          
      def instruccio(self, cmd):
          chksum=0
          for c in cmd:
              chksum+=ord(c)
          chksum=chksum%256
          c="%(#)02x" % {"#": chksum}
          cmd="#"+c+";"+cmd+"\r"
          return cmd

      # Funcio que reb la proxima trama
       
      def rebre(self):
          c = self.ser.read()
          while c != '#':
                c = self.ser.read()
   
          inst = ''
          while c != '\r':
                inst += c
                c = self.ser.read()
           
          self.buffer = inst
          return inst
    
      def envia(self, cmd):
          try:
             self.ser.write(instruccio(cmd))
             retval = true
          except:
             print "Error al enviar la comanda!"
             retval = false
             
          return retval   

      # Funcio per autentificar-se contra el Hermes

      def autenticar(self, passwd):
        
          self.envia("55"+passwd)
        
          r = self.rebre()
          if r[4:] == "AA1":
             return True
          else:  
             return False

      def numero_serie(self):
          self.envia('52')
          
          r = self.rebre()
          return r[6:]
    
      def firmware_version(self):
          self.envia('54')
    
          r = self.rebre()
          return r[6:]
    
      def num_registres(self):
          self.envia('5F')
    
          r = self.rebre()
          num_regs = int("0x"+r[6:],16)-1
       
          return num_regs
    
      # Ens interpreta la resposta de la peticio de baixar-se les dades del
      # datalogger.

      def interpreta_log(self, inst):
          txt_valors=''
          valors = inst[27:]
    
          ret_vals = {}
          ret_vals["data"] = "%(dia)s/%(mes)s/%(any)s" % {"dia": inst[18:20], "mes": inst[16:18], "any": inst[14:16]}
          ret_vals["hora"] = "%(hora)s:%(min)s:%(seg)s" % {"hora": inst[20:22], "min": inst[22:24], "seg": inst[24:26]}
          ret_vals["valors"] = []
    
          for v in valors.split(';'):
              ret_vals['valors'].append("%(val)s" % {"val": v[1:]})
    
          return ret_vals

      # Funció per generar una linia de text a partir de les dades del log 

      def linia_log(self, l_valors):
          txt_valors = ''
          for v in l_valors['valors']:
              txt_valors += "%(val)s\t" % {"val": v}
    
          linia="%(data)s\t%(hora)s\t%(valors)s" % \
                {"data": l_valors['data'], "hora": l_valors['hora'], "valors": txt_valors}
       
          return linia    
