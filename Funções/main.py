produtos = []

def cadastrar_produto():
    nome = str(input('Informe o nome do produto: '))
    preco = float(input('Informe o valor do produto R$: '))
    quantidade_inicial = int(input('Informe a quantidade em estoque: '))

    produto = {
    'nome': nome,
    'preco': preco,
    'estoque': quantidade_inicial,
    'vendas': 0,
    'quantidade_inicial': quantidade_inicial

}
    produtos.append(produto)

def relatorio():
    if len(produtos) == 0:
        print('\nNenhum produto cadastrado!')
    else:
        print('=== RELATORIO ===\n')
        print('Produtos cadastrados:')
        for prod in produtos:
            
            print(f'\nProduto: {prod["nome"]}')
            print(f'Preço unitário: {prod["preco"]}')

            print(f'\nQuantidade inicial: {prod["quantidade_inicial"]}')
            print(f'Quantidade vendida: {prod["vendas"]}')
            print(f'Quantidade restante: {prod["estoque"] }')

            print(f'Valor total vendido: R$ {(prod["vendas"]) * (prod["preco"])}')


def venda():
    if len(produtos) == 0:
        print('\nNenhum produto cadastrado!')
    else:
        print('=== REGISTRAR VENDA ===\n')
        busca = str(input('Digite o nome do produto para atualizar as vendas: ')).strip().lower()
        achou = False
        for i in produtos:
            if i['nome'].lower() == busca:
                achou = True
                venda_atual = int(input('Digite a quantidade vendida para atualizar: '))
                i['vendas'] += venda_atual
                i['estoque'] -= venda_atual
                print('\nValor atualizado com sucesso!')
        if achou == False:
            print('\nProduto não encontrado!')


def limpar_tela():
    print("\033c", end="")

