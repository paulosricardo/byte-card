from datetime import date, datetime
from collections import defaultdict
from model import Cartao, Compra, cria_numero_do_cartao, cria_cvv_do_cartao, cria_numero_do_cartao, define_validade_do_cartao

cartao1 = Cartao(cria_numero_do_cartao(), date(2031, 1, 31), '321', 1000.0, 'Steve   Rogers', id = 1)
cartao2 = Cartao(cria_numero_do_cartao(), date(2035, 5, 31), '789', 2000.0, 'Matt   Murdock', id = 2)
cartao3 = Cartao(cria_numero_do_cartao(), date(2029, 5, 31), '887', 10000.0, 'Bruce Wayne', id = 3)

#print(cartao1.id)

banco_cartoes = {
    cartao1.id: cartao1,
    cartao2.id: cartao2,
    cartao3.id: cartao3
}

#banco_cartoes = [cartao1, cartao2, cartao3]
sequencia_ids = 0
banco_compras = []

def lista_cartoes():
    return banco_cartoes.values()

def pesquisa_cartao_por_id(id):
    return banco_cartoes.get(id)       

def cadastra_cartao(cliente, limite):
    global sequencia_ids, banco_cartoes
    numero = cria_numero_do_cartao()
    cvv = cria_cvv_do_cartao()
    validade = define_validade_do_cartao()
    novo_cartao = Cartao(numero=numero, validade=validade, cvv=cvv, limite=limite, cliente=cliente, id=sequencia_ids)
    banco_cartoes[novo_cartao.id] = novo_cartao
    sequencia_ids += 1
    
def cadastra_compra(cartao_id, valor, categoria, estabelecimento):
    global banco_compras        
    cartao = pesquisa_cartao_por_id(cartao_id)
    agora = datetime.now()
    nova_compra = Compra(valor=valor, categoria=categoria, estabelecimento=estabelecimento, cartao=cartao, data=agora, id=sequencia_ids)
    banco_compras.append(nova_compra)

def lista_compras():
    return banco_compras

def monta_relatorio_gastos_por_categoria():
    #pass
    gasto_por_categoria = defaultdict(float)
    for compra in lista_compras():
        gasto_por_categoria[compra.categoria] += compra.valor

    return gasto_por_categoria


