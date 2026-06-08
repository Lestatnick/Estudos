import main

while True:
    print('\n=== MENU ===')
    print('1 - Cadastrar Produto')
    print('2 - Atualizar vendas')
    print('3 - Gerar relatorio')
    try:
        opcao = int(input('Digite a opção desejada (0 para sair): '))
    except ValueError:
        print('Digite apenas numeros!')
        continue
    

    if opcao == 1: # Cadastrar Produto
        main.cadastrar_produto()
    elif opcao == 2:
        main.venda()
    elif opcao == 3:
        main.relatorio()
    elif opcao == 0:
        print('encerrando programa!')
        break