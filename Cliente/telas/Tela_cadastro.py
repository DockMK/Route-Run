# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\cadastrar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class TelaCadastro(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEditNome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNome.setObjectName("lineEditNome")
        self.horizontalLayout_4.addWidget(self.lineEditNome)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEditMail = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMail.setObjectName("lineEditMail")
        self.horizontalLayout_3.addWidget(self.lineEditMail)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.dateEditNascimento = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEditNascimento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEditNascimento.setWhatsThis("")
        self.dateEditNascimento.setReadOnly(False)
        self.dateEditNascimento.setCalendarPopup(True)
        self.dateEditNascimento.setObjectName("dateEditNascimento")
        self.horizontalLayout_5.addWidget(self.dateEditNascimento)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEditEndereco = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEndereco.setObjectName("lineEditEndereco")
        self.horizontalLayout_7.addWidget(self.lineEditEndereco)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSenha.setObjectName("lineEditSenha")
        self.horizontalLayout_2.addWidget(self.lineEditSenha)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditCSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCSenha.setObjectName("lineEditCSenha")
        self.horizontalLayout.addWidget(self.lineEditCSenha)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.btn_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_voltar.setObjectName("btn_voltar")
        self.horizontalLayout_10.addWidget(self.btn_voltar)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_10)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.btn_cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cadastrar.setObjectName("btn_cadastrar")
        self.horizontalLayout_6.addWidget(self.btn_cadastrar)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Seja Bem-Vindo!</span></p><p align=\"center\"><span style=\" font-weight:600;\">Cadastro Usuário</span></p></body></html>"))
        self.lineEditNome.setPlaceholderText(_translate("MainWindow", "Nome completo"))
        self.lineEditMail.setPlaceholderText(_translate("MainWindow", "E-mail"))
        self.lineEditEndereco.setPlaceholderText(_translate("MainWindow", "Endereço"))
        self.lineEditSenha.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.lineEditCSenha.setPlaceholderText(_translate("MainWindow", "Confirmar senha"))
        self.btn_voltar.setText(_translate("MainWindow", "Voltar"))
        self.btn_cadastrar.setText(_translate("MainWindow", "Cadastrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaCadastro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
