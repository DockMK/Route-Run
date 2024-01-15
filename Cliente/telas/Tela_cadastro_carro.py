# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\cadastro_carro.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class TelaCadastroCarro(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.placa_line = QtWidgets.QLineEdit(self.centralwidget)
        self.placa_line.setObjectName("placa_line")
        self.horizontalLayout.addWidget(self.placa_line)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cor_line = QtWidgets.QLineEdit(self.centralwidget)
        self.cor_line.setObjectName("cor_line")
        self.horizontalLayout_2.addWidget(self.cor_line)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.marca_line = QtWidgets.QLineEdit(self.centralwidget)
        self.marca_line.setObjectName("marca_line")
        self.horizontalLayout_4.addWidget(self.marca_line)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.modelo_line = QtWidgets.QLineEdit(self.centralwidget)
        self.modelo_line.setObjectName("modelo_line")
        self.horizontalLayout_3.addWidget(self.modelo_line)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.b_voltar = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_voltar.sizePolicy().hasHeightForWidth())
        self.b_voltar.setSizePolicy(sizePolicy)
        self.b_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_voltar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../Icons/feather/arrow-left-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_voltar.setIcon(icon)
        self.b_voltar.setIconSize(QtCore.QSize(20, 20))
        self.b_voltar.setObjectName("b_voltar")
        self.horizontalLayout_5.addWidget(self.b_voltar)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.b_cadastro = QtWidgets.QPushButton(self.centralwidget)
        self.b_cadastro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_cadastro.setObjectName("b_cadastro")
        self.horizontalLayout_5.addWidget(self.b_cadastro)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Cadastro do Veículo"))
        self.placa_line.setPlaceholderText(_translate("MainWindow", "Insira a placa do veículo"))
        self.cor_line.setPlaceholderText(_translate("MainWindow", "Cor do carro"))
        self.marca_line.setPlaceholderText(_translate("MainWindow", "Insira a marca do veículo"))
        self.modelo_line.setPlaceholderText(_translate("MainWindow", "Insira o modelo do veículo"))
        self.label.setText(_translate("MainWindow", "Insira a quantidade de assentos:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox.setItemText(9, _translate("MainWindow", "10"))
        self.comboBox.setItemText(10, _translate("MainWindow", "11"))
        self.comboBox.setItemText(11, _translate("MainWindow", "12"))
        self.comboBox.setItemText(12, _translate("MainWindow", "13"))
        self.comboBox.setItemText(13, _translate("MainWindow", "14"))
        self.comboBox.setItemText(14, _translate("MainWindow", "15"))
        self.comboBox.setItemText(15, _translate("MainWindow", "16"))
        self.comboBox.setItemText(16, _translate("MainWindow", "17"))
        self.comboBox.setItemText(17, _translate("MainWindow", "18"))
        self.comboBox.setItemText(18, _translate("MainWindow", "19"))
        self.comboBox.setItemText(19, _translate("MainWindow", "20"))
        self.comboBox.setItemText(20, _translate("MainWindow", "21"))
        self.comboBox.setItemText(21, _translate("MainWindow", "22"))
        self.comboBox.setItemText(22, _translate("MainWindow", "23"))
        self.comboBox.setItemText(23, _translate("MainWindow", "24"))
        self.comboBox.setItemText(24, _translate("MainWindow", "25"))
        self.comboBox.setItemText(25, _translate("MainWindow", "26"))
        self.comboBox.setItemText(26, _translate("MainWindow", "27"))
        self.comboBox.setItemText(27, _translate("MainWindow", "28"))
        self.comboBox.setItemText(28, _translate("MainWindow", "29"))
        self.comboBox.setItemText(29, _translate("MainWindow", "30"))
        self.b_voltar.setToolTip(_translate("MainWindow", "Voltar"))
        self.b_cadastro.setText(_translate("MainWindow", "Cadastrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaCadastroCarro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
