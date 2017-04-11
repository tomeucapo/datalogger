#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from FXPy.fox import *
from xml.dom.minidom import *

# Definicio de la finestra de la llibreta d'adreçes

class Llibreta(FXDialogBox):
    ID_GUARDAR = FXDialogBox.ID_LAST
    ID_BORRAR = ID_GUARDAR+1
    max_rows = 1
    
    def __init__(self, owner):
        self.nodes = {} 
        
        FXDialogBox.__init__(self,owner, "Llibreta d'adreçes", DECOR_TITLE|DECOR_BORDER)
                
        FXMAPFUNC(self, SEL_COMMAND, Llibreta.ID_GUARDAR, Llibreta.onCmdGuardar)
        FXMAPFUNC(self, SEL_COMMAND, Llibreta.ID_BORRAR, Llibreta.onCmdBorrar)
        
        frame = FXVerticalFrame(self, LAYOUT_SIDE_TOP|FRAME_NONE|LAYOUT_FILL_X|LAYOUT_FILL_Y)   
        gp = FXGroupBox(frame,'Dades del node',LAYOUT_SIDE_TOP|FRAME_GROOVE|LAYOUT_FILL_X, 0,0,0,0)
        
        matriu = FXMatrix(gp, 2, MATRIX_BY_COLUMNS|LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y)

        FXLabel(matriu, "Telèfon:", None, LAYOUT_LEFT)
        self.c_telef = FXTextField(matriu,13,opts=JUSTIFY_LEFT|FRAME_SUNKEN|FRAME_THICK|LAYOUT_LEFT)
        FXLabel(matriu, "Descripció del node:", None, LAYOUT_LEFT)
        self.c_desc = FXTextField(matriu,40,opts=JUSTIFY_LEFT|FRAME_SUNKEN|FRAME_THICK|LAYOUT_LEFT)
        FXLabel(matriu, "Ubicació:", None, LAYOUT_LEFT)
        self.c_ubic = FXTextField(matriu,40,opts=JUSTIFY_LEFT|FRAME_SUNKEN|FRAME_THICK|LAYOUT_LEFT)
        FXLabel(matriu, "Núm. Sèrie:", None, LAYOUT_LEFT)
        self.c_nserie = FXTextField(matriu,12,opts=JUSTIFY_LEFT|FRAME_SUNKEN|FRAME_THICK|LAYOUT_LEFT)
        FXLabel(matriu, "Ver. Firmware:", None, LAYOUT_LEFT)
        self.c_vfirmw = FXTextField(matriu,12,opts=JUSTIFY_LEFT|FRAME_SUNKEN|FRAME_THICK|LAYOUT_LEFT)
        
        FXLabel(matriu, "", None, LAYOUT_LEFT)
                
        frm_buttons1 = FXHorizontalFrame(matriu, LAYOUT_FILL_X)
             
        self.b_guardar_node = FXButton(frm_buttons1, " Afegir node ", None, self, self.ID_GUARDAR,         
                                       (FRAME_RAISED|FRAME_THICK|LAYOUT_SIDE_LEFT|LAYOUT_CENTER_Y))
        
        self.b_borrar_node = FXButton(frm_buttons1, " Borrar ", None, self, self.ID_BORRAR,
                                       (FRAME_RAISED|FRAME_THICK|LAYOUT_SIDE_LEFT|LAYOUT_CENTER_Y))

        self.b_borrar_node.disable()
                 
        gp1 = FXGroupBox(frame,'Llistat de nodes',LAYOUT_SIDE_TOP|FRAME_GROOVE|LAYOUT_FILL_X, 0,0,0,0)
        self.t_nodes = FXTable(gp1, 10, 8, None, 0, LAYOUT_FILL_X|LAYOUT_FILL_Y, 0,0,0,0, 2,2,2,2)
        self.t_nodes.setTableSize(1,5)
        self.t_nodes.setItemText(0, 0, 'Telèfon')
        self.t_nodes.setItemText(0, 1, 'Descripció')
        self.t_nodes.setItemText(0, 2, 'Ubicació')
        self.t_nodes.setItemText(0, 3, 'N. Sèrie')
        self.t_nodes.setItemText(0, 4, 'V. Firmware')
        
        self.t_nodes.setLeadingRows(1)
        self.t_nodes.setLeadingCols(1)

        frm_buttons = FXHorizontalFrame(frame, LAYOUT_FILL_X)

        FXButton(frm_buttons, " Aceptar ", None, self, FXDialogBox.ID_ACCEPT,
                 (FRAME_RAISED|FRAME_THICK|LAYOUT_SIDE_LEFT|LAYOUT_CENTER_Y))
                 
        FXButton(frm_buttons, " Cancelar ", None, self, FXDialogBox.ID_CANCEL,
                 (FRAME_RAISED|FRAME_THICK|LAYOUT_SIDE_RIGHT|LAYOUT_CENTER_Y))
        try:
           self.dom = parse('llibreta.xml')
           self.root = self.dom.firstChild
        except:
           print "Error al obrir el fitxer de la llibreta: "+fitxer
        else:
           self.__ompleTaula__()

    def guardarXML(self):
        f = open('llibreta.xml','w') 
        self.dom.writexml(f, encoding="ISO-8859-15")
        f.close()
        
    def onCmdBorrar(self, sender, sel, ptr):
        print "Borrar node"
        
    def onCmdGuardar(self, sender, sel, ptr):
        if self.__dadesCorrectes__():
           self.__nouNode__()
           self.__ompleTaula__()
           self.__buidaCamps__()
           
    def __ompleTaula__(self): 
        i=1
        if(self.max_rows>1):
           self.t_nodes.removeRows(1,self.max_rows-1)
           
        self.l_nodes = {}
        
        if self.root.nodeType == self.root.ELEMENT_NODE and self.root.localName == "llibreta":
           for node in self.root.childNodes:
               if node.nodeType == node.ELEMENT_NODE and node.localName == "node":
                  if node.hasAttribute('id'):
                     self.t_nodes.insertRows(i)
                     node.setIdAttribute('id')
                     id_node = node.getAttribute('id').encode('ISO-8859-15')
                     self.t_nodes.setItemText(i, 0, id_node)
                     c=1
                     for subnode in node.childNodes:
                         if subnode.nodeType == subnode.ELEMENT_NODE:
                            nom_atribut = subnode.localName
                            valor_attr = ''
                            if subnode.firstChild:
                               valor_attr = subnode.firstChild.data.encode('ISO-8859-15')

                            self.t_nodes.setItemText(i, c, valor_attr)
                            c=c+1
                     i=i+1
                  else:
                     print "Node sense identificador definit!"
           self.max_rows = i  
        else:
           print "El fitxer de la llibreta està buid!"
             
    def __dadesCorrectes__(self):
        retval = False
        
        if (self.c_telef.getText()==''):
            showModalErrorBox(self,MBOX_OK,"Error","No ha possat un nombre de telèfon")
        else:
            if (self.c_desc.getText()==''):
                showModalErrorBox(self,MBOX_OK,"Error","No ha escrit la descripció del node")
            else:
                if(self.dom.getElementById(self.c_telef.getText())):
                   showModalErrorBox(self,MBOX_OK,"Error","Aquest numero de telèfon ja existeix!")
                else:
                   retval = True
                  
        return retval
        
    def __crearCamp__(self, nomCamp, valor):
        camp_nou = self.dom.createElement(nomCamp)
        valor_nou = self.dom.createTextNode(valor.encode("ISO-8859-15"))
        camp_nou.appendChild(valor_nou)
        return camp_nou       
        
    def __nouNode__(self):
        node_nou = self.dom.createElement('node')
        node_nou.setAttribute('id', self.c_telef.getText())   
        node_nou.setIdAttribute('id')
        
        node_nou.appendChild(self.__crearCamp__('titol',self.c_desc.getText()))
        node_nou.appendChild(self.__crearCamp__('ubicacio',self.c_ubic.getText()))
        node_nou.appendChild(self.__crearCamp__('nserie',self.c_nserie.getText()))
        node_nou.appendChild(self.__crearCamp__('firmware',self.c_vfirmw.getText()))
        self.root.appendChild(node_nou)
        
    def __buidaCamps__(self):
        self.c_telef.setText('')
        self.c_desc.setText('')
        self.c_ubic.setText('')
        self.c_nserie.setText('')
        self.c_vfirmw.setText('')
    
    