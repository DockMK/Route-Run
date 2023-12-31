import socket
import threading
from mysql.connector.utils import print_buffer


class plataforma_cliente():

    def __init__(self):
        self._lista_contas = []

    def conecxao_servidor(self, codigo):

        ip = 'localhost'
        port = 8000
        addr = ((ip, port))
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(addr)
        client_socket.send(codigo.encode())
        print('entrada: '+codigo)
        saida = client_socket.recv(1024).decode()
        client_socket.close()

        return saida

    def cadastro_user(self, nome, endereco, cpf, nascimento, usuario, senha, email):
        codigo = '0/'+nome+'/'+endereco+'/'+cpf+'/'+nascimento.toString("yyyy-MM-dd")+'/'+usuario+'/'+senha+'/'+email
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return False
    
    def busca_cpf_cliente(self, cpf):
        codigo = '1/'+cpf
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst
        return None
    
    def buscar_email_cliente(self, email):
        codigo = '2/'+email
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst
        return None

    def cadastro_mot(self, nome, endereco, cpf, nascimento, usuario, senha, email, cnh):

        codigo = '3/'+nome+'/'+endereco+'/'+cpf+'/'+nascimento.toString("yyyy-MM-dd")+'/'+usuario+'/'+senha+'/'+email+'/'+cnh
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None

    def busca_cpf_mot(self, cpf):
        codigo = '4/'+cpf
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst
        return None

    def buscar_email_mot(self, email):
        codigo = '5/'+email
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst
        return None

    def guardar_num(self, cod):
        self._lista_contas.clear()
        self._lista_contas.append(cod)

    def buscar_cod(self, cod):
        for num in self._lista_contas:
            if num == cod:
                return num
        return None

    def redefinir(self, email, senha):
        codigo = '6/'+email+'/'+senha
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None

    def cadastrar_carro(self, placa, tipo, modelo, cpf):
        codigo = '7/'+placa+'/'+tipo+'/'+modelo+'/'+cpf
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None
    
    def busca_carro(self, placa):
        codigo = '8/'+placa
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst
        return None
    
    def contar(self):
        codigo = '9/'
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return int(saida_lst[1])
        return None
    
    def cadastro_rota(self, id, uf_origem, cidade_origem, uf_destino, cidade_destino, horario, valor, placa, horario_volta):
        codigo = '10/'+str(id)+'/'+uf_origem+'/'+cidade_origem+'/'+uf_destino+'/'+cidade_destino+'/'+horario.toString("HH:mm:ss")+'/'+valor+'/'+placa+'/'+horario_volta.toString("HH:mm:ss")
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None
    
    def add_city(self, id, cidade, uf):
        codigo = '11/'+str(id)+'/'+cidade+'/'+uf

        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None
    
    def get_busca(self, cidade):
        codigo = '12/'+cidade
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('-')
        if (saida_lst[0] == '1'):
            return saida_lst[1].split(',')
        return None

    def verificar_cidade_id(self, cidade, id, uf_cidade):
        codigo = '13/'+cidade+'/'+str(id)+'/'+uf_cidade
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst
        return None
    
    def verificar_cidade(self, id):
        codigo = '14/'+str(id)
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst
        return None
    
    def busca_cnh(self, cnh):
        codigo = '15/'+cnh
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst
        return None

    def editar_perfil_cliente(self, nome, cpf, endereco, email, nascimento):
        codigo = '16/'+nome+'/'+cpf+'/'+endereco+'/'+email+'/'+nascimento.toString("yyyy-MM-dd")
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None

    def editar_perfil_motorista(self, nome, cpf, endereco, email, nascimento):
        codigo = '17/'+nome+'/'+cpf+'/'+endereco+'/'+email+'/'+nascimento.toString("yyyy-MM-dd")
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None
    def guardar_msg(self, msg, remetente, destinatario, sinal):
        codigo = '18/'+msg+'/'+remetente+'/'+destinatario+'/'+str(sinal)
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None
        
    def retirar_msg(self, remetente, destinatario):
        codigo = '19/'+remetente+'/'+destinatario
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('-')
        if (saida_lst[0] == '1'):
            print(saida_lst[1].split(','))
            return saida_lst[1].split(',')
        return None
    
    def zerar_mensagens(self, cpf):
        codigo = '20/'+cpf
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None
    # def enviar_receber(self, msg, placa, cpf_cliente):
    #     codigo = '18/'+msg+'/'+placa+'/'+cpf_cliente
    #     # try:
    #     #     saida = self.conecxao_servidor(codigo)
    #     # except:
    #     #     return False
    #     # print(codigo)
    #     # saida_lst = saida.split('/')
    #     # if (saida_lst[0] == '1'):
    #     #     return True
    #     # return None
    #     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     try:
    #         ip_local = socket.gethostbyname(socket.gethostname())
    #         print(f'IP Local: {ip_local}')
    #         client.connect((ip_local, 8000))
    #     except:
    #         return print('\nNão foi possívvel se conectar ao servidor!\n')

    #     thread1 = threading.Thread(target=self.receiveMessages, args=[client])
    #     thread2 = threading.Thread(target=self.sendMessages, args=[client, codigo])

    #     thread1.start()
    #     thread2.start()