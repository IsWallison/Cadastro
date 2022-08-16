from time import sleep
import json



cores = {"limpa": '\033[m',
         "azul": '\033[34m',
         "amarelo": '\033[33m',
         "vermelho": '\033[31m',
         "verde": '\033[32m'}


def header(txt):
    print('-' * 30)
    print(f"{txt:^30}")
    print('-' * 30)


def menu():
    header('MENU PRINCIPAL')
    options = ['Ver produto cadrastradas',
               'Cadrastrar nova pessoa', 'Sair do sistema', 'Remover pessoa']
    for i, k in enumerate(options):
        print(
            f'{cores["amarelo"]}{i + 1}{cores["limpa"]} - {cores["azul"]}{k}{cores["limpa"]}')
    print('-' * 30)


def mostrar():
    print('produto cadrastadas: ')
    for i, k in enumerate(produtos):
        print(f'{k["Produto"]} \t\t{k["Quantidades"]}')
    menu()


def cadrastrar():
    produto["Produto"] = str(input('Digite o Produto: ').title())
    try:
        with open(arquivo, 'a') as file:
            produto["Quantidades"] = int(input(f'Digite a quantidade {produto["Produto"]} '))
            print('Registrando . . .')
            file.write(f'{produto["Produto"]};{produto["Quantidades"]}\n')

    except:
        print('Erro, falha no registro')
    else:
        sleep(0.2)
        print(
            f'{cores["verde"]}{produto["Produto"]}{cores["limpa"]} registrado com sucesso')
        menu()


def lerarquivo():
    try:
        with open(arquivo, 'r') as file:
            header('PRODUTOS CADASTRADOS')
            print(f'{"Produtos"} \t{"Quantidade"}')
            for linha in file:
                dado = linha.split(';')
                print(f'{dado[0]:<20}{dado[1]:>3}',end='')

        menu()
    except:
        print('Erro, arquivo nao encontrado')
    else:
        return True


def criararquivo():
    if not lerarquivo():
        with open('arquivo.txt', 'wt+') as file:
            print('criei o arquivo')
            pass


def deletar():
    with open(arquivo, 'rt') as file:
        print('a pessoa tal foi deletada')


def selecao():
    opcao = int(
        input(f'{cores["amarelo"]}Selecione sua opção: {cores["limpa"]}'))
    while opcao in range(1, 5):
        if opcao not in range(1, 5):
            print(
                f'{cores["vermelho"]}Por favor selecione corretamente{cores["limpa"]}')
            opcao = int(
                input(f'{cores["amarelo"]}Sua Opção: {cores["limpa"]}'))
        elif opcao == 1:
            criararquivo()  # cria / le o arquivo
        elif opcao == 2:
            header('CADASTANDO PRODUTOS')
            cadrastrar()
        elif opcao == 3:
            print('Saindo do sistema ... Até logo !!')
            break
        elif opcao == 4:
            print('deletando')
            deletar()
        opcao = int(
            input(f'{cores["amarelo"]}Selecione sua opção: {cores["limpa"]}'))


arquivo = 'arquivo.txt'
produto = {}
produtos = []
menu()
selecao()


