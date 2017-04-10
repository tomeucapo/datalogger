import sys
from PyQt4 import QtCore, QtGui, QtSql
from frmLlibreta import Ui_frmLlibreta

class Estacions(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        model = QtSql.QSqlTableModel()
        model.setTable("unitat")
        model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        model.select()          
        
        model.removeColumn(0)
        model.setHeaderData(0, QtCore.Qt.Horizontal, QtCore.QVariant(QtCore.QObject.tr(model, "Telefon")))
        model.setHeaderData(1, QtCore.Qt.Horizontal, QtCore.QVariant(QtCore.QObject.tr(model, "Descripcio")))

        self.ui = Ui_frmLlibreta()
        self.ui.setupUi(self)       
        
        self.ui.t_estacions.setModel(model)
        self.ui.t_estacions.showColumn(1)

     
    def Llista(self):
        query = QtSql.QSqlQuery()
         
        query.exec_("select telefon, descripcio from unitat")
    
        l1 = QtCore.QStringList()
        l2 = []
    
        l1.append("Tria una estacio")
        l2.append("")
    
        while (query.next()):
               l1.append(query.value(0).toString()+" "+query.value(1).toString())
               l2.append(query.value(0).toString())
    
        l_estacions = [l1, l2]
        return l_estacions

    def IdTelefon(self, telef):
        query = QtSql.QSqlQuery()
        query.exec_("select id from unitat where telefon='%(tlf)s'" % {"tlf": telef})
        
        if(query.next()):
           retval = str(query.value(0).toString())    
        else:
           retval = -1
           
        return retval
        
    def Actualitza(self, id_estacio, dades):
        query = QtSql.QSqlQuery()
        
        qs = "update unitat set n_serie='%(nserie)s', v_firmware='%(vfirmware)s', darrera_connexio='%(datahora)s' where id=%(ids)s" % {"nserie": dades[0], "vfirmware": dades[1], "datahora": dades[2],"ids": id_estacio}
        print qs
        query.exec_(qs)
        
        return
        
    
        
        
        
