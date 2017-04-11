#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

############################################################################
#
# datalogger.py
# Utilitat per descarregar el registre del datalogger de l'HERMES
#
# GUI API......: FXPy. http://fxpy.sourceforge.net/
# Serial API...: PySerial. http://pyserial.sourceforge.net/
#
# Author.......: Tomeu Capó Capó 2006 (C)
# Last Modified: 03/10/2006
# Use under terms of GNU public licence.

from FXPy.fox import *
import string
import time
import serial
import re
import sys

# Moduls propis de l'aplicacio

from Configurador import *
from Llibreta import *
from Hermes import * 

############################################################################
# Definicio de la GUI del programa
                 
# Definicio de la finestra principal

class Datalogger(FXMainWindow):
    ID_CONNECTAR = FXMainWindow.ID_LAST
    ID_CONN_LOCAL = ID_CONNECTAR + 1
    ID_CONN_REMOT = ID_CONN_LOCAL + 1
    ID_VALUE = ID_CONN_REMOT + 1
    ID_ABOUT = ID_VALUE + 1
    ID_BOOKMARK = ID_ABOUT + 1
    ID_GUARDAR = ID_BOOKMARK + 1
    ID_CONFIG = ID_GUARDAR + 1
    ID_BUIDAR = ID_CONFIG + 1
    n_dades = 0
    num_regs = 0
    
    def __init__(self, app):
        FXMainWindow.__init__(self, app, "Hermes Datalogger 2.0",w=597,h=580)

        self.dlg_config = Configurador(self)
        self.dlg_llibreta = Llibreta(self)
        
        val_conf = self.dlg_config.val_conf
        self.COM_DEF = val_conf["disp"]
        self.COM_VEL = val_conf["baud"]
        self.entrades_analog = int(val_conf["max_ent_analog"])-1
        self.entrades_digit = int(val_conf["max_ent_digit"])-1
        self.modem_init = val_conf["modem_init"]
        self.modem_dial = val_conf["modem_dial"]
        
        self.progressTarget = FXDataTarget(0)
        self.analogTarget = FXDataTarget(self.entrades_analog)
        self.digitalTarget = FXDataTarget(self.entrades_digit)
       
        # Message map
        FXMAPFUNC(self, SEL_COMMAND, Datalogger.ID_CONNECTAR, Datalogger.connectar)
        FXMAPFUNC(self, SEL_COMMAND, Datalogger.ID_CONN_LOCAL, Datalogger.onConnLocal)
        FXMAPFUNC(self, SEL_COMMAND, Datalogger.ID_CONN_REMOT, Datalogger.onConnRemot)
        FXMAPFUNC(self, SEL_COMMAND, Datalogger.ID_ABOUT, Datalogger.onCmdAbout)
        FXMAPFUNC(self, SEL_COMMAND, Datalogger.ID_GUARDAR, Datalogger.onCmdGuardar)
        FXMAPFUNC(self, SEL_COMMAND, Datalogger.ID_BOOKMARK, Datalogger.onCmdLlibreta)
        FXMAPFUNC(self, SEL_COMMAND, Datalogger.ID_CONFIG, Datalogger.onCmdConfig)
        FXMAPFUNC(self, SEL_COMMAND, Datalogger.ID_BUIDAR, Datalogger.onCmdBuidarReg)

        # Menubar
        menubar = FXMenubar(self,LAYOUT_SIDE_TOP|LAYOUT_FILL_X)

        # Separator
        FXHorizontalSeparator(self,LAYOUT_SIDE_TOP|LAYOUT_FILL_X|SEPARATOR_GROOVE)

        # File Menu
        filemenu = FXMenuPane(self)
        self.opc_guardar = FXMenuCommand(filemenu, "&Guardar", None, self, self.ID_GUARDAR, 0)
        self.opc_guardar.disable()
        FXMenuCommand(filemenu, "&Llibreta", None, self, self.ID_BOOKMARK, 0)
        FXMenuCommand(filemenu, "&Configurar", None, self, self.ID_CONFIG, 0)
        FXMenuSeparator(filemenu)
        FXMenuCommand(filemenu,"&Sortir",None,self.getApp(),FXApp.ID_QUIT,0)
        FXMenuTitle(menubar,"&Fitxer",None,filemenu)

        helpmenu = FXMenuPane(self)
        FXMenuCommand(helpmenu, "&Sobre el programa", None, self, self.ID_ABOUT)
        FXMenuTitle(menubar, "&Ajuda", None, helpmenu, LAYOUT_RIGHT)

        # Frame general (Vertical)
        conten1 = FXVerticalFrame(self,LAYOUT_SIDE_TOP|FRAME_NONE|LAYOUT_FILL_X|LAYOUT_FILL_Y)
 
        # Sub-frame 
        contents = FXVerticalFrame(conten1,LAYOUT_SIDE_TOP|FRAME_NONE|LAYOUT_FILL_X|LAYOUT_FILL_Y)  
        cont_ctrls = FXHorizontalFrame(contents,LAYOUT_SIDE_TOP|FRAME_NONE|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        cont_entra = FXHorizontalFrame(contents,LAYOUT_SIDE_TOP|FRAME_NONE|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        
        ####################################################################
        # Selecció del tipus de connexió
        
        gp = FXGroupBox(cont_ctrls,'Connexió',LAYOUT_SIDE_TOP|FRAME_GROOVE|LAYOUT_FILL_X|LAYOUT_FILL_Y, 0,0,0,0)
        c_local = FXRadioButton(gp,"Local",self, self.ID_CONN_LOCAL)
        c_local.setCheck(True)
        c_rmt = FXRadioButton(gp,"Remota", self, self.ID_CONN_REMOT)
        self.b_conn = FXButton(gp,"Connectar",None,self,self.ID_CONNECTAR,FRAME_RAISED|FRAME_THICK|LAYOUT_CENTER_X|LAYOUT_CENTER_Y)

        ####################################################################
        # Paràmetres de l'estació remota
        
        gp2 = FXGroupBox(cont_ctrls,'Estació',LAYOUT_SIDE_TOP|FRAME_GROOVE|LAYOUT_FILL_X|LAYOUT_FILL_Y, 0,0,0,0)
        
        matrix = FXMatrix(gp2, 4, MATRIX_BY_COLUMNS|LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        
        FXLabel(matrix, "N. Telèfon:", None, LAYOUT_RIGHT)
        self.c_telef = FXTextField(matrix, 20, opts=JUSTIFY_LEFT|LAYOUT_RIGHT|FRAME_SUNKEN|FRAME_THICK)
        self.c_telef.disable()       
        
        FXLabel(matrix, "Clau access:", None, LAYOUT_RIGHT)
        self.c_clau = FXTextField(matrix,10,opts=JUSTIFY_LEFT|FRAME_SUNKEN|FRAME_THICK|LAYOUT_RIGHT|TEXTFIELD_PASSWD)
        self.c_clau.disable()
        
        FXLabel(matrix, "", None, LAYOUT_LEFT)
        FXLabel(matrix, "", None, LAYOUT_LEFT)
        FXLabel(matrix, "", None, LAYOUT_LEFT)
        FXLabel(matrix, "", None, LAYOUT_LEFT)
        
        FXLabel(matrix, "N. de sèrie:", None, LAYOUT_RIGHT)
        self.c_nserie = FXLabel(matrix, "", None, LAYOUT_LEFT)
        FXLabel(matrix, "Ver. firmware:", None, LAYOUT_RIGHT)
        self.c_vfirmware = FXLabel(matrix, "", None, LAYOUT_LEFT)

        FXLabel(matrix, "Nº total de regs.:", None, LAYOUT_LEFT)
        self.c_num_regs = FXLabel(matrix, "         ", None, LAYOUT_LEFT)        
        FXLabel(matrix, "Regs. descarregats:", None, LAYOUT_LEFT)
        self.c_num_dades = FXLabel(matrix, "         ", None, LAYOUT_LEFT)
        
        ####################################################################
        # Selectors d'entrades analògiques/digitals
        
        g_ent_analog = FXGroupBox(cont_entra,'Consulta d\'entrades',LAYOUT_SIDE_TOP|FRAME_GROOVE|LAYOUT_FILL_X|LAYOUT_FILL_Y, 0,0,0,0)
        
        cont_ent = FXHorizontalFrame(g_ent_analog,LAYOUT_SIDE_TOP|FRAME_NONE|LAYOUT_FILL_X)
        
        self.analog = FXSpinner(cont_ent, 5, self.analogTarget, FXDataTarget.ID_VALUE, FRAME_SUNKEN|FRAME_THICK|LAYOUT_CENTER_Y|LAYOUT_FILL_ROW)
        self.analog.setRange(0,self.entrades_analog)
        
        self.digital = FXSpinner(cont_ent, 5, self.digitalTarget, FXDataTarget.ID_VALUE, FRAME_SUNKEN|FRAME_THICK|LAYOUT_CENTER_Y|LAYOUT_FILL_ROW)
        self.digital.setRange(0,self.entrades_digit)

        self.b_buidar = FXButton(cont_ent,"Buidar registre",None,self,self.ID_BUIDAR,FRAME_RAISED|FRAME_THICK|LAYOUT_CENTER_X|LAYOUT_CENTER_Y)        

        ####################################################################
        # Taula de resultats 
        
        self.t_resultat = FXTable(conten1, 10, 8, None, 0, LAYOUT_FILL_X|LAYOUT_FILL_Y, 0,0,0,0, 2,2,2,2)
        self.defineixTaula()
        self.t_resultat.setLeadingRows(1)
        
        ####################################################################
        # Etiqueta per saber la darrera instrucció llegida i la barra
        # d'estat.
        
        self.l_inst = FXLabel(conten1, "  ", None, LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|FRAME_SUNKEN|FRAME_THICK)
        self.b_progres = FXProgressBar(conten1, opts=LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|FRAME_SUNKEN|FRAME_THICK)
        self.b_progres.showNumber()
        self.b_progres.setTotal(100)
       
        self.Estat = FXStatusline(conten1, None, 0)
        self.Estat.setNormalText("Off-line")
        self.Estat.setWidth(40)      

    
    def defineixTaula(self):
        self.t_resultat.setTableSize(1,2+(self.entrades_analog+self.entrades_digit))
       
        titols = ['Data', 'Hora']
        for ea in range(self.entrades_analog):
            titols.append('Analog. %(#)d' % {"#": ea})
       
        for ed in range(self.entrades_digit):
            titols.append('Digit. %(#)d' % {"#": ed})
       
        col = 0
        for titol in titols:
            self.t_resultat.setItemText(0, col, titol)
            col = col + 1
            
    ################################################################################
    # Opció de desar el Log

    def onCmdGuardar(self, sender, sel, ptr):
        if self.n_dades > 0:
           d_guardar = FXFileDialog(self, "Fitxer destí per guardar el log")
           d_guardar.setFilename("%(any)d%(mes)02d%(dia)02d_data.txt" % {"any": time.localtime()[0], "mes": time.localtime()[1], "dia": time.localtime()[2]});
           
           if d_guardar.execute():
              f=open(d_guardar.getFilename(),'w')
           
              for registre in self.l_valors:
                  f.write(linia_log(registre)+"\n")
              
              f.close()
        else:
           showModalInformationBox(self,MBOX_OK, "Avis","Encara no s'ha baixat res per guardar-ho!")        
        
    def onCmdAbout(self, sender, sel, ptr):
        showModalInformationBox(self,MBOX_OK, "Sobre el programa","HERMES Datalogger 2.0\nUtilitat per descarregar-se les dades del datalogger d'HERMES\n\nTomeu Capó Capó 2006 (C)")     
   
    def onCmdLlibreta(self, sender, sel, ptr):       
        if self.dlg_llibreta.execute():
           self.dlg_llibreta.guardarXML()

    def onCmdBuidarReg(self, sender, sel, ptr):
        if self.n_dades>0:
           self.t_resultat.removeRows(1,self.n_dades)
           
    ################################################################################
    # Configuració general del programa
    
    def onCmdConfig(self, sender, sel, ptr):
        if self.dlg_config.execute():
           val_conf = self.dlg_config.guardar_valors();
           self.COM_DEF = val_conf["disp"]
           self.COM_VEL = val_conf["baud"]
           self.entrades_analog = val_conf["max_ent_analog"]
           self.entrades_digit = val_conf["max_ent_digit"]
           self.modem_init = val_conf["modem_init"]
           self.modem_dial = val_conf["modem_dial"]
           
    ################################################################################
    # Mètodes referents als radiobuttons del tipus de connexió
    
    def onConnRemot(self, sender, sel, ptr):
        self.tipus_conn = 1
        self.c_telef.enable()
        self.c_clau.enable()
 
    def onConnLocal(self, sender, sel, ptr):
        self.tipus_conn = 2
        self.c_telef.disable()
        self.c_clau.disable()

    ################################################################################
    # Mètodes per la connexió i la descarrega del datalogger

    def volcar_logger(self, ser):
        
        # inst_download = instruccio('56%(digit)04x%(analog)04x' % {"digit": self.digital.getValue(), "analog": self.analog.getValue()})

        inst_download = instruccio('560001%(analog)04x' % {"digit": self.digital.getValue(), "analog": self.analog.getValue()})

        try:
          ser.write(inst_download)
        except:
          print "Error al enviar la petició de lectura del DataLogger\n "+inst_download

        inst = rebre_instruccio(ser)
        i=0
        self.l_valors = []
        
        while inst != '#7A;A9':
              valors = interpreta_log(inst)
              self.t_resultat.insertRows(i+1)
              self.t_resultat.setItemText(i+1, 0, valors['data'])
              self.t_resultat.setItemText(i+1, 1, valors['hora'])
            
              col=2
              for v in valors['valors']:
                  self.t_resultat.setItemText(i+1, col, v)
                  col = col + 1

              self.l_valors.append(valors);
              self.b_progres.setProgress(i*100/self.num_regs)
              self.l_inst.setText(inst)
              self.getApp().repaint()
              
              inst = rebre_instruccio(ser)
              i = i + 1

        return i
        
    def connectar(self, sender, sel, ptr):
        if self.tipus_conn == 0:
           showModalErrorBox(self,MBOX_OK,"Error","No ha triat el tipus de connexió")
           return 0

        self.opc_guardar.disable()
        try:
           ser = serial.Serial(self.COM_DEF, self.COM_VEL, timeout=2)
        except:
           showModalErrorBox(self,MBOX_OK, "Error","Error al obrir el port "+self.COM_DEF)
        else: 
           self.b_conn.disable()
           self.Estat.setText("Connectant ...");
           cont = False
           if self.tipus_conn == 2:
              for i in range(10):
                  self.b_progres.setProgress(i*100/10)
                  self.getApp().repaint()
                  time.sleep(0.02)
                  if re.findall(r'GsmReady',ser.readline()):
                     cont = True
                     break
           else:
              if self.c_telef.getText() == '':
                 showModalErrorBox(self,MBOX_OK,"Error","No ha possat un nombre de telèfon")
              else: 
                 print "Inicialitzant ..."
                 
                 # Cadena que tenia per defècte:
                 # AT S7=45 S0=0 L1 V1 X4 &c1 E1 Q0
                 
                 ser.write(self.modem_init+"\r\n");
                 print ser.readline()
                 
                 print "Marcant ... (Fins a 30 segons d'espera màxima)"

                 self.Estat.setText("Marcant "+self.c_telef.getText()+" ...");
                 self.getApp().repaint()
                 
                 ser.write(self.modem_dial+self.c_telef.getText()+"\r\n")
                 
                 self.Estat.setText("Esperant connexió ...");
                 
                 for i in range(30):
                     self.b_progres.setProgress(i*100/29)
                     self.getApp().repaint()
                     if re.findall(r'CONNECT',ser.readline()):
                        self.b_progres.setProgress(100)
                        print "Connectat ..."
                        cont = True
                        break
                     else:
                        if re.findall(r'CARRIER',ser.readline()):
                           showModalErrorBox(self,MBOX_OK,"Error","No hi ha tò de marcatge") 
                           break
                 if cont:
                    self.Estat.setText("Autenticant ...");
                    self.getApp().repaint()
                    if autenticar(ser, self.c_clau.getText()) == False:
                       showModalErrorBox(self,MBOX_OK,"Error","La contrasenya és incorrecte!")
                       cont = False
                    
           if cont: 
              self.Estat.setText("Llegint estat ...")
              self.getApp().repaint()

              # Determinam el nombre de registres existents dins el Hermes,
              # el nombre de sèrie i la versió del Firmware.
              
              self.num_regs = num_registres(ser)

              self.c_nserie.setText(numero_serie(ser))
              self.c_vfirmware.setText(firmware_version(ser))
              self.c_num_regs.setText("%(#)d" % {"#": self.num_regs})
              self.getApp().repaint()
              
              self.Estat.setText("Llegint dades ...")
              self.getApp().repaint()
              
              self.n_dades = self.volcar_logger(ser)
              self.c_num_dades.setText("%(#)d" % {"#": self.n_dades})
               
              if self.n_dades == 0:
                 showModalInformationBox(self,MBOX_OK, "Avis","El datalogger estava buid i no s'ha baixat res!")
              else:
                 self.opc_guardar.enable()
                 showModalInformationBox(self,MBOX_OK, "Info","S'han baixat %(r_baixat)d registre(s) de %(r_totals)d" % {"r_baixat": self.n_dades, "r_totals": self.num_regs})
                 if MBOX_CLICKED_YES == showModalQuestionBox(self, MBOX_YES_NO, "Avis!","Vol buidar el datalogger?"):
                    ser.write(instruccio('57'))
                    inst_resp = rebre_instruccio(ser)
                    if inst_resp == instruccio("A81"):
                       print "Borrat!"

           else:
              showModalErrorBox(self,MBOX_OK,"Error","No hem puc possar en contacte amb l'Hermes!")

           self.b_progres.setProgress(0)  
           self.Estat.setText("Off-Line");
           self.b_conn.enable()
           ser.close()            
              
    # Start
    def create(self):
        self.tipus_conn = 2
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

def runme():
    import sys
    app = FXApp("Dialog", "Test")
    app.init(sys.argv)
    Datalogger(app)
    app.create()
    app.run()

if __name__ == '__main__':    
    runme()
