#Projeto ByteCard 

from datetime import datetime
from model import  Cartao, CompraCredito, Compra
 

visa = Cartao('4321 8765 9807 2222','31/1/2023', '001', 4000.0, 'Ricardo Paulos')
mastercard = Cartao('8765 5432 9090 1111', '05/2035', '789', 6000.0, 'Karina')

print(visa.numero)
print(visa.validade)
print(visa.cvv)
print(visa.limite)
print(visa.cliente)
print(visa.status)
print()

print(mastercard.numero)
print(mastercard.validade)
print(mastercard.cvv)
print(mastercard.limite)
print(mastercard.cliente)
print(mastercard.status)
print()

visa.cancelar()
mastercard.cancelar

print(visa.status)
print(mastercard.status)

visa.limite = 5000.0
mastercard.limite = 9000.0
print(visa.limite)
print(mastercard.limite)
print()


cartao_invalido = Cartao('3333 3333 3333 3333', '5/29', '887', 10000.0, 'BruceWayne')
compra_amazon = CompraCredito(1000.0, datetime(2023, 2, 15, 19, 46, 17), 'Amazon','Casa', visa, 10)
compra_farmacia_visa = Compra(100.0, datetime(2023, 1, 1, 10, 0, 0), 'Farmácia Drosil', 'Saúde', visa)
compra_restaurante_visa = Compra(89.9, datetime(2023, 1, 2, 12, 15, 0), 'Burguer King','Lazer', visa)
compra_supermercado_visa = Compra(475.5, datetime(2023, 2, 3, 7, 5, 5), 'Carrefour','Alimentação', visa)
print()



compra_farmacia_mastercard = Compra(400.0, datetime(2023, 1, 1, 10, 0, 0), 'Farmácia São Paulo','Saúde',mastercard)
compra_restaurante_mastercard = Compra(89.9, datetime(2023, 1, 2, 12, 15, 0), 'Burguer mcdonald', 'Lazer',mastercard)
compra_supermercado_mastercard = Compra(665.5, datetime(2023, 2, 3, 7, 5, 5), 'Atacadão','Alimentação',mastercard)
print()

print(compra_farmacia_visa)
print(compra_farmacia_mastercard)
print()
print(compra_restaurante_visa)
print(compra_restaurante_mastercard)
print()
print(compra_supermercado_visa)
print(compra_supermercado_mastercard)
print()

print(f'Compra a crédito de visa: {compra_amazon.valor} em {compra_amazon.quantidade_parcelas} x de {compra_amazon.valor_parcela}')
fatura = [compra_farmacia_visa, compra_restaurante_visa, compra_supermercado_visa, compra_amazon]
total = 0
for compra in fatura:
	total += compra.valor
print(f'O total da fatura é: {total}')

print(f'Compra a crédito de mastercard: {compra_amazon.valor} em {compra_amazon.quantidade_parcelas} x de {compra_amazon.valor_parcela}')
fatura = [compra_farmacia_mastercard, compra_restaurante_mastercard, compra_supermercado_mastercard, compra_amazon]
total = 0
for compra in fatura:
	total += compra.valor
print(f'O total da fatura é: {total}')
  

 


