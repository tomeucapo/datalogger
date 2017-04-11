# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/f_llibreta.ui'
#
# Created: Sun Jan  7 22:56:54 2007
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_frmLlibreta(object):
    def setupUi(self, frmLlibreta):
        frmLlibreta.setObjectName("frmLlibreta")
        frmLlibreta.resize(QtCore.QSize(QtCore.QRect(0,0,741,504).size()).expandedTo(frmLlibreta.minimumSizeHint()))

        self.centralWidget = QtGui.QWidget(frmLlibreta)
        self.centralWidget.setObjectName("centralWidget")

        self.vboxlayout = QtGui.QVBoxLayout(self.centralWidget)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setObjectName("groupBox")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout1.setMargin(9)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.t_estacions = QtGui.QTableView(self.groupBox)
        self.t_estacions.setObjectName("t_estacions")
        self.vboxlayout1.addWidget(self.t_estacions)

        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setMinimumSize(QtCore.QSize(16,16))
        self.groupBox_2.setObjectName("groupBox_2")

        self.gridlayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.c_telef = QtGui.QLineEdit(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_telef.sizePolicy().hasHeightForWidth())
        self.c_telef.setSizePolicy(sizePolicy)
        self.c_telef.setObjectName("c_telef")
        self.gridlayout.addWidget(self.c_telef,0,1,1,1)

        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5,0,0,1,1)

        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4,3,0,1,1)

        self.c_ubicacio = QtGui.QLineEdit(self.groupBox_2)
        self.c_ubicacio.setObjectName("c_ubicacio")
        self.gridlayout.addWidget(self.c_ubicacio,2,1,1,1)

        self.c_nserie = QtGui.QLineEdit(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_nserie.sizePolicy().hasHeightForWidth())
        self.c_nserie.setSizePolicy(sizePolicy)
        self.c_nserie.setObjectName("c_nserie")
        self.gridlayout.addWidget(self.c_nserie,3,1,1,1)

        self.label_2_2_2_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2_2_2_2.setObjectName("label_2_2_2_2")
        self.gridlayout.addWidget(self.label_2_2_2_2,1,0,1,1)

        self.c_vfirmware = QtGui.QLineEdit(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_vfirmware.sizePolicy().hasHeightForWidth())
        self.c_vfirmware.setSizePolicy(sizePolicy)
        self.c_vfirmware.setObjectName("c_vfirmware")
        self.gridlayout.addWidget(self.c_vfirmware,4,1,1,1)

        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3,2,0,1,1)

        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,4,0,1,1)

        self.c_descripcio = QtGui.QLineEdit(self.groupBox_2)
        self.c_descripcio.setObjectName("c_descripcio")
        self.gridlayout.addWidget(self.c_descripcio,1,1,1,1)
        self.vboxlayout1.addWidget(self.groupBox_2)
        self.vboxlayout.addWidget(self.groupBox)
        frmLlibreta.setCentralWidget(self.centralWidget)

        self.toolBar = QtGui.QToolBar(frmLlibreta)
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setObjectName("toolBar")
        frmLlibreta.addToolBar(self.toolBar)

        self.actionAfegir_nova_estacio = QtGui.QAction(frmLlibreta)
        self.actionAfegir_nova_estacio.setChecked(False)
        self.actionAfegir_nova_estacio.setIcon(QtGui.QIcon(":/icones/Icones/afegir.png"))
        self.actionAfegir_nova_estacio.setObjectName("actionAfegir_nova_estacio")

        self.actionAcceptar = QtGui.QAction(frmLlibreta)
        self.actionAcceptar.setEnabled(False)
        self.actionAcceptar.setIcon(QtGui.QIcon(":/icones/Icones/ok.png"))
        self.actionAcceptar.setObjectName("actionAcceptar")

        self.actionCancelar = QtGui.QAction(frmLlibreta)
        self.actionCancelar.setEnabled(False)
        self.actionCancelar.setIcon(QtGui.QIcon(":/icones/Icones/cancel.png"))
        self.actionCancelar.setObjectName("actionCancelar")

        self.actionBorrar = QtGui.QAction(frmLlibreta)
        self.actionBorrar.setEnabled(False)
        self.actionBorrar.setIcon(QtGui.QIcon(":/icones/Icones/buidar.png"))
        self.actionBorrar.setObjectName("actionBorrar")

        self.actionTancar = QtGui.QAction(frmLlibreta)
        self.actionTancar.setIcon(QtGui.QIcon(":/icones/Icones/sortir.png"))
        self.actionTancar.setObjectName("actionTancar")
        self.toolBar.addAction(self.actionAfegir_nova_estacio)
        self.toolBar.addAction(self.actionBorrar)
        self.toolBar.addAction(self.actionAcceptar)
        self.toolBar.addAction(self.actionCancelar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTancar)

        self.retranslateUi(frmLlibreta)
        QtCore.QObject.connect(self.actionTancar,QtCore.SIGNAL("triggered()"),frmLlibreta.close)
        QtCore.QMetaObject.connectSlotsByName(frmLlibreta)
        frmLlibreta.setTabOrder(self.c_telef,self.c_descripcio)
        frmLlibreta.setTabOrder(self.c_descripcio,self.c_ubicacio)
        frmLlibreta.setTabOrder(self.c_ubicacio,self.c_nserie)
        frmLlibreta.setTabOrder(self.c_nserie,self.c_vfirmware)

    def retranslateUi(self, frmLlibreta):
        frmLlibreta.setWindowTitle(QtGui.QApplication.translate("frmLlibreta", "Manteniment d\'estacions", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("frmLlibreta", "Estacions", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("frmLlibreta", "Detalls de l\'estació", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("frmLlibreta", "<b>Telèfon:</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("frmLlibreta", "<b>Núm. Sèrie:</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2_2_2_2.setText(QtGui.QApplication.translate("frmLlibreta", "<b>Descripció: </b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("frmLlibreta", "<b>Ubicació:</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("frmLlibreta", "<b>Ver. Firmware:</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAfegir_nova_estacio.setText(QtGui.QApplication.translate("frmLlibreta", "Afegir nova estacio", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAcceptar.setText(QtGui.QApplication.translate("frmLlibreta", "Acceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCancelar.setText(QtGui.QApplication.translate("frmLlibreta", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBorrar.setText(QtGui.QApplication.translate("frmLlibreta", "Borrar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTancar.setText(QtGui.QApplication.translate("frmLlibreta", "Tancar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTancar.setShortcut(QtGui.QApplication.translate("frmLlibreta", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    frmLlibreta = QtGui.QMainWindow()
    ui = Ui_frmLlibreta()
    ui.setupUi(frmLlibreta)
    frmLlibreta.show()
    sys.exit(app.exec_())
