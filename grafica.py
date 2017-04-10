import sys, whrandom
from PyQt4 import QtCore, QtGui

FIVE_SECONDS = 1000 * 5 #  5 seconds in milli-seconds
AVERAGE_TYPESPEED = 125 # kind of calibration
BARWIDTH = 3

TRUE=1
FALSE=0

class FinestraGrafica(QtGui.QWidget):
  
      def __init__(self, parent = None):
          QtGui.QWidget.__init__(self, parent)                   
          self.p = QtGui.QPixmap() 
          self.setBackgroundRole(QtGui.QPalette.Base)
          self.col = 0
          self.valors = []
      
      def AssignaValors(self, l_valors):
          self.valors = l_valors
          #for v in l_valors:
          #    self.valors.append(float(v['valors'][0]))
              
      def __PintaMarca__(self, p, x, y, color, valor, txt):
          p.setPen(QtGui.QColor(color))
          p.drawText(x, y, str(valor))
          p.drawText(x, y+16, txt)
          p.drawLine(x, y-11, x, y+11)
          p.setPen(QtGui.QColor("blue"))      
      
      def paintEvent(self, event):
          poligon = QtGui.QPolygonF()
          myFont = QtGui.QFont()
          
          h = self.height()
          w = self.width()

          max_val = len(self.valors)
          if max_val == 0: 
             return 
          
          max=0
          min=0
      
          for v in self.valors:
              if max < float(v['valors'][0]):
                 max = float(v['valors'][0])
                 
              if min > float(v['valors'][0]):
                 min = float(v['valors'][0])
              else:
                 if min == 0:
                    min = float(v['valors'][0])
          
          pasY = (h/2)/max
          
          iniciX = 0
          finalX = w
          pasX = (finalX-iniciX)/max_val
          
          p = QtGui.QPainter()
          p.begin(self)
          
          p.setPen(QtGui.QColor("gray"))
          for i in range(1, h, h/8):
              p.drawLine(0, i, w, i)
          
          #x = 0
          #for i in range(max_val):
          #    if i%(max_val/8) == 0:
          #       p.drawLine(x, 0, x, h)
          #       p.drawText(x, 10, self.valors[i]['hora'])
          #       x = x + (h/8)
              
          p.setPen(QtGui.QColor("blue"))
           
          
          ho = iniciX
          
          pPath = QtGui.QPainterPath()
          for val in self.valors:
              valor_r = float(val['valors'][0])
              vp = (h-(valor_r*pasY))
              
              poligon.append(QtCore.QPointF(ho, vp))
              
              if (valor_r == max):   
                  self.__PintaMarca__(p, ho, vp, "red", max, val['hora'])
                  
              if (valor_r == min):   
                  self.__PintaMarca__(p, ho, vp, "green", min, val['hora'])

                  
              ho = ho + pasX

                
          pPath.addPolygon(poligon)
          #pPath.addText(QtCore.QPointF(10,h), myFont, "min")  
          #pPath.addText(QtCore.QPointF(10,10), myFont, "max")
          
          p.drawPath(pPath)

          
              
          p.end()
          