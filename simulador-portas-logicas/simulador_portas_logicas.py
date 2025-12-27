#─────────────────────────────────────────────────────────
# SIMULADOR DE SISTEMAS BINÁRIOS E PORTAS LÓGICAS
# Descrição: Simula portas lógicas com entradas binárias
#─────────────────────────────────────────────────────────

#─────────────────────────────────────────────────────────
# Portas Lógicas 
#─────────────────────────────────────────────────────────
def porta_and(a, b):
    return a & b

def porta_or(a, b):
    return a | b

def porta_not(a):
    return 1 - a

def porta_xor(a, b):
    return a ^ b
#─────────────────────────────────────────────────────────
# Validação de Entrada
#─────────────────────────────────────────────────────────
def ler_binario(mensagem):
    while True:
        valor = input(mensagem)
        if valor in ['0', '1']:
            return int(valor)
        else:
            print('Entrada inválida! Digite apenas 0 ou 1.')

#─────────────────────────────────────────────────────────
# Tabela Verdade
#─────────────────────────────────────────────────────────
def tabela_verdade(porta):
    print('\nTABELA VERDADE')

    if porta == 'NOT':
        print('A | Saída')
        for a in [0, 1]:
            print(f'{a} | {porta_not(a)}')
    else:
        print('A B | Saída')
        for a in [0, 1]:
            for b in [0, 1]:
                if porta == 'AND':
                    r = porta_and(a, b)
                elif porta == 'OR':
                    r = porta_or(a, b)
                elif porta == 'XOR':
                    r = porta_xor(a, b)
                print(f'{a} {b} | {r}')
                
#─────────────────────────────────────────────────────────
# Menu
#─────────────────────────────────────────────────────────
def menu():
    print('\n「 SIMULADOR DE PORTAS LÓGICAS 」')
    print('1 - AND')
    print('2 - OR')
    print('3 - NOT')
    print('4 - XOR')
    print('5 - Tabela Verdade')
    print('0 - Sair')

#─────────────────────────────────────────────────────────
# Principal
#─────────────────────────────────────────────────────────
def main():
    while True:
        menu()
        opcao = input('Escolha uma opção: ')

        if opcao == '0':
            print('Encerrando o simulador...')
            break

        elif opcao == '1':
            a = ler_binario('Digite A (0 ou 1): ')
            b = ler_binario('Digite B (0 ou 1): ')
            print('Resultado AND:', porta_and(a, b))

        elif opcao == '2':
            a = ler_binario('Digite A (0 ou 1): ')
            b = ler_binario('Digite B (0 ou 1): ')
            print('Resultado OR:', porta_or(a, b))

        elif opcao == '3':
            a = ler_binario('Digite A (0 ou 1): ')
            print('Resultado NOT:', porta_not(a))

        elif opcao == '4':
            a = ler_binario('Digite A (0 ou 1): ')
            b = ler_binario('Digite B (0 ou 1): ')
            print('Resultado XOR:', porta_xor(a, b))

        elif opcao == '5':
            print('\nQual porta?')
            print('1 - AND | 2 - OR | 3 - NOT | 4 - XOR')
            escolha = input('Escolha: ')

            if escolha == '1':
                tabela_verdade('AND')
            elif escolha == '2':
                tabela_verdade('OR')
            elif escolha == '3':
                tabela_verdade('NOT')
            elif escolha == '4':
                tabela_verdade('XOR')
            else:
                print('Opção inválida!')

        else:
            print('Opção inválida!')

#─────────────────────────────────────────────────────────
# Execução 
#─────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
