import textwrap
from datetime import datetime
import os
from abc import ABC, abstractclassmethod, abstractproperty

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.conta = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar()

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Cliente:
    def __init__(self, nome, data_de_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

def sacar(self, valor):
    saldo = self.saldo
    excedeu_saldo = valor > saldo

    if excedeu_saldo:
        print("---Falha na operação! \nVocê não tem limite suficiente para realizar o saque!---")
    
    elif valor > 0:
        print("===\nSaque realizado com sucesso!===")
    
    else:
        print('---Falha na operação! \nO valor digitado é inválido!')
    
        return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("===Depósito realizado com sucesso!===")
        
        else:
            print("---Falha na operação! Valor difitado inválido!---")
            return False
        return False
    
class ContaCorrente:
    def __init__(self, numero, cliente, limite = 500, limite_saque = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self):
        numero_saques = len(transacao for transacao in self.historico.transacoes if transacao["tipo"] == saque.__name__)
        execedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.numero_saques

        if execedeu_limite:
            print("---Falha na operação! \nValor do saque excedeu o limite!")
        
        elif excedeu_saques:
            print('---Falha na operação! \nO número máximo de saques excedeu!')

        else:
            return super().sacar(valor)
        
        return False

    def __str__(self):
        return f"""
            Agência:\t{self.agencia}
            C\C: \t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes (self):
        self.transacoes

    @property
    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor (self):
        pass

    @abstractclassmethod
    def registra(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self.valor

    def registrar(self):
        sucesso_transacao = conta.sacar(valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
