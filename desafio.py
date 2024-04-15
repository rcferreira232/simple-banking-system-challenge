menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[l] Limite
[q] Sair
"""

clientes = {
    1: {
        'nome': 'João',
        'saldo': 1000,
        'limite': 500,
        'numero_saque': 0
    },
    2: {
        'nome': 'Maria',
        'saldo': 500,
        'limite': 300,
        'numero_saque': 0
    },
}

while True:
    print(menu)
    opcao = input('Escolha uma opção: ')
    if opcao == 'q':
        break
    elif opcao == 'd':
        cliente = int(input('Digite o número do cliente: '))
        valor = float(input('Digite o valor do depósito: '))
        clientes[cliente]['saldo'] += valor
    elif opcao == 's':
        cliente = int(input('Digite o número do cliente: '))
        valor = float(input('Digite o valor do saque: '))
        if valor > clientes[cliente]['saldo']:
            print('Saldo insuficiente')
        elif valor > clientes[cliente]['limite']:
            print('Limite excedido')
        elif clientes[cliente]['numero_saque'] >= 3:
            print('Número de saques excedido')
        else:
            clientes[cliente]['saldo'] -= valor
            clientes[cliente]['numero_saque'] += 1
    elif opcao == 'e':
        cliente = int(input('Digite o número do cliente: '))
        print(f"""
        Nome: {clientes[cliente]['nome']}
        Saldo: {clientes[cliente]['saldo']}
        Limite: {clientes[cliente]['limite']}
        Número de saques: {clientes[cliente]['numero_saque']}
        """)
    elif opcao == 'l':
        cliente = int(input('Digite o número do cliente: '))
        print(f'Limite: {clientes[cliente]["limite"]}')
    else:
        print('Opção inválida')