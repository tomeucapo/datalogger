# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/f_configurador.ui'
#
# Created: Sun Jan  7 22:56:54 2007
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_frmConfigurador(object):
    def setupUi(self, frmConfigurador):
        frmConfigurador.setObjectName("frmConfigurador")
        frmConfigurador.resize(QtCore.QSize(QtCore.QRect(0,0,371,391).size()).expandedTo(frmConfigurador.minimumSizeHint()))

        self.layoutWidget = QtGui.QWidget(frmConfigurador)
        self.layoutWidget.setGeometry(QtCore.QRect(10,350,162,31))
        self.layoutWidget.setObjectName("layoutWidget")

        self.hboxlayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.okButton = QtGui.QPushButton(self.layoutWidget)
        self.okButton.setObjectName("okButton")
        self.hboxlayout.addWidget(self.okButton)

        self.cancelButton = QtGui.QPushButton(self.layoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout.addWidget(self.cancelButton)

        self.verticalLayout = QtGui.QWidget(frmConfigurador)
        self.verticalLayout.setGeometry(QtCore.QRect(10,10,351,331))
        self.verticalLayout.setObjectName("verticalLayout")

        self.vboxlayout = QtGui.QVBoxLayout(self.verticalLayout)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.groupBox_2 = QtGui.QGroupBox(self.verticalLayout)
        self.groupBox_2.setObjectName("groupBox_2")

        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(40,30,69,20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.c_port = QtGui.QComboBox(self.groupBox_2)
        self.c_port.setGeometry(QtCore.QRect(120,30,191,27))
        self.c_port.setEditable(True)
        self.c_port.setObjectName("c_port")

        self.c_vel = QtGui.QComboBox(self.groupBox_2)
        self.c_vel.setGeometry(QtCore.QRect(120,70,101,22))
        self.c_vel.setEditable(True)
        self.c_vel.setMaxCount(152000)
        self.c_vel.setObjectName("c_vel")

        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(50,70,60,20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.vboxlayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QtGui.QGroupBox(self.verticalLayout)
        self.groupBox_3.setObjectName("groupBox_3")

        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(11,30,113,21))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10,70,152,21))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")

        self.c_dial = QtGui.QLineEdit(self.groupBox_3)
        self.c_dial.setGeometry(QtCore.QRect(170,70,171,20))
        self.c_dial.setObjectName("c_dial")

        self.c_init = QtGui.QLineEdit(self.groupBox_3)
        self.c_init.setGeometry(QtCore.QRect(140,30,201,20))
        self.c_init.setObjectName("c_init")
        self.vboxlayout.addWidget(self.groupBox_3)

        self.groupBox = QtGui.QGroupBox(self.verticalLayout)
        self.groupBox.setObjectName("groupBox")

        self.c_analog = QtGui.QLineEdit(self.groupBox)
        self.c_analog.setGeometry(QtCore.QRect(190,30,41,20))
        self.c_analog.setMaxLength(32767)
        self.c_analog.setObjectName("c_analog")

        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10,30,176,21))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")

        self.c_digit = QtGui.QLineEdit(self.groupBox)
        self.c_digit.setGeometry(QtCore.QRect(190,70,41,20))
        self.c_digit.setMaxLength(4)
        self.c_digit.setObjectName("c_digit")

        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(40,70,147,21))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.vboxlayout.addWidget(self.groupBox)

        self.retranslateUi(frmConfigurador)
        QtCore.QObject.connect(self.okButton,QtCore.SIGNAL("clicked()"),frmConfigurador.accept)
        QtCore.QObject.connect(self.cancelButton,QtCore.SIGNAL("clicked()"),frmConfigurador.reject)
        QtCore.QMetaObject.connectSlotsByName(frmConfigurador)
        frmConfigurador.setTabOrder(self.c_port,self.c_vel)
        frmConfigurador.setTabOrder(self.c_vel,self.c_init)
        frmConfigurador.setTabOrder(self.c_init,self.c_dial)
        frmConfigurador.setTabOrder(self.c_dial,self.c_analog)
        frmConfigurador.setTabOrder(self.c_analog,self.c_digit)
        frmConfigurador.setTabOrder(self.c_digit,self.okButton)
        frmConfigurador.setTabOrder(self.okButton,self.cancelButton)

    def retranslateUi(self, frmConfigurador):
        frmConfigurador.setWindowTitle(QtGui.QApplication.translate("frmConfigurador", "Configurar", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("frmConfigurador", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("frmConfigurador", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("frmConfigurador", "Port Serie", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("frmConfigurador", "Dispositiu:", None, QtGui.QApplication.UnicodeUTF8))
        self.c_port.addItem(QtGui.QApplication.translate("frmConfigurador", "COM1", None, QtGui.QApplication.UnicodeUTF8))
        self.c_port.addItem(QtGui.QApplication.translate("frmConfigurador", "COM2", None, QtGui.QApplication.UnicodeUTF8))
        self.c_vel.addItem(QtGui.QApplication.translate("frmConfigurador", "110", None, QtGui.QApplication.UnicodeUTF8))
        self.c_vel.addItem(QtGui.QApplication.translate("frmConfigurador", "300", None, QtGui.QApplication.UnicodeUTF8))
        self.c_vel.addItem(QtGui.QApplication.translate("frmConfigurador", "1200", None, QtGui.QApplication.UnicodeUTF8))
        self.c_vel.addItem(QtGui.QApplication.translate("frmConfigurador", "2400", None, QtGui.QApplication.UnicodeUTF8))
        self.c_vel.addItem(QtGui.QApplication.translate("frmConfigurador", "4800", None, QtGui.QApplication.UnicodeUTF8))
        self.c_vel.addItem(QtGui.QApplication.translate("frmConfigurador", "9600", None, QtGui.QApplication.UnicodeUTF8))
        self.c_vel.addItem(QtGui.QApplication.translate("frmConfigurador", "19200", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("frmConfigurador", "Velocitat:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("frmConfigurador", "Modem", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("frmConfigurador", "Cadena AT d\'inici:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("frmConfigurador", "Cadena AT de marcatge:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("frmConfigurador", "Configuració d\'entrades de l\'HERMES", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("frmConfigurador", "Num. entrades analògiques:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("frmConfigurador", "Num. entrades digitals:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    frmConfigurador = QtGui.QDialog()
    ui = Ui_frmConfigurador()
    ui.setupUi(frmConfigurador)
    frmConfigurador.show()
    sys.exit(app.exec_())
