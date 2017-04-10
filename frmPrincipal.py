# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/f_principal.ui'
#
# Created: Sun Jan  7 22:56:53 2007
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_Datalogger(object):
    def setupUi(self, Datalogger):
        Datalogger.setObjectName("Datalogger")
        Datalogger.resize(QtCore.QSize(QtCore.QRect(0,0,757,627).size()).expandedTo(Datalogger.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Datalogger.sizePolicy().hasHeightForWidth())
        Datalogger.setSizePolicy(sizePolicy)

        self.centralwidget = QtGui.QWidget(Datalogger)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.resultats = QtGui.QWidget()
        self.resultats.setObjectName("resultats")

        self.gridlayout1 = QtGui.QGridLayout(self.resultats)
        self.gridlayout1.setMargin(9)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.t_resultat = QtGui.QTableWidget(self.resultats)
        self.t_resultat.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.t_resultat.setObjectName("t_resultat")
        self.gridlayout1.addWidget(self.t_resultat,0,0,1,1)
        self.tabWidget.addTab(self.resultats, "")

        self.grafica = QtGui.QWidget()
        self.grafica.setObjectName("grafica")

        self.vboxlayout = QtGui.QVBoxLayout(self.grafica)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.tabWidget.addTab(self.grafica, "")

        self.estat_entrades = QtGui.QWidget()
        self.estat_entrades.setObjectName("estat_entrades")

        self.hboxlayout = QtGui.QHBoxLayout(self.estat_entrades)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.g_analogiques = QtGui.QGroupBox(self.estat_entrades)
        self.g_analogiques.setObjectName("g_analogiques")
        self.hboxlayout.addWidget(self.g_analogiques)

        self.g_digitals = QtGui.QGroupBox(self.estat_entrades)
        self.g_digitals.setObjectName("g_digitals")
        self.hboxlayout.addWidget(self.g_digitals)
        self.tabWidget.addTab(self.estat_entrades, "")
        self.gridlayout.addWidget(self.tabWidget,1,0,1,1)

        self.b_progres = QtGui.QProgressBar(self.centralwidget)
        self.b_progres.setAutoFillBackground(False)
        self.b_progres.setProperty("value",QtCore.QVariant(0))
        self.b_progres.setOrientation(QtCore.Qt.Horizontal)
        self.b_progres.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.b_progres.setObjectName("b_progres")
        self.gridlayout.addWidget(self.b_progres,3,0,1,1)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(100,16777215))
        self.groupBox.setObjectName("groupBox")

        self.c_local = QtGui.QRadioButton(self.groupBox)
        self.c_local.setGeometry(QtCore.QRect(10,50,83,18))
        self.c_local.setChecked(True)
        self.c_local.setObjectName("c_local")

        self.c_rmt = QtGui.QRadioButton(self.groupBox)
        self.c_rmt.setGeometry(QtCore.QRect(10,80,83,18))
        self.c_rmt.setObjectName("c_rmt")
        self.hboxlayout1.addWidget(self.groupBox)

        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(16,130))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_40 = QtGui.QLabel(self.groupBox_2)
        self.label_40.setGeometry(QtCore.QRect(10,90,105,20))
        self.label_40.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")

        self.label_41 = QtGui.QLabel(self.groupBox_2)
        self.label_41.setGeometry(QtCore.QRect(40,60,72,20))
        self.label_41.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")

        self.c_num_regs = QtGui.QLabel(self.groupBox_2)
        self.c_num_regs.setGeometry(QtCore.QRect(120,90,111,21))
        self.c_num_regs.setFrameShape(QtGui.QFrame.Panel)
        self.c_num_regs.setFrameShadow(QtGui.QFrame.Sunken)
        self.c_num_regs.setObjectName("c_num_regs")

        self.c_nserie = QtGui.QLabel(self.groupBox_2)
        self.c_nserie.setGeometry(QtCore.QRect(120,60,111,21))
        self.c_nserie.setFrameShape(QtGui.QFrame.Panel)
        self.c_nserie.setFrameShadow(QtGui.QFrame.Sunken)
        self.c_nserie.setObjectName("c_nserie")

        self.c_clau = QtGui.QLineEdit(self.groupBox_2)
        self.c_clau.setEnabled(False)
        self.c_clau.setGeometry(QtCore.QRect(490,30,81,20))
        self.c_clau.setMaxLength(10)
        self.c_clau.setEchoMode(QtGui.QLineEdit.Password)
        self.c_clau.setObjectName("c_clau")

        self.label_38 = QtGui.QLabel(self.groupBox_2)
        self.label_38.setGeometry(QtCore.QRect(380,30,101,20))
        self.label_38.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")

        self.c_vfirmware = QtGui.QLabel(self.groupBox_2)
        self.c_vfirmware.setGeometry(QtCore.QRect(490,60,111,21))
        self.c_vfirmware.setFrameShape(QtGui.QFrame.Panel)
        self.c_vfirmware.setFrameShadow(QtGui.QFrame.Sunken)
        self.c_vfirmware.setObjectName("c_vfirmware")

        self.label_37 = QtGui.QLabel(self.groupBox_2)
        self.label_37.setGeometry(QtCore.QRect(390,60,90,20))
        self.label_37.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")

        self.c_num_dades = QtGui.QLabel(self.groupBox_2)
        self.c_num_dades.setGeometry(QtCore.QRect(490,90,111,21))
        self.c_num_dades.setFrameShape(QtGui.QFrame.Panel)
        self.c_num_dades.setFrameShadow(QtGui.QFrame.Sunken)
        self.c_num_dades.setObjectName("c_num_dades")

        self.label_39 = QtGui.QLabel(self.groupBox_2)
        self.label_39.setGeometry(QtCore.QRect(360,90,122,20))
        self.label_39.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")

        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(50,30,61,17))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.c_estacions = QtGui.QComboBox(self.groupBox_2)
        self.c_estacions.setEnabled(False)
        self.c_estacions.setGeometry(QtCore.QRect(120,30,261,26))
        self.c_estacions.setEditable(False)
        self.c_estacions.setObjectName("c_estacions")
        self.hboxlayout1.addWidget(self.groupBox_2)
        self.gridlayout.addLayout(self.hboxlayout1,0,0,1,1)

        self.l_inst = QtGui.QLabel(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_inst.sizePolicy().hasHeightForWidth())
        self.l_inst.setSizePolicy(sizePolicy)
        self.l_inst.setMaximumSize(QtCore.QSize(16777215,13))
        self.l_inst.setFrameShape(QtGui.QFrame.Panel)
        self.l_inst.setFrameShadow(QtGui.QFrame.Sunken)
        self.l_inst.setAlignment(QtCore.Qt.AlignCenter)
        self.l_inst.setObjectName("l_inst")
        self.gridlayout.addWidget(self.l_inst,2,0,1,1)
        Datalogger.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(Datalogger)
        self.menubar.setGeometry(QtCore.QRect(0,0,757,22))
        self.menubar.setObjectName("menubar")

        self.menuUtilitats = QtGui.QMenu(self.menubar)
        self.menuUtilitats.setObjectName("menuUtilitats")

        self.menuAjuda = QtGui.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")

        self.menuUtilitats_2 = QtGui.QMenu(self.menubar)
        self.menuUtilitats_2.setObjectName("menuUtilitats_2")

        self.menuFitxer = QtGui.QMenu(self.menubar)
        self.menuFitxer.setObjectName("menuFitxer")
        Datalogger.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(Datalogger)
        self.statusbar.setGeometry(QtCore.QRect(0,605,757,22))
        self.statusbar.setObjectName("statusbar")
        Datalogger.setStatusBar(self.statusbar)

        self.toolBar = QtGui.QToolBar(Datalogger)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setObjectName("toolBar")
        Datalogger.addToolBar(self.toolBar)

        self.actionSortir = QtGui.QAction(Datalogger)
        self.actionSortir.setIcon(QtGui.QIcon(":/icones/Icones/sortir.png"))
        self.actionSortir.setObjectName("actionSortir")

        self.actionGuardar = QtGui.QAction(Datalogger)
        self.actionGuardar.setEnabled(False)
        self.actionGuardar.setIcon(QtGui.QIcon(":/icones/Icones/guardar.png"))
        self.actionGuardar.setObjectName("actionGuardar")

        self.actionConfigurar = QtGui.QAction(Datalogger)
        self.actionConfigurar.setIcon(QtGui.QIcon(":/icones/Icones/preferencies.png"))
        self.actionConfigurar.setObjectName("actionConfigurar")

        self.actionLlibreta = QtGui.QAction(Datalogger)
        self.actionLlibreta.setEnabled(True)
        self.actionLlibreta.setIcon(QtGui.QIcon(":/icones/Icones/llibreta.png"))
        self.actionLlibreta.setObjectName("actionLlibreta")

        self.actionAbout = QtGui.QAction(Datalogger)
        self.actionAbout.setIcon(QtGui.QIcon(":/icones/Icones/about.png"))
        self.actionAbout.setObjectName("actionAbout")

        self.actionConnectar = QtGui.QAction(Datalogger)
        self.actionConnectar.setCheckable(False)
        self.actionConnectar.setChecked(False)
        self.actionConnectar.setIcon(QtGui.QIcon(":/icones/Icones/connectar.png"))
        self.actionConnectar.setObjectName("actionConnectar")

        self.actionDescarregar = QtGui.QAction(Datalogger)
        self.actionDescarregar.setEnabled(False)
        self.actionDescarregar.setIcon(QtGui.QIcon(":/icones/Icones/baixar.png"))
        self.actionDescarregar.setObjectName("actionDescarregar")

        self.actionDesconnectar = QtGui.QAction(Datalogger)
        self.actionDesconnectar.setEnabled(False)
        self.actionDesconnectar.setIcon(QtGui.QIcon(":/icones/Icones/desconnectar.png"))
        self.actionDesconnectar.setObjectName("actionDesconnectar")

        self.actionAjustar_Data = QtGui.QAction(Datalogger)
        self.actionAjustar_Data.setEnabled(False)
        self.actionAjustar_Data.setIcon(QtGui.QIcon(":/icones/Icones/rellotge.png"))
        self.actionAjustar_Data.setObjectName("actionAjustar_Data")

        self.actionBorrarDatalogger = QtGui.QAction(Datalogger)
        self.actionBorrarDatalogger.setEnabled(False)
        self.actionBorrarDatalogger.setIcon(QtGui.QIcon(":/icones/Icones/buidar.png"))
        self.actionBorrarDatalogger.setObjectName("actionBorrarDatalogger")
        self.menuAjuda.addAction(self.actionAbout)
        self.menuUtilitats_2.addAction(self.actionAjustar_Data)
        self.menuUtilitats_2.addAction(self.actionBorrarDatalogger)
        self.menuFitxer.addAction(self.actionGuardar)
        self.menuFitxer.addAction(self.actionLlibreta)
        self.menuFitxer.addAction(self.actionConfigurar)
        self.menuFitxer.addSeparator()
        self.menuFitxer.addAction(self.actionSortir)
        self.menubar.addAction(self.menuFitxer.menuAction())
        self.menubar.addAction(self.menuUtilitats_2.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.toolBar.addAction(self.actionGuardar)
        self.toolBar.addAction(self.actionConfigurar)
        self.toolBar.addAction(self.actionLlibreta)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConnectar)
        self.toolBar.addAction(self.actionDesconnectar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDescarregar)
        self.toolBar.addAction(self.actionBorrarDatalogger)
        self.toolBar.addAction(self.actionAjustar_Data)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSortir)

        self.retranslateUi(Datalogger)
        QtCore.QObject.connect(self.c_rmt,QtCore.SIGNAL("clicked(bool)"),self.c_clau.setEnabled)
        QtCore.QObject.connect(self.c_local,QtCore.SIGNAL("clicked(bool)"),self.c_clau.setDisabled)
        QtCore.QObject.connect(self.c_local,QtCore.SIGNAL("clicked(bool)"),self.c_estacions.setDisabled)
        QtCore.QObject.connect(self.c_rmt,QtCore.SIGNAL("clicked(bool)"),self.c_estacions.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Datalogger)

    def retranslateUi(self, Datalogger):
        Datalogger.setWindowTitle(QtGui.QApplication.translate("Datalogger", "Hermes Datalogger 2.2", None, QtGui.QApplication.UnicodeUTF8))
        self.t_resultat.clear()
        self.t_resultat.setColumnCount(0)
        self.t_resultat.setRowCount(0)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.resultats), QtGui.QApplication.translate("Datalogger", "Datalogger", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.grafica), QtGui.QApplication.translate("Datalogger", "Gràfica", None, QtGui.QApplication.UnicodeUTF8))
        self.g_analogiques.setTitle(QtGui.QApplication.translate("Datalogger", "Analògiques", None, QtGui.QApplication.UnicodeUTF8))
        self.g_digitals.setTitle(QtGui.QApplication.translate("Datalogger", "Digitals", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.estat_entrades), QtGui.QApplication.translate("Datalogger", "Estat d\'entrades/sortides", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Datalogger", "Connexió", None, QtGui.QApplication.UnicodeUTF8))
        self.c_local.setText(QtGui.QApplication.translate("Datalogger", "Local", None, QtGui.QApplication.UnicodeUTF8))
        self.c_rmt.setText(QtGui.QApplication.translate("Datalogger", "Remota", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Datalogger", "Estació", None, QtGui.QApplication.UnicodeUTF8))
        self.label_40.setText(QtGui.QApplication.translate("Datalogger", "N. total de regs.:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_41.setText(QtGui.QApplication.translate("Datalogger", "Num. Sèrie:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_38.setText(QtGui.QApplication.translate("Datalogger", "Clau d\'access:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("Datalogger", "Ver. Firmware:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_39.setText(QtGui.QApplication.translate("Datalogger", "Regs. descarregats:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Datalogger", "Estació:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuUtilitats.setTitle(QtGui.QApplication.translate("Datalogger", "Utilitats", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAjuda.setTitle(QtGui.QApplication.translate("Datalogger", "Ajuda", None, QtGui.QApplication.UnicodeUTF8))
        self.menuUtilitats_2.setTitle(QtGui.QApplication.translate("Datalogger", "Utilitats", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFitxer.setTitle(QtGui.QApplication.translate("Datalogger", "Fitxer", None, QtGui.QApplication.UnicodeUTF8))
        self.statusbar.setStatusTip(QtGui.QApplication.translate("Datalogger", "Off-Line", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSortir.setText(QtGui.QApplication.translate("Datalogger", "Sortir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSortir.setStatusTip(QtGui.QApplication.translate("Datalogger", "Sortir del programa ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSortir.setShortcut(QtGui.QApplication.translate("Datalogger", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar.setText(QtGui.QApplication.translate("Datalogger", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar.setToolTip(QtGui.QApplication.translate("Datalogger", "Guardar les dades descarregades del datalogger", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar.setStatusTip(QtGui.QApplication.translate("Datalogger", "Guardar les dades descarregades del datalogger", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar.setShortcut(QtGui.QApplication.translate("Datalogger", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigurar.setText(QtGui.QApplication.translate("Datalogger", "Preferències", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigurar.setStatusTip(QtGui.QApplication.translate("Datalogger", "Configurar els paràmetres del programa", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigurar.setShortcut(QtGui.QApplication.translate("Datalogger", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLlibreta.setText(QtGui.QApplication.translate("Datalogger", "Manteniment d\'estacions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLlibreta.setIconText(QtGui.QApplication.translate("Datalogger", "Estacions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLlibreta.setToolTip(QtGui.QApplication.translate("Datalogger", "Estacions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLlibreta.setStatusTip(QtGui.QApplication.translate("Datalogger", "Manteniment d\'estacions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLlibreta.setShortcut(QtGui.QApplication.translate("Datalogger", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("Datalogger", "Sobre el programa ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnectar.setText(QtGui.QApplication.translate("Datalogger", "Connectar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDescarregar.setText(QtGui.QApplication.translate("Datalogger", "Descarregar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDesconnectar.setText(QtGui.QApplication.translate("Datalogger", "Desconnectar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAjustar_Data.setText(QtGui.QApplication.translate("Datalogger", "Ajustar data/hora", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBorrarDatalogger.setText(QtGui.QApplication.translate("Datalogger", "Buidar datalogger", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Datalogger = QtGui.QMainWindow()
    ui = Ui_Datalogger()
    ui.setupUi(Datalogger)
    Datalogger.show()
    sys.exit(app.exec_())
