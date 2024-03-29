# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class TelaPrincipal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(919, 670)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.b_perfil = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_perfil.sizePolicy().hasHeightForWidth())
        self.b_perfil.setSizePolicy(sizePolicy)
        self.b_perfil.setMinimumSize(QtCore.QSize(90, 28))
        self.b_perfil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_perfil.setStyleSheet("QPushButton { \n"
"    \n"
"     border: none;\n"
" }")
        self.b_perfil.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../Icons/feather/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_perfil.setIcon(icon)
        self.b_perfil.setIconSize(QtCore.QSize(30, 30))
        self.b_perfil.setObjectName("b_perfil")
        self.gridLayout.addWidget(self.b_perfil, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.procurar = QtWidgets.QLineEdit(self.centralwidget)
        self.procurar.setText("")
        self.procurar.setObjectName("procurar")
        self.horizontalLayout.addWidget(self.procurar)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.b_procura = QtWidgets.QPushButton(self.centralwidget)
        self.b_procura.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_procura.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\../Icons/feather/lupa.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_procura.setIcon(icon1)
        self.b_procura.setObjectName("b_procura")
        self.horizontalLayout.addWidget(self.b_procura)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_reservas = QtWidgets.QPushButton(self.frame)
        self.btn_reservas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui\\../Icons/feather/smartphone.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reservas.setIcon(icon2)
        self.btn_reservas.setObjectName("btn_reservas")
        self.verticalLayout.addWidget(self.btn_reservas)
        self.b_chat = QtWidgets.QPushButton(self.frame)
        self.b_chat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui\\../Icons/feather/users.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_chat.setIcon(icon3)
        self.b_chat.setObjectName("b_chat")
        self.verticalLayout.addWidget(self.b_chat)
        self.b_voltar = QtWidgets.QPushButton(self.frame)
        self.b_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_voltar.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui\\../Icons/feather/arrow-left-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_voltar.setIcon(icon4)
        self.b_voltar.setIconSize(QtCore.QSize(30, 30))
        self.b_voltar.setObjectName("b_voltar")
        self.verticalLayout.addWidget(self.b_voltar, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frame, 0, 0, 3, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMouseTracking(False)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 674, 562))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.gridLayout.addWidget(self.frame_2, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.procurar.setPlaceholderText(_translate("MainWindow", "Rota Origem..."))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Rota Destino..."))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Route Run - </span><span style=\" font-size:20pt; font-weight:600; font-style:italic;\">Cliente</span></p></body></html>"))
        self.btn_reservas.setText(_translate("MainWindow", "Reservas"))
        self.b_chat.setText(_translate("MainWindow", "Chat"))
        self.b_voltar.setToolTip(_translate("MainWindow", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaPrincipal()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
