# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\Inicial.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class TelaInicial(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setMidLineWidth(0)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("ui\\../Icons/feather/rr6.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lineEditMail = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMail.setObjectName("lineEditMail")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditMail)
        self.lineEditSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSenha.setObjectName("lineEditSenha")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditSenha)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonSair = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSair.setObjectName("pushButtonSair")
        self.horizontalLayout.addWidget(self.pushButtonSair)
        self.pushButtonEntrar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEntrar.setObjectName("pushButtonEntrar")
        self.horizontalLayout.addWidget(self.pushButtonEntrar)
        self.pushButtonCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCadastrar.setObjectName("pushButtonCadastrar")
        self.horizontalLayout.addWidget(self.pushButtonCadastrar)
        self.pushButtonRedefinir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRedefinir.setObjectName("pushButtonRedefinir")
        self.horizontalLayout.addWidget(self.pushButtonRedefinir)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditMail, self.lineEditSenha)
        MainWindow.setTabOrder(self.lineEditSenha, self.pushButtonSair)
        MainWindow.setTabOrder(self.pushButtonSair, self.pushButtonEntrar)
        MainWindow.setTabOrder(self.pushButtonEntrar, self.pushButtonCadastrar)
        MainWindow.setTabOrder(self.pushButtonCadastrar, self.pushButtonRedefinir)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEditMail.setPlaceholderText(_translate("MainWindow", "E-mail"))
        self.lineEditSenha.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.pushButtonSair.setText(_translate("MainWindow", "Sair"))
        self.pushButtonEntrar.setText(_translate("MainWindow", "Entrar"))
        self.pushButtonCadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.pushButtonRedefinir.setText(_translate("MainWindow", "Redefinir senha"))
#import imagens_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaInicial()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
