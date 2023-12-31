import sys
import socket
import threading
import random
import win32com.client as win32
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QDateTimeEdit, QWidget, QHBoxLayout, QPushButton, QTextEdit, QVBoxLayout, QLineEdit, QLabel
from hashlib import md5
from telas.Tela_inicial import TelaInicial
from telas.Tela_cadastro import TelaCadastro
from telas.Tela_principal import TelaPrincipal
from telas.Tela_motorista import TelaMotorista
from telas.Tela_redefinir import Redefinir
from telas.Tela_principal_motorista import TelaPrincipalMotorista
from telas.Tela_cad_rota import TelaCadRota
from telas.Tela_autentificacao import TelaAutentificacao
from telas.Tela_autentificacao2 import TelaAutentificacao2
from telas.Tela_cadastro_carro import TelaCadastroCarro
from telas.Tela_perfil_cliente import PerfilCliente
from telas.Tela_perfil import Perfil
from telas.Tela_cpf import TelaCpf
from telas.Tela_confirmacao_senha import CSenha
from telas.Tela_cidades import TelaCidades
from telas.Tela_chat import TelaChat

from client import plataforma_cliente


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()
        self.stack9 = QtWidgets.QMainWindow()
        self.stack10 = QtWidgets.QMainWindow()
        self.stack11 = QtWidgets.QMainWindow()
        self.stack12 = QtWidgets.QMainWindow()
        self.stack13 = QtWidgets.QMainWindow()
        self.stack14 = QtWidgets.QMainWindow()
        self.stack15 = QtWidgets.QMainWindow()

        self.telaInicial = TelaInicial()
        self.telaInicial.setupUi(self.stack0)

        self.telaCadastro = TelaCadastro()
        self.telaCadastro.setupUi(self.stack1)

        self.telaPrincipal = TelaPrincipal()
        self.telaPrincipal.setupUi(self.stack2)

        self.telaMotorista = TelaMotorista()
        self.telaMotorista.setupUi(self.stack3)

        self.telaRedefinir = Redefinir()
        self.telaRedefinir.setupUi(self.stack4)

        self.telaPrincipalMotorista = TelaPrincipalMotorista()
        self.telaPrincipalMotorista.setupUi(self.stack5)

        self.telaRota = TelaCadRota()
        self.telaRota.setupUi(self.stack6)

        self.telaAut = TelaAutentificacao()
        self.telaAut.setupUi(self.stack7)

        self.telaAut2 = TelaAutentificacao2()
        self.telaAut2.setupUi(self.stack8)

        self.telaperfil = Perfil()
        self.telaperfil.setupUi(self.stack9)

        self.telacadastrocarro = TelaCadastroCarro()
        self.telacadastrocarro.setupUi(self.stack10)

        self.telaperfilcliente = PerfilCliente()
        self.telaperfilcliente.setupUi(self.stack11)

        self.telacpf = TelaCpf()
        self.telacpf.setupUi(self.stack12)

        self.telacsenha = CSenha()
        self.telacsenha.setupUi(self.stack13)

        self.telacitys = TelaCidades()
        self.telacitys.setupUi(self.stack14)

        self.telachat = TelaChat()
        self.telachat.setupUi(self.stack15)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)
        self.QtStack.addWidget(self.stack10)
        self.QtStack.addWidget(self.stack11)
        self.QtStack.addWidget(self.stack12)
        self.QtStack.addWidget(self.stack13)
        self.QtStack.addWidget(self.stack14)
        self.QtStack.addWidget(self.stack15)


class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)

        self.cad = plataforma_cliente()
        self.rot = plataforma_cliente()
        self.carro = plataforma_cliente()
<<<<<<< HEAD

=======
        self.numero_placa_atual = None
>>>>>>> chat
        self.telaInicial.pushButtonCadastrar.clicked.connect(self.abrirCadastroCpf)
        self.telaInicial.pushButtonEntrar.clicked.connect(self.abrirMain)
        self.telaInicial.pushButtonSair.clicked.connect(self.fecharPrograma)
        self.telaInicial.pushButtonRedefinir.clicked.connect(self.abrirEmail)

        self.telaCadastro.btn_cadastrar.clicked.connect(self.cadastrar)
        self.telaCadastro.btn_voltar.clicked.connect(self.voltar)

        self.telaPrincipal.b_voltar.clicked.connect(self.voltar)
        self.telaPrincipal.b_perfil.clicked.connect(self.abrir_perfil_cliente)
        self.telaPrincipal.b_procura.clicked.connect(self.procurarRota)
        self.telaPrincipal.lay = QVBoxLayout()

        self.telaperfilcliente.b_voltar.clicked.connect(self.voltar_principal_perfil_cliente)
        self.telaperfilcliente.b_editar.clicked.connect(self.editar_perfil_cliente)#

        self.telaMotorista.Btn_voltar.clicked.connect(self.voltar)
        self.telaMotorista.btn_finalizar.clicked.connect(self.cad_motorista)

        self.telaRedefinir.btn_confirmar.clicked.connect(self.redefinir)
        self.telaRedefinir.btn_voltar.clicked.connect(self.voltar)

        self.telaPrincipalMotorista.b_voltar.clicked.connect(self.voltar)
        self.telaPrincipalMotorista.b_cad_rota.clicked.connect(self.abrirCadastroRota)
        self.telaPrincipalMotorista.b_perfil.clicked.connect(self.abrirperfil)
        self.telaPrincipalMotorista.b_cad_carro.clicked.connect(self.abrirCadastroCarro)

        self.telaRota.b_voltar.clicked.connect(self.voltar_principal)
        self.telaRota.b_cadastro.clicked.connect(self.cad_rota)

        self.telaperfil.b_voltar.clicked.connect(self.voltar_principal)
        self.telaperfil.b_editar.clicked.connect(self.editar_perfil_motorista)#

        self.telacadastrocarro.b_cadastro.clicked.connect(self.cadCarro)
        self.telacadastrocarro.b_voltar.clicked.connect(self.voltar_principal_cadCarro)

        self.telaAut2.enviar.clicked.connect(self.email)
        self.telaAut2.voltar.clicked.connect(self.voltar)

        self.telaAut.confirmar.clicked.connect(self.autentificacao)
        self.telaAut.voltar.clicked.connect(self.voltar)

        self.telacpf.btn_confirmar.clicked.connect(self.verificar_cpf)
        self.telacpf.btn_voltar.clicked.connect(self.voltar)

        self.telacsenha.btn_confirmar.clicked.connect(self.confirmar_senha)
        self.telacsenha.btn_voltar.clicked.connect(self.voltar)

        self.telacitys.btn_voltar.clicked.connect(self.abrirTelaMotorista)
        self.telacitys.btn_cadastrar.clicked.connect(self.add_cidades)
        self.telacitys.btn_confirmar.clicked.connect(self.abrirTelaMotorista)

        self.telachat.voltar.clicked.connect(self.voltar_principal_perfil_cliente)
        self.telachat.enviar.clicked.connect(self.enviar_mensagem)
        self.telachat.layC = QVBoxLayout()

    def fecharPrograma(self):
        sys.exit(app.exec_())

    def voltar(self):
        self.telaInicial.lineEditMail.setText('')
        self.telaInicial.lineEditSenha.setText('')
        self.telaAut2.lineEdit.setText('')
        self.telaAut.lineEdit.setText('')
        self.telaPrincipal.procurar.setText('')
        self.telaPrincipal.lineEdit.setText('')
        self.telacpf.comboBoxUsuario.setCurrentText('')
        self.telacpf.lineEdit_cpf.setText('')
        self.QtStack.setCurrentIndex(0)

    def voltar_principal(self):
        self.telaRota.line_cidade_destino.setText('')
        self.telaRota.line_cidade_origem.setText('')
        self.telaRota.line_UF_destino.setText('')
        self.telaRota.line_UF_origem.setText('')
        self.telaRota.line_valor.setText('')
        self.telaRota.line_placa.setText('')
        self.telacitys.lineEditcity.setText('')
        self.telacitys.lineEdit.setText('')
        self.telaRota.checkBox.setChecked(False)
        self.QtStack.setCurrentIndex(5)

    def voltar_principal_cadCarro(self):
        self.telacadastrocarro.placa_line.setText('')
        self.telacadastrocarro.modelo_line.setText('')
        self.telacadastrocarro.tipos_box.setCurrentText('')
        self.QtStack.setCurrentIndex(5)

    def voltar_principal_perfil_cliente(self):
        self.telaPrincipal.procurar.setText('')
        self.telaPrincipal.lineEdit.setText('')
        self.QtStack.setCurrentIndex(2)
        self.limpar_layout(self.telaPrincipal.lay)
<<<<<<< HEAD
=======
        self.limpar_layout(self.telachat.layC)
        email = self.telaInicial.lineEditMail.text()
        c = self.cad.buscar_email_cliente(email)
        self.cad.zerar_mensagens(c[3])
>>>>>>> chat

    def abrir_perfil_cliente(self):
        self.QtStack.setCurrentIndex(11)
        self.perfil_cliente()

    def abrirCadastroRota(self):
        self.QtStack.setCurrentIndex(6)

    def abrirCadastroCarro(self):
        self.QtStack.setCurrentIndex(10)

    def abrirCadastroCpf(self):
        self.QtStack.setCurrentIndex(12)

    def abrirTelaCliente(self):
        self.QtStack.setCurrentIndex(2)
        self.limpar_layout(self.telaPrincipal.lay)

    def abrirTelaMotorista(self):
        self.QtStack.setCurrentIndex(5)

    def abrirCadastro(self):
        self.telaCadastro.lineEditNome.setText('')
        self.telaCadastro.lineEditEndereco.setText('')
        self.telaCadastro.lineEdit.setText('')
        self.telaCadastro.lineEditSenha.setText('')
        self.telaCadastro.lineEditCSenha.setText('')
        self.telaCadastro.lineEditMail.setText('')
        self.telaInicial.lineEditMail.setText('')
        self.telaInicial.lineEditSenha.setText('')
        self.telaCadastro.comboBoxUsuario.setCurrentIndex(0)
        self.telaInicial.lineEditCPF.setText('')
        self.telaCadastro.dateEditNascimento.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0)))
        self.telaMotorista.lineEditCNH.setText('')
        self.QtStack.setCurrentIndex(1)

    def abrirEmail(self):
        self.QtStack.setCurrentIndex(8)

    def abrirperfil(self):
        self.QtStack.setCurrentIndex(9)
        self.perfil()

    def redefinir(self):
        nsenha = self.telaRedefinir.lineEditnsenha.text()
        cnsenha = self.telaRedefinir.lineEditcnsenha.text()
        email = self.telaRedefinir.lineEditEmail.text()
        if nsenha == '' or cnsenha == '':
            QMessageBox.information(None, 'motorista', 'Todos os espaços devem ser preenchidos!')
        else:
            if (nsenha == cnsenha):
                if (self.cad.redefinir(email, nsenha) != None):
                    self.QtStack.setCurrentIndex(0)
                    self.telaRedefinir.lineEditEmail.setText('')
                    self.telaRedefinir.lineEditnsenha.setText('')
                    self.telaRedefinir.lineEditcnsenha.setText('')
                    QMessageBox.information(None, 'Busca', 'Senha alterada com sucesso!')
                else:
                    QMessageBox.information(None, 'Busca', 'não cadastrado na base de dados!')
                    self.telaRedefinir.lineEditnsenha.setText('')
                    self.telaRedefinir.lineEditcnsenha.setText('')
            else:
                QMessageBox.information(None, 'Cadastro', 'Senhas diferentes!')

    def email(self):
        email = self.telaAut2.lineEdit.text()
        #usuario = self.telaAut2.comboBoxUsuarios.currentText()
        if email == '':
            QMessageBox.information(None, 'Login', 'Todos os espaços devem ser preenchidos!')
        else:
            if (self.cad.buscar_email_mot(email) and (self.cad.buscar_email_cliente(email))):
                QMessageBox.information(None, 'Duas contas', 'Você possui cadastro como cliente e como motorista\nA senha dos seus dois cadastros serão alteradas!')
                cod = random.randint(100000, 999999)
                outlook = win32.Dispatch('outlook.application')

                mail = outlook.CreateItem(0)

                mail.To = email
                mail.Subject = "Número de alteração da senha do motorista e cliente"
                mail.HTMLBody = f"""
                <p>Codigo de alteração da senha da conta</p>

                <p>O seu codigo de alteração de senha é {cod} </p>

                """

                mail.Send()
                self.cad.guardar_num(cod)
                self.telaAut2.lineEdit.setText('')
                self.QtStack.setCurrentIndex(7)
            elif (self.cad.buscar_email_mot(email) != None and (self.cad.buscar_email_cliente(email)) == None):
                cod = random.randint(100000, 999999)
                outlook = win32.Dispatch('outlook.application')

                mail = outlook.CreateItem(0)

                mail.To = email
                mail.Subject = "Número de alteração da senha do motorista"
                mail.HTMLBody = f"""
                <p>Codigo de alteração da senha da conta</p>

                <p>O seu codigo de alteração de senha é {cod} </p>

                """

                mail.Send()
                self.cad.guardar_num(cod)
                self.telaAut2.lineEdit.setText('')
                self.QtStack.setCurrentIndex(7)
            elif (self.cad.buscar_email_mot(email) == None and (self.cad.buscar_email_cliente(email)) != None):
                cod = random.randint(100000, 999999)
                outlook = win32.Dispatch('outlook.application')

                mail = outlook.CreateItem(0)

                mail.To = email
                mail.Subject = "Número de alteração da senha do cliente"
                mail.HTMLBody = f"""
                <p>Codigo de alteração de senha</p>

                <p>O seu codigo de alteração de senha é {cod} </p>

                """

                mail.Send()
                self.cad.guardar_num(cod)
                self.telaAut2.lineEdit.setText('')
                self.QtStack.setCurrentIndex(7)

    def autentificacao(self):
        num = int(self.telaAut.lineEdit.text())

        if num == '':
            QMessageBox.information(None, 'Login', 'Todos os espaços devem ser preenchidos!')
        else:
            if (self.cad.buscar_cod(num) != None):
                self.telaAut.lineEdit.setText('')
                self.QtStack.setCurrentIndex(4)
            else:
                QMessageBox.information(None, 'Login', 'O codigo inserido não corresponde ao enviado no email')

    def abrirMain(self):

        email = self.telaInicial.lineEditMail.text()
        senha = self.telaInicial.lineEditSenha.text()

        if email == '' or senha == '':
            QMessageBox.information(None, 'Login', 'Todos os espaços devem ser preenchidos!')
        else:               
            if (self.cad.buscar_email_mot(email) and (self.cad.buscar_email_cliente(email))):
                senha = senha.encode("utf8")
                senha = md5(senha).hexdigest()

                if (self.cad.buscar_email_mot(email)[6] == senha):
                    msg = QMessageBox()
                    msg.setWindowTitle("Login")
                    msg.setText("Conta cadastrada como cliente e motorista\nDeseja Logar como cliente ou motorista?")

                    cliente_button = msg.addButton("Cliente", QMessageBox.YesRole)
                    motorista_button = msg.addButton("Motorista", QMessageBox.NoRole)
                    
                    cliente_button.clicked.connect(self.abrirTelaCliente)
                    motorista_button.clicked.connect(self.abrirTelaMotorista)
                    msg.exec()
                else:
                    QMessageBox.information(None, 'Busca', 'Senha errada')
            elif (self.cad.buscar_email_mot(email) == None and (self.cad.buscar_email_cliente(email)) != None):
                senha = senha.encode("utf8")
                senha = md5(senha).hexdigest()
                if self.cad.buscar_email_cliente(email)[6] == senha:
                    self.QtStack.setCurrentIndex(2)
                else:
                    QMessageBox.information(None, 'Busca', 'Senha errada')
            elif (self.cad.buscar_email_mot(email) != None and (self.cad.buscar_email_cliente(email)) == None):
                senha = senha.encode("utf8")
                senha = md5(senha).hexdigest()
                if self.cad.buscar_email_mot(email)[6] == senha:
                    self.QtStack.setCurrentIndex(5)
                else:
                    QMessageBox.information(None, 'Busca', 'Senha errada')
            else:
                QMessageBox.information(None, 'Busca', 'não cadastrado na base de dados!')

    ###############################################################################
    #ok?
    def add_cidades(self):
        cidade = self.telacitys.lineEditcity.text()
        uf = self.telacitys.lineEdit.text()
        if cidade == '' or uf == '':
            QMessageBox.information(None, 'cidade', 'Todos os espaços devem ser preenchidos!')
        else:
            id = self.rot.contar()

            if self.rot.add_city(id, cidade, uf):

                self.telacitys.lineEditcity.setText('')
                self.telacitys.lineEdit.setText('')
                QMessageBox.information(None, 'Cidade', 'Cidade cadastrada com sucesso')
            else:
                self.telacitys.lineEditcity.setText('')
                self.telacitys.lineEdit.setText('')
                QMessageBox.information(None, 'Cidade', 'Cidade já está cadastrada nessa rota')
    #ok?
    def cad_rota(self):
        uf_origem = self.telaRota.line_UF_origem.text()
        cidade_origem = self.telaRota.line_cidade_origem.text()
        uf_destino = self.telaRota.line_UF_destino.text()
        cidade_destino = self.telaRota.line_cidade_destino.text()
        horario = self.telaRota.horario.time()
        valor = self.telaRota.line_valor.text()
        horario_volta = self.telaRota.horario_volta.time()

        placa = self.telaRota.line_placa.text()
        if uf_origem == '' or uf_destino == '' or cidade_origem == '' or cidade_destino == '' or valor == '' or placa == '':
            QMessageBox.information(None, 'rota', 'Todos os espaços devem ser preenchidos!')
        else:
            id = self.rot.contar()  
            if (id == None):
                id = 0
            id = id + 1

            if (self.carro.busca_carro(placa) != None):
                if not (self.telaRota.checkBox.isChecked()):

                    self.rot.cadastro_rota(id, uf_origem, cidade_origem, uf_destino, cidade_destino, horario, valor, placa, horario_volta)

                    self.rot.add_city(id, cidade_origem, uf_origem)
                    self.rot.add_city(id, cidade_destino, uf_destino)

                    self.telaRota.line_UF_origem.setText('')
                    self.telaRota.line_UF_destino.setText('')
                    self.telaRota.line_cidade_origem.setText('')
                    self.telaRota.line_cidade_destino.setText('')
                    self.telaRota.line_placa.setText('')
                    self.telaRota.horario.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0)))
                    self.telaRota.horario_volta.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0)))
                    self.telaRota.line_valor.setText('')

                    self.QtStack.setCurrentIndex(5)
                else:
                    self.rot.cadastro_rota(id, uf_origem, cidade_origem, uf_destino, cidade_destino, horario, valor, placa, horario_volta)
                    self.rot.add_city(id, cidade_origem, uf_origem)
                    self.rot.add_city(id, cidade_destino, uf_destino)
                    self.telaRota.line_UF_origem.setText('')
                    self.telaRota.line_UF_destino.setText('')
                    self.telaRota.line_cidade_origem.setText('')
                    self.telaRota.line_cidade_destino.setText('')
                    self.telaRota.line_placa.setText('')
                    self.telaRota.horario.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0)))
                    self.telaRota.horario_volta.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0)))
                    self.telaRota.line_valor.setText('')
                    self.QtStack.setCurrentIndex(14)
            else:
                QMessageBox.information(None, 'Rota', 'Placa de carro n cadastrada')
    #ok?
    def procurarRota(self):
        rota_origem = self.telaPrincipal.procurar.text()
        rota_destino = self.telaPrincipal.lineEdit.text()
        self.limpar_layout(self.telaPrincipal.lay)
        if rota_origem == '' or rota_destino == '':
            QMessageBox.information(None, 'Rota', 'Todos os campos devem ser preenchidos')
        else:
            origem = self.rot.get_busca(rota_origem)
            if origem is None:
                origem = 0
                tam = 0
            else:
                tam = (len(origem))

            if origem != None and self.rot.get_busca(rota_destino):
                ctt = 0
                for i in range(tam):
                    if self.rot.verificar_cidade_id(rota_destino, (origem[i].split("'")[1].split("'")[0]).split('/')[0], (origem[i].split("'")[1].split("'")[0]).split('/')[2]):
                        rota_encontrada = self.rot.verificar_cidade((origem[i].split("'")[1].split("'")[0]).split('/')[0])
                        ctt = 1
<<<<<<< HEAD
                        label = QLabel()
                        label.setText(f"Id da rota: {rota_encontrada[1]}\nCidade origem: {rota_encontrada[3]} - {rota_encontrada[2]}\nCidade destino: {rota_encontrada[5]} - {rota_encontrada[4]}\nPlaca: {rota_encontrada[8]}\nHorario de saída: {rota_encontrada[6]}\nHorario de volta: {rota_encontrada[9]}\nValor da passagem: {rota_encontrada[7]}")
                        self.telaPrincipal.lay.addWidget(label)
                        self.chat_reserva(self.telaPrincipal.lay)
                        label2 = QLabel()
                        label2.setText("----------------------------------------------------------------------------------------------------------------")
                        self.telaPrincipal.lay.addWidget(label2)
                        label.setAlignment(Qt.AlignTop)
                        label2.setAlignment(Qt.AlignTop)
=======
                        self.telaPrincipal.label = QLabel()
                        self.telaPrincipal.label.setText(f"Id da rota: {rota_encontrada[1]}\nCidade origem: {rota_encontrada[3]} - {rota_encontrada[2]}\nCidade destino: {rota_encontrada[5]} - {rota_encontrada[4]}\nPlaca: {rota_encontrada[8]}\nHorario de saída: {rota_encontrada[6]}\nHorario de volta: {rota_encontrada[9]}\nValor da passagem: {rota_encontrada[7]}")
                        self.telaPrincipal.lay.addWidget(self.telaPrincipal.label)
                        self.chat_reserva(self.telaPrincipal.lay, rota_encontrada[8])
                        self.numero_placa_atual = rota_encontrada[8]
                        self.telaPrincipal.label2 = QLabel()
                        self.telaPrincipal.label2.setText("----------------------------------------------------------------------------------------------------------------")
                        self.telaPrincipal.lay.addWidget(self.telaPrincipal.label2)
                        self.telaPrincipal.label.setAlignment(Qt.AlignTop)
                        self.telaPrincipal.label2.setAlignment(Qt.AlignTop)
>>>>>>> chat
                        self.telaPrincipal.scrollAreaWidgetContents.setLayout(self.telaPrincipal.lay)
                if ctt == 0:
                    QMessageBox.information(None, 'Busca', 'A rota não existe ou não foi encontrada.')
            else:
                QMessageBox.information(None, 'Rota', 'A rota não existe ou não foi encontrada.')

    def chat_reserva(self, layout, placa):
        botao_chat = QPushButton('chat', self)
        botao_reserva = QPushButton('reserva', self)
    
        # Conectar os botões a métodos específicos
        
        botao_chat.clicked.connect(lambda: self.chat(placa))
        botao_reserva.clicked.connect(lambda: self.chat(placa))

        # Adicionar os botões ao layout
        layout.addWidget(botao_chat)
        layout.addWidget(botao_reserva)

        layout.setAlignment(Qt.AlignTop)

<<<<<<< HEAD
    def chat(self):
        # Lógica para aceitar a rota
        QMessageBox.information(None, 'Ação', 'Chat')
        #self.limpar_layout(lay)
=======
    def chat(self, placa):
        # Lógica para aceitar a rota
        cpf = self.cad.buscar_email_cliente(self.telaInicial.lineEditMail.text())[3]
        self.cad.zerar_mensagens(cpf)
        self.alimentar_chat(cpf, placa)
        carro = self.carro.busca_carro(placa)
        mot = self.cad.busca_cpf_mot(carro[4])
        print(mot[1])
        self.telachat.label.setText(mot[1])
        self.QtStack.setCurrentIndex(15)
        #QMessageBox.information(None, 'Ação', 'Chat')
        #self.limpar_layout(lay)dokadsss
>>>>>>> chat

    def reserva(self):
        # Lógica para negar a rota
        QMessageBox.information(None, 'Ação', 'Reserva')

    def limpar_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def enviar_mensagem(self):
        msg = self.telachat.lineEdit.text()
        print(self.numero_placa_atual)
        max_chars_per_line = 100

        formatted_msg = ""
        for i in range(0, len(msg), max_chars_per_line):
            formatted_msg += msg[i:i + max_chars_per_line]

        cpf = self.cad.buscar_email_cliente(self.telaInicial.lineEditMail.text())[3]
        if self.numero_placa_atual is not None:
            self.cad.guardar_msg(formatted_msg, cpf, self.numero_placa_atual, 0)
            self.telachat.lineEdit.setText("")
            self.alimentar_chat(cpf, self.numero_placa_atual)
        else:
            QMessageBox.information(None, 'Erro', 'Número da placa não disponível.')
        
    def alimentar_chat(self, cpf, placa):
        print('alimentar chat')
        mensagem = self.cad.retirar_msg(cpf, placa)
        # print("passou")
        if mensagem:
            tam = len(mensagem)
        # print(tam)
        # print(mensagem)
            for i in range(tam):
                label = QLabel()
                formatted_msg = mensagem[i].split("'")[1].split("'")[0] + '\n'
                label.setText(f"{formatted_msg}")
                self.telachat.layC.addWidget(label)
                label.setAlignment(Qt.AlignBottom)
                label.setAlignment(Qt.AlignRight)
                self.telachat.layC.setAlignment(Qt.AlignBottom)
                self.telachat.scrollAreaWidgetContents.setLayout(self.telachat.layC)

    #     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     try:
    #         ip_local = socket.gethostbyname(socket.gethostname())
    #         print(f'IP Local: {ip_local}')
    #         client.connect((ip_local, 8000))
    #     except:
    #         return print('\nNão foi possível se conectar ao servidor!\n')

    #     self.sendMessages(client)
    #     self.receiveMessages(client)

    # def receiveMessages(self, client):
    #     print("recebre")
    #     while True:
    #         try:
    #             msg = client.recv(2048).decode()
    #             print("-------------------------------------")
    #             print(msg+'\n')
    #             #return msg
    #         except:
    #             print('\nNão foi possível permanecer conectado no servidor!\n')
    #             print('Pressione <Enter> Para continuar...')
    #             client.close()
    #             break

    # def sendMessages(self, client):
    #     print("Enviar")
    #     while True:
    #         try:
    #             #msg = input('\n')
    #             msg = self.telachat.lineEdit.text()
    #             #self.telachat.label.setText("Dokasd")
    #             max_chars_per_line = 100

    #             formatted_msg = ""
    #             for i in range(0, len(msg), max_chars_per_line):
    #                 formatted_msg += msg[i:i + max_chars_per_line] + "\n"
    #             label = QLabel()
    #             label.setText(f"{formatted_msg}")
    #             self.telachat.layC.addWidget(label)
    #             label.setAlignment(Qt.AlignBottom)
    #             label.setAlignment(Qt.AlignRight)
    #             self.telachat.layC.setAlignment(Qt.AlignBottom)
    #             self.telachat.scrollAreaWidgetContents.setLayout(self.telachat.layC)
    #             self.telachat.lineEdit.setText("")
    #             placa = '1234abc'
    #             cpf_cliente = self.telaperfilcliente.line_nome.text()
    #             codigo = '18/'+formatted_msg+'/'+placa+'/'+cpf_cliente
    #             client.send(codigo.encode())
    #         except:
    #             print("erro")

    def perfil(self):
        cpf = self.telaInicial.lineEditMail.text()
        m = self.cad.buscar_email_mot(cpf)
        if (m != None):
            self.telaperfil.line_nome.setText(m[1])
            self.telaperfil.line_cpf.setText(m[3])
            self.telaperfil.line_enderco.setText(m[2])
            self.telaperfil.line_cnh.setText(m[8])
            self.telaperfil.email.setText(m[7])
            data_str = m[4]
            data_lista = data_str.split('-')
            qdate = QDate(int(data_lista[0]), int(data_lista[1]), int(data_lista[2]))
            self.telaperfil.nascimento.setDate(qdate)
        else: 
            QMessageBox.information(None, 'Perfil', 'CPF não existe.')
    #ok?
    def cadCarro(self):
        placa = self.telacadastrocarro.placa_line.text()
        modelo = self.telacadastrocarro.modelo_line.text()
        tipo = self.telacadastrocarro.tipos_box.currentText()
        email = self.telaInicial.lineEditMail.text()
        cpf = self.cad.buscar_email_mot(email)[3]
        if placa == '' or modelo == '' or tipo == '' or cpf == '':
            QMessageBox.information(None, 'Carro', 'Todos os espaços devem ser preenchidos!')
        else:
            if not (self.carro.busca_carro(placa)):
                self.carro.cadastrar_carro(placa, tipo, modelo, cpf)
                self.telacadastrocarro.placa_line.setText('')
                self.telacadastrocarro.modelo_line.setText('')
                self.telacadastrocarro.tipos_box.setCurrentText('')
                QMessageBox.information(None, 'Carro', 'Cadastro realizado com sucesso.')
                self.QtStack.setCurrentIndex(5)
            else:
                QMessageBox.information(None, 'Rota', 'O carro já existe.')

    #######################################################################
    #######################################################################
    #feito
    def perfil_cliente(self):
        email = self.telaInicial.lineEditMail.text()
        c = self.cad.buscar_email_cliente(email)
        if (c != None):
            self.telaperfilcliente.line_nome.setText(c[1])
            self.telaperfilcliente.line_cpf.setText(c[3])
            self.telaperfilcliente.line_enderco.setText(c[2])
            self.telaperfilcliente.email.setText(c[7])
            data_str = c[4]
            data_lista = data_str.split('-')

            qdate = QDate(int(data_lista[0]), int(data_lista[1]), int(data_lista[2]))
            self.telaperfilcliente.nascimento.setDate(qdate)
        else: 
            QMessageBox.information(None, 'Perfil', 'CPF não existe.')

    def editar_perfil_cliente(self):
        self.telaperfilcliente.line_nome.setReadOnly(False)
        self.telaperfilcliente.line_enderco.setReadOnly(False)
        self.telaperfilcliente.email.setReadOnly(False)
        self.telaperfilcliente.nascimento.setReadOnly(False)

        botao_salvar = QPushButton('Salvar', self)
        botao_salvar.clicked.connect(self.salvar_perfil_cliente)
        self.limpar_layout(self.telaperfilcliente.horizontalLayout_5)
        self.telaperfilcliente.horizontalLayout_5.addWidget(botao_salvar)

    def salvar_perfil_cliente(self):
        nome = self.telaperfilcliente.line_nome.text()
        cpf = self.telaperfilcliente.line_cpf.text()
        endereco = self.telaperfilcliente.line_enderco.text()
        email = self.telaperfilcliente.email.text()
        nascimento = self.telaperfilcliente.nascimento.date()

        if not (nome == '' or cpf == '' or endereco == '' or email == ''):
            if (self.cad.buscar_email_cliente(email) == None):
                if (self.cad.editar_perfil_cliente(nome, cpf, endereco, email, nascimento)):
                    self.telaInicial.lineEditMail.setText(email)
                    self.QtStack.setCurrentIndex(2)
                    #self.telaperfilcliente = PerfilCliente()
                    #conectar botões de voltar e editar
                    self.telaperfilcliente.setupUi(self.stack11)
                    self.telaperfilcliente.b_voltar.clicked.connect(self.voltar_principal_perfil_cliente)
                    self.telaperfilcliente.b_editar.clicked.connect(self.editar_perfil_cliente)
                else:
                    QMessageBox.information(None, 'Cadastro', 'Erro desconhecido')
            else:
                QMessageBox.information(None, 'Cadastro', f'email já cadastrado no banco de dados')
        else:
            QMessageBox.information(None, 'Cadastro', 'Todos os dados devem estar preenchidos!')

    def editar_perfil_motorista(self):
        self.telaperfil.line_nome.setReadOnly(False)
        self.telaperfil.line_enderco.setReadOnly(False)
        self.telaperfil.email.setReadOnly(False)
        self.telaperfil.nascimento.setReadOnly(False)

        botao_salvarM = QPushButton('Salvar', self)
        botao_salvarM.clicked.connect(self.salvar_perfil_motorista)
        self.limpar_layout(self.telaperfil.horizontalLayout_7)
        self.telaperfil.horizontalLayout_7.addWidget(botao_salvarM)

    def salvar_perfil_motorista(self):
        nome = self.telaperfil.line_nome.text()
        cpf = self.telaperfil.line_cpf.text()
        endereco = self.telaperfil.line_enderco.text()
        email = self.telaperfil.email.text()
        nascimento = self.telaperfil.nascimento.date()

        if not (nome == '' or cpf == '' or endereco == '' or email == ''):
            if (self.cad.buscar_email_mot(email) == None):
                if (self.cad.editar_perfil_motorista(nome, cpf, endereco, email, nascimento)):
                    self.telaInicial.lineEditMail.setText(email)
                    self.QtStack.setCurrentIndex(5)
                    self.telaperfil.setupUi(self.stack9)
                    self.telaperfil.b_voltar.clicked.connect(self.voltar_principal)
                    self.telaperfil.b_editar.clicked.connect(self.editar_perfil_motorista)#
                else:
                    QMessageBox.information(None, 'Cadastro', 'Erro desconhecido')
            else:
                QMessageBox.information(None, 'Cadastro', f'email já cadastrado no banco de dados')
        else:
            QMessageBox.information(None, 'Cadastro', 'Todos os dados devem estar preenchidos!')

    #######################################################################
    #feito
    def cad_motorista(self):
        nome = self.telaCadastro.lineEditNome.text()
        endereco = self.telaCadastro.lineEditEndereco.text()
        cpf = self.telacpf.lineEdit_cpf.text()
        nascimento = self.telaCadastro.dateEditNascimento.date()
        usuario = self.telacpf.comboBoxUsuario.currentText()
        senha = self.telaCadastro.lineEditSenha.text()
        email = self.telaCadastro.lineEditMail.text()
        cnh = self.telaMotorista.lineEditCNH.text()

        if cnh == '':
            QMessageBox.information(None, 'motorista', 'Todos os espaços devem ser preenchidos!')
        elif self.cad.busca_cnh(cnh) != None:
            QMessageBox.information(None, 'motorista', 'CNH já cadastrada no bando de dados!')
        else:
            if (self.cad.busca_cpf_mot(cpf) == None):
                if (self.cad.buscar_email_mot(email) == None):
                    if (self.cad.cadastro_mot(nome, endereco, cpf, nascimento, usuario, senha, email, cnh)):
                        self.telaCadastro.lineEditNome.setText('')
                        self.telaCadastro.lineEditEndereco.setText('')
                        self.telaCadastro.lineEditSenha.setText('')
                        self.telaCadastro.lineEditCSenha.setText('')
                        self.telaCadastro.lineEditMail.setText('')
                        self.telaInicial.lineEditMail.setText('')
                        self.telaInicial.lineEditSenha.setText('')
                        self.telacpf.comboBoxUsuario.setCurrentText('')
                        self.telacpf.lineEdit_cpf.setText('')
                        self.telacpf.comboBoxUsuario.setCurrentIndex(0)
                        self.telaCadastro.dateEditNascimento.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0)))
                        self.telaMotorista.lineEditCNH.setText('')
                        QMessageBox.information(None, 'Cadastro', 'Cadastro realizado com sucesso.')
                        self.QtStack.setCurrentIndex(0)
                    else:
                        QMessageBox.information(None, 'Cadastro', 'Pessoa já consta no banco de dados!')
                else:
                    QMessageBox.information(None, 'Cadastro', f'email já cadastrado no banco de dados')
            else:
                QMessageBox.information(None, 'Cadastro', f'Cpf já cadastrado no banco de dados')
    #ok?
    def verificar_cpf(self):
        cpf = self.telacpf.lineEdit_cpf.text()
        usuario = self.telacpf.comboBoxUsuario.currentText()
        if not (cpf == '' or usuario == ''):
            if usuario == 'Usuário Motorista':
                if (self.cad.busca_cpf_mot(cpf) == None):
                    if (self.cad.busca_cpf_cliente(cpf) == None):
                        self.QtStack.setCurrentIndex(1)
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Cadastro")
                        msg.setText("Cpf Já cadastrado no banco de dados como cliente, deseja cadastrar como motorista (Seus dados serão o mesmo da conta cliente) ?")
                        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

                        result = msg.exec()
                        if result == QMessageBox.Yes:
                            self.QtStack.setCurrentIndex(13)
                        else:
                            self.voltar()
                else:
                    QMessageBox.information(None, 'Cadastro', f'Cpf já cadastrado no banco de dados de motorista')
            elif usuario == 'Usuário Cliente':
                if (self.cad.busca_cpf_cliente(cpf) == None):
                    if (self.cad.busca_cpf_mot(cpf) == None):
                        self.QtStack.setCurrentIndex(1)
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Cadastro")
                        msg.setText("Cpf Já cadastrado no banco de dados como motorista, deseja cadastrar como cliente (Seus dados serão o mesmo da conta motorista) ?")
                        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                        result = msg.exec()
                        if result == QMessageBox.Yes:
                            self.QtStack.setCurrentIndex(13)
                        else:
                            self.voltar()
                else:
                    QMessageBox.information(None, 'Cadastro', f'Cpf já cadastrado no banco de dados de cliente')
        else:
            QMessageBox.information(None, 'Cadastro', 'Todos os dados devem estar preenchidos!')

    def confirmar_senha(self):
        senha = self.telacsenha.lineEditSenha.text()
        cpf = self.telacpf.lineEdit_cpf.text()
        if not (senha == ''):
            if self.cad.busca_cpf_cliente(cpf):
                c = self.cad.busca_cpf_cliente(cpf)
                sen = senha
                senha = senha.encode("utf8")
                senha = md5(senha).hexdigest()
                if senha == c[6]:
                    self.telaCadastro.lineEditNome.setText(c[1])
                    self.telacpf.lineEdit_cpf.setText(c[3])
                    self.telaCadastro.lineEditEndereco.setText(c[2])
                    self.telaCadastro.lineEditMail.setText(c[7])
                    data_str = c[4]
                    data_lista = data_str.split('-')
                    # Convertendo para QDate
                    qdate = QDate(int(data_lista[0]), int(data_lista[1]), int(data_lista[2]))
                    self.telaCadastro.dateEditNascimento.setDate(qdate)
                    self.telacpf.comboBoxUsuario.setCurrentIndex(1)
                    self.telaCadastro.lineEditSenha.setText(sen)
                    self.telaCadastro.lineEditCSenha.setText(sen)
                    self.cadastrar()
                else:
                    QMessageBox.information(None, 'Senha', "Senha errada")
            elif self.cad.busca_cpf_mot(cpf):
                c = self.cad.busca_cpf_mot(cpf)
                sen = senha
                senha = senha.encode("utf8")
                senha = md5(senha).hexdigest()
                if senha == c.senha:    
                    self.telaCadastro.lineEditNome.setText(c.nome)
                    self.telacpf.lineEdit_cpf.setText(c.cpf)
                    self.telaCadastro.lineEditEndereco.setText(c.endereco)
                    self.telaCadastro.lineEditMail.setText(c.email)
                    self.telaCadastro.dateEditNascimento.setDate(c.nascimento)
                    self.telacpf.comboBoxUsuario.setCurrentIndex(0)
                    self.telaCadastro.lineEditSenha.setText(sen)
                    self.telaCadastro.lineEditCSenha.setText(sen)
                    self.cadastrar()
                else:
                    QMessageBox.information(None, 'Senha', "Senha errada")
        else:
            QMessageBox.information(None, 'Cadastro', 'Todos os dados devem estar preenchidos!')
    #feito
    def cadastrar(self):
        nome = self.telaCadastro.lineEditNome.text()
        endereco = self.telaCadastro.lineEditEndereco.text()
        cpf = self.telacpf.lineEdit_cpf.text()
        nascimento = self.telaCadastro.dateEditNascimento.date()
        usuario = self.telacpf.comboBoxUsuario.currentText()
        senha = self.telaCadastro.lineEditSenha.text()
        csenha = self.telaCadastro.lineEditCSenha.text()
        email = self.telaCadastro.lineEditMail.text()
        if not (nome == '' or endereco == '' or cpf == '' or usuario == '' or senha == '' or csenha == '' or email == ''):
            if (csenha == senha):
                if usuario == 'Usuário Motorista':
                    self.QtStack.setCurrentIndex(3)
                else:
                    if (self.cad.busca_cpf_cliente(cpf) == None):
                        if (self.cad.buscar_email_cliente(email) == None):
                            if (self.cad.cadastro_user(nome, endereco, cpf, nascimento, usuario, senha, email)):
                                self.telaCadastro.lineEditNome.setText('')
                                self.telaCadastro.lineEditEndereco.setText('')
                                self.telaCadastro.lineEditSenha.setText('')
                                self.telaCadastro.lineEditCSenha.setText('')
                                self.telaCadastro.lineEditMail.setText('')
                                self.telaCadastro.dateEditNascimento.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0)))
                                self.telaInicial.lineEditMail.setText('')
                                self.telaInicial.lineEditSenha.setText('')
                                self.telacpf.comboBoxUsuario.setCurrentText('')
                                self.telacpf.lineEdit_cpf.setText('')
                                QMessageBox.information(None, 'Cadastro', f'Cadastro realizado com sucesso.')
                                self.QtStack.setCurrentIndex(0)
                            else:
                                QMessageBox.information(None, 'Cadastro', 'Pessoa já consta no banco de dados!')
                        else:
                            QMessageBox.information(None, 'Cadastro', f'email já cadastrado no banco de dados')
                    else:
                        QMessageBox.information(None, 'Cadastro', f'Cpf já cadastrado no banco de dados')               
            else:
                QMessageBox.information(None, 'Cadastro', 'Senhas diferentes!')
        else:
            QMessageBox.information(None, 'Cadastro', 'Todos os dados devem estar preenchidos!')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())