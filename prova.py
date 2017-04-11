#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import cgi
from xml.dom.minidom import *

if __name__ == '__main__':
     try:
        dom = parse('llibreta.xml')
        root = dom.firstChild
     except:
        print "Error al obrir el fitxer de la llibreta llibreta.xml"
     else:
        if root.nodeType == root.ELEMENT_NODE and root.localName == "llibreta":
           l_nodes = {}
           for node in root.childNodes:
               if node.nodeType == node.ELEMENT_NODE and node.localName == "node":
                  if node.hasAttribute('id'):
                     print node.getAttribute('id')
                     id_node = node.getAttribute('id')
                     atributs = {}
                     for subnode in node.childNodes:
                         if subnode.nodeType == subnode.ELEMENT_NODE:
                            print subnode.localName
                            nom_atribut = subnode.localName
                            
                            valor_attr = ''
                            if subnode.firstChild:
                               valor_attr = subnode.firstChild.data.encode('ISO-8859-15')
                            
                            atributs[nom_atribut] = valor_attr
                            
                     
                     l_nodes[id_node] = atributs
                     
                     print
                  else:
                     print "No te identificador definit!"
        else:
           print "El fitxer de la llibreta estˆ corrupte!"
          
        
        node_nou = dom.createElement('node')
        node_nou.setAttribute('id', '9999')        
        titol_nou = dom.createElement('titol')
        valor_nou = dom.createTextNode('doweofjwfw')
        titol_nou.appendChild(valor_nou)
        node_nou.appendChild(titol_nou)
        root.appendChild(node_nou)
        
        f = open('llibreta.xml','w') 
        dom.writexml(f,'\t','\t','\n')
        f.close()     
        
        