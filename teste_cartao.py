#Projeto ByteCard 

from model import Cartao, CompraCredito, Compra

 
visa = Cartao('4321 8765 9807 2222', '07/2032', '001', 4000.0, 'Ricardo Paulos')

mastercard = Cartao('8765 5432 9090 2222', '05/2035', '789', 6000.0, 'Karina')

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

visa.cancela()
mastercard.cancela()

print(visa.status)
print(mastercard.status)

visa.limite = 5000.0

mastercard.limite = 9000.0

print(visa.limite)
print(mastercard.limite)


compra_amazon = CompraCredito(1000.0, '15/02/2023 19:46:17', 'Amazon', 'Casa',visa, 10)


compra_farmacia_visa = Compra(200.0, '01/01/2023 10:00:00', 'Farmácia Drosil','Saude',visa)
compra_restaurante_visa = Compra(89.9, '02/01/2023 12:15:00', 'Burguer King', 'Lazer',visa)
compra_supermercado_visa = Compra(475.5, '03/02/2023 07:05:05', 'Extra','Alimentação',visa)


compra_farmacia_mastercard = Compra(400.0, '06/01/2023 12:30:00', 'Farmácia São Paulo','Saúde',mastercard)
compra_restaurante_mastercard = Compra(89.9, '07/07/2023 15:05:00', 'Burguer mcdonald', 'Lazer',mastercard)
compra_supermercado_mastercard = Compra(475.5, '08/09/2023 07:05:05', 'Atacadão','Alimentação',mastercard)




print(compra_farmacia_visa)
print(compra_farmacia_mastercard)

print(compra_restaurante_visa)
print(compra_restaurante_mastercard)

print(compra_supermercado_visa)
print(compra_supermercado_mastercard)




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
  


