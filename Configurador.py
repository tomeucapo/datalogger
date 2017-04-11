#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from FXPy.fox import *
import cgi
from xml.dom.minidom import parse, parseString

# Definicio de la finestra de configuració

class Configurador(FXDialogBox):
    def __init__(self, owner):
        FXDialogBox.__init__(self,owner, "Configuració", DECOR_TITLE|DECOR_BORDER)
        
        self.val_conf = self.llegeix_config('config.xml')
        
        frame = FXVerticalFrame(self, LAYOUT_SIDE_TOP|FRAME_NONE|LAYOUT_FILL_X|LAYOUT_FILL_Y)   
        gp = FXGroupBox(frame,'Port Serie',LAYOUT_SIDE_TOP|FRAME_GROOVE|LAYOUT_FILL_X, 0,0,0,0)
        
        FXLabel(gp, "Dispositiu:", None, LAYOUT_LEFT)
        self.c_port = FXTextField(gp,30,opts=JUSTIFY_LEFT|FRAME_SUNKEN|FRAME_THICK|LAYOUT_LEFT)
        self.c_port.setValue(self.val_conf["disp"])
        FXLabel(gp, "Velocitat (baudis):", None, LAYOUT_LEFT)
        self.c_vel = FXTextField(gp,6,opts=JUSTIFY_LEFT|FRAME_SUNKEN|FRAME_THICK|LAYOUT_LEFT)
        self.c_vel.setText(self.val_conf["baud"])
        
        gp1 = FXGroupBox(frame,'Modem',LAYOUT_SIDE_TOP|FRAME_GROOVE|LAYOUT_FILL_X, 0,0,0,0)
        FXLabel(gp1, "Cadena AT de inicialització:", None, LAYOUT_LEFT)
        self.c_init = FXTextField(gp1,40,opts=JUSTIFY_LEFT|FRAME_SUNKEN|FRAME_THICK|LAYOUT_LEFT)
        self.c_init.setText(self.val_conf["modem_init"])
        FXLabel(gp1, "Cadena AT de marcatge:", None, LAYOUT_LEFT)
        self.c_dial = FXTextField(gp1,20,opts=JUSTIFY_LEFT|FRAME_SUNKEN|FRAME_THICK|LAYOUT_LEFT)
        self.c_dial.setText(self.val_conf["modem_dial"])
        
        gp1 = FXGroupBox(frame,'Configuració Entrades HERMES',LAYOUT_SIDE_TOP|FRAME_GROOVE|LAYOUT_FILL_X, 0,0,0,0)
        FXLabel(gp1, "Número d'entrades analògiques:", None, LAYOUT_LEFT)
        self.c_analog = FXTextField(gp1,4,opts=JUSTIFY_LEFT|FRAME_SUNKEN|FRAME_THICK|LAYOUT_LEFT)
        self.c_analog.setText(self.val_conf["max_ent_analog"])
        FXLabel(gp1, "Número d'entrades digitals:", None, LAYOUT_LEFT)
        self.c_digit = FXTextField(gp1,4,opts=JUSTIFY_LEFT|FRAME_SUNKEN|FRAME_THICK|LAYOUT_LEFT)
        self.c_digit.setText(self.val_conf["max_ent_digit"])
        
        frm_buttons = FXHorizontalFrame(frame, LAYOUT_FILL_X)

        FXButton(frm_buttons, "  Aceptar ", None, self, FXDialogBox.ID_ACCEPT,
                 (FRAME_RAISED|FRAME_THICK|LAYOUT_SIDE_LEFT|LAYOUT_CENTER_Y))
                 
        FXButton(frm_buttons, " Cancelar ", None, self, FXDialogBox.ID_CANCEL,
                 (FRAME_RAISED|FRAME_THICK|LAYOUT_SIDE_RIGHT|LAYOUT_CENTER_Y))

    def llegeix_config(self, fitxer):
        valors = {}
     
        try:
           dom1 = parse('config.xml')
           root = dom1.firstChild
        except:
           print "Error al obrir el fitxer de configuració config.xml"
           valors = {"disp": "COM1", "baud": "9600", "modem_init": "", "modem_dial": "ATD" }
           return valors
       
        if root.nodeType == root.ELEMENT_NODE and root.localName == "configuracio":
           conf_serie = root.getElementsByTagName('portserie')[0]
           for node in conf_serie.childNodes:
               if node.nodeType == node.ELEMENT_NODE:
                  valors[node.localName] = node.firstChild.data.encode('ISO-8859-15')
                    
           conf_modem = root.getElementsByTagName('modem')[0]
           for node in conf_modem.childNodes:
               if node.nodeType == node.ELEMENT_NODE:
                  key = "modem_%(#)s" % {"#": node.localName}
                  valors[key] = node.firstChild.data.encode('ISO-8859-15')

           conf_serie = root.getElementsByTagName('hermes')[0]
           for node in conf_serie.childNodes:
               if node.nodeType == node.ELEMENT_NODE:
                  valors[node.localName] = node.firstChild.data.encode('ISO-8859-15')

        else:
           print "El fitxer de configuració està corrupte!"  
    
        return valors
        
    def guardar_config(self, valors, fitxer):  
        modem_init = cgi.escape(valors["modem_init"]).encode("ascii", "xmlcharrefreplace")
        modem_dial = cgi.escape(valors["modem_dial"]).encode("ascii", "xmlcharrefreplace")
        f = open('config.xml', 'w')
        f.write("<?xml version='1.0' encoding='ISO-8859-15'?>\n")
        f.write("<configuracio>\n")
        f.write("  <portserie>\n")
        f.write("     <disp>%(disp)s</disp>\n" % {"disp": valors["disp"]})
        f.write("     <baud>%(vel)s</baud>\n" % {"vel": valors["baud"]})
        f.write("  </portserie>\n")
        f.write("  <modem>\n")
        f.write("     <init>%(m_init)s</init>\n" % {"m_init": modem_init})
        f.write("     <dial>%(m_dial)s</dial>\n" % {"m_dial": modem_dial})
        f.write("  </modem>\n")
        f.write("  <hermes>\n")
        f.write("     <max_ent_analog>%(analog)s</max_ent_analog>\n" % {"analog": valors["max_ent_analog"]})
        f.write("     <max_ent_digit>%(digital)s</max_ent_digit>\n" % {"digital": valors["max_ent_digit"]})
        f.write("  </hermes>\n")
        f.write("</configuracio>\n")
        f.close()
        
    def guardar_valors(self):
        self.val_conf["disp"] = self.c_port.getText()
        self.val_conf["baud"] = self.c_vel.getText()
        self.val_conf["modem_init"] = self.c_init.getText()
        self.val_conf["modem_dial"] = self.c_dial.getText()
        self.val_conf["max_ent_analog"] = self.c_analog.getText()
        self.val_conf["max_ent_digit"] = self.c_digit.getText()
        self.guardar_config(self.val_conf, 'config.xml')
        return self.val_conf