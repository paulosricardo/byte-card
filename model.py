# Projeto ByteCard

from collections import defaultdict
from datetime import date
from datetime import datetime
from random import randint

from dateutil.relativedelta import relativedelta

from excecoes import ValorExcedidoException



class Cartao:

    def __init__(self, numero, validade, cvv, limite, cliente, id=None):

        self.__numero = numero
        self.__validade = validade
        self.__cvv = cvv
        self.__set__limite = limite
        self.__set_cliente(cliente)
        self.__status = 'ATIVO'
        self.__id = id

        # padrao_validade = re.compile('[0-9]{2}\/[0-9]{4}')

        # if not padrao_validade.match(self.__validade):

        # print(f'Cartão com validade inválida: {self.__validade}')

    def cancela(self):
        self.__status = 'CANCELADO'

    @property
    def ativa(self):
        self.__status = 'ATIVO'

    @property
    def id(self):
        return self.__id

    @property
    def numero(self):
        return self.__numero

    @property
    def validade(self):
        return self.__validade

    @property
    def cvv(self):
        return self.__cvv

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite(limite)

    def __set__limite(self, limite):
        limite_minimo = 10
        if limite < limite_minimo:
            raise ValvueError(f'O limite deve ser de no mínimo{limite_minimo}')
        self.__limite = limite

    def __set_cliente(self, cliente):
        self.__cliente = cliente

    @property
    def cliente(self):
        return self.__cliente

    @property
    def status(self):
        return self.__status

    def _str_(self):
        return f'Cartão(#{self.id}) {self.numero} do(a) {self.cliente} com limite de {self.limite} válido até {self.validade}'

    def __set__limite(self, limite):
        limite_minimo = 10
        if limite < limite_minimo:
            raise ValvueError(f'O limite deve ser de no mínimo {limite_minimo}')
        self.__limite = limite


class Compra:
    def __init__(self, valor, data, estabelecimento, categoria, cartao, id=None):

        self.__set__valor(valor)
        self.__data = data
        self.__set__estabelecimento(estabelecimento)
        self.__categoria = categoria.strip()
        self.__set__cartao(cartao)
        self.__id = id
        self.__valida_compra()

        # if len(self.__estabelecimento) > 10:

        # print(f'Nome do estabelecimento grande: {self.__estabelecimento}')

        # dia_da_compra = self.__data.strftime('%d/%m/%Y')

        # hora_da_compra = self.__data.strftime('%H:%M:%S')

        # print(f'Compra realizada no dia {dia_da_compra} na hora {hora_da_compra}')

    @property
    def __set__valor(self, valor):
            if valor <= 0:
                raise ValvueError(f"O valor (valor) deve ser superior a zero")
            self.__valor = valor

    def __set__cartao(self, cartao):
            if cartao is None:
                raise ValvueError("É obrigatório um cartão")
            self.__cartao = cartao

    def __set__estabelecimento(self, estabelecimento):
            limite_caracteres = 30
            limite_estabelecimento = len(estabelecimento)
            if tamanho_estabelecimento > limite_caracteres:
                raise ValvueError(f'Estabelecimento com (tamanho_caracteres) caracteres')
            self.__estabelecimento = estabelecimento.strip()

    @property
    def categoria(self):
        return self.__categoria

    def _str_(self):
        return f'Compra: {self.__valor} no dia {self.__data} em{self.__estabelecimento} no cartão {self.__2cartao.numero}'

    def valida_compra(self):

        limite = self.__cartao.limite

        valor = self.__valor

        if valor > limite:
            valor_excedido = valor - limite

            raise ValorExcedidoException(f'O valor da compra excedeu ${valor_excedido} do limite')


class CompraCredito(Compra):

    def __init__(self, valor, data, estabelecimento, categoria, cartao, quantidade_parcelas=1, id=None):
        super().__init__(valor, data, estabelecimento, categoria, cartao, id)

        self.__quantidade_parcelas = quantidade_parcelas

    @property
    def valor(self):
        return super().valor * 1.1

    @property
    def quantidade_parcelas(self):
        return self.__quantidade_parcelas

    @property
    def valor_parcela(self):
        return self.valor / self.quantidade_parcelas

from model import Cartao, Compra


def cria_numero_do_cartao():
        grupos_de_numeros = [f'{randint(1, 9999):04}' for i in range(4)]
        return ' '.join(grupos_de_numeros)


    
def cria_cvv_do_cartao():
         cvv = f'{randint(1, 999):03}'
         return cvv


def define_validade_do_cartao():
         validade = date.today() + relativedelta(years=4, months=6, day=31)
         return validade


