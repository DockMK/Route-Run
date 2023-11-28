# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro_carro.ui'
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.placa_line = QtWidgets.QLineEdit(self.centralwidget)
        self.placa_line.setObjectName("placa_line")
        self.horizontalLayout.addWidget(self.placa_line)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.tipos_box = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tipos_box.sizePolicy().hasHeightForWidth())
        self.tipos_box.setSizePolicy(sizePolicy)
        self.tipos_box.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tipos_box.setObjectName("tipos_box")
        self.tipos_box.addItem("")
        self.tipos_box.setItemText(0, "")
        self.tipos_box.addItem("")
        self.tipos_box.addItem("")
        self.tipos_box.addItem("")
        self.tipos_box.addItem("")
        self.horizontalLayout_2.addWidget(self.tipos_box)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAccessibleName("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.modelo_line = QtWidgets.QLineEdit(self.centralwidget)
        self.modelo_line.setObjectName("modelo_line")
        self.horizontalLayout_3.addWidget(self.modelo_line)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.b_cadastro = QtWidgets.QPushButton(self.centralwidget)
        self.b_cadastro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_cadastro.setObjectName("b_cadastro")
        self.verticalLayout_2.addWidget(self.b_cadastro)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.b_voltar = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_voltar.sizePolicy().hasHeightForWidth())
        self.b_voltar.setSizePolicy(sizePolicy)
        self.b_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_voltar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/feather/arrow-left-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_voltar.setIcon(icon)
        self.b_voltar.setIconSize(QtCore.QSize(20, 20))
        self.b_voltar.setObjectName("b_voltar")
        self.verticalLayout_2.addWidget(self.b_voltar)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Placa:"))
        self.label_2.setText(_translate("MainWindow", "Tipo:"))
        self.tipos_box.setItemText(1, _translate("MainWindow", "Sedan"))
        self.tipos_box.setItemText(2, _translate("MainWindow", "Van"))
        self.tipos_box.setItemText(3, _translate("MainWindow", "SUV"))
        self.tipos_box.setItemText(4, _translate("MainWindow", "Mini-Van"))
        self.label_3.setText(_translate("MainWindow", "Modelo:"))
        self.b_cadastro.setText(_translate("MainWindow", "Cadastrar"))
        self.b_voltar.setToolTip(_translate("MainWindow", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaCadastroCarro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())