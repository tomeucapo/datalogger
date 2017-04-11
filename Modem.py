class Modem:
     
      def __init__(self, serial):
          self.ser = serial
      
      def InitString(self, initStr):
          self.initStr = initStr
          
      def DialString(self, dialStr):
          self.dialStr = dialStr
      
      def Dial(self, n_telef):
          print "Inicialitzant ..."
                
          self.ser.write(self.initStr+"\r\n");
                
          print self.ser.readline() 
          print "Marcant ... (Fins a 30 segons d'espera mˆxima)"
           
          self.ser.write(self.dialStr+n_telef+"\r\n")
                 
          for i in range(30):
              if re.findall(r'CONNECT',self.ser.readline()):
                 print "Connectat ..."
                 retval = True
                 break
              else:
                 if re.findall(r'CARRIER',self.ser.readline()): 
                    break
                          
          return retval