#Projeto ByteCard 

from Cartao import Cartao

#visa = Cartao()
#mastercard = Cartao()
#print(visa)
#print(mastercard)
 
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




