#Projeto ByteCard 

import re

class Cartao:
   

   def __init__(self,numero, validade, cvv, limite, cliente):
     
      self.__numero = numero
      self.__validade = validade
      self.__cvv = cvv
      self.__limite = limite
      self.__cliente = cliente
      self.__status = 'ATIVO'

      padrao_validade = re.compile('[0-9]{2}\/[0-9]{4}')

      if not padrao_validade.match(self.__validade):

         print(f'Cartão com validade inválida: {self.__validade}')



   def cancelar(self):
      self.__status = 'CANCELADO'

   def ativa(self):
      self.__status = 'ATIVO'

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


   @property
   def cliente(self):
      return self.__cliente.title()

   @property
   def status(self):
      return self.__status
   
   @limite.setter
   def limite(self, limite):
      self.__limite = limite

class Compra:

   def __init__(self, valor, data, estabelecimento, categoria, cartao):

         self.__valor = valor
         self.__data = data
         self.__estabelecimento = estabelecimento.strip()
         self.__categoria = categoria.strip()
         self.__cartao = cartao

         if len(self.__estabelecimento) > 10:

            print(f'Nome do estabelecimento grande: {self.__estabelecimento}')
         
         dia_da_compra = self.__data.strftime('%d/%m/%Y')

         hora_da_compra = self.__data.strftime('%H:%M:%S')

         
         print(f'Compra realizada no dia {dia_da_compra} na hora {hora_da_compra}')

   def __str__(self):
         return f'Compra: {self.__valor} no dia {self.__data} em{self.__estabelecimento} no cartão {self.__cartao.numero}'
         


   @property

   def valor(self):
        return self.__valor


class CompraCredito(Compra):

    def __init__(self, valor, data, estabelecimento, categoria, cartao,quantidade_parcelas):
      
      super().__init__(valor, data, estabelecimento, categoria, cartao)

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