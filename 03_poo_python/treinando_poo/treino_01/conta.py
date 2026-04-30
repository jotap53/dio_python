class Conta:
    def __init__(self, usuario, tipo_de_conta):
        self.usuario = usuario
        self.tipo_de_conta = tipo_de_conta

    def __str__(self):
        return(f'Usuário: {self.usuario} || Tipo da Conta: {self.tipo_de_conta}]')

    def deposito(self):
        valor = float(input('Quanto você quer depositar? '))
        print(f'Valor depositado: {valor}')

    def saque(self):
        valor = float(input('Quanto você quer sacar? '))
        print(f'Valor sacado: {valor}')