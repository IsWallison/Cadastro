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



def cadrastrar():
    
    adicionar_produto = str(input('Digite o Produto: ').title())
    adicionar_quantidade = int(input(f'Digite a quantidade {adicionar_produto} '))
    try:
        with open(arquivo, 'r+') as file:
            print('Registrando . . .')
            produto[adicionar_produto] = adicionar_quantidade
            json_produto = json.dumps(produto)
            file.write(f'{json_produto}\n')

    except:
        print('Erro, falha no registro')
    else:
        sleep(0.2)
        print(
            f'{cores["verde"]}{produto[adicionar_produto]}{cores["limpa"]} registrado com sucesso')
        menu()


def lerarquivo():
    try:
        with open(arquivo) as file:
            header('PRODUTOS CADASTRADOS')
            print(f'{"Produtos"} \t{"Quantidade"}')
            result = json.load(file)
            for i, k in result.items():
                print(f'{i} \t\t   {k}')

        menu()
    except:
        print('Erro, arquivo nao encontrado')
    else:
        return True


def criararquivo():
    if not lerarquivo():
        with open('arquivo.json', 'wt+') as file:
            print('criei o arquivo')
            pass


def deletar():
    with open(arquivo, 'rt') as file:
        print('a pessoa tal foi deletada')


def selecao():      
    opcao = int(
        input(f'{cores["amarelo"]}Selecione sua opção: {cores["limpa"]}'))
    while opcao in range(1, 5):
        match opcao:
            case  1:
                criararquivo()  # cria / le o arquivo
            case  2:
                header('CADASTANDO PRODUTOS')
                cadrastrar()
            case 3:
                print('Saindo do sistema ... Até logo !!')
                break
            case 4:
                print('deletando')
                deletar()
            case _:
                print(f'{cores["vermelho"]}Por favor selecione corretamente{cores["limpa"]}')
                opcao = int(input(f'{cores["amarelo"]}Sua Opção: {cores["limpa"]}'))
        opcao = int(input(f'{cores["amarelo"]}Selecione sua opção: {cores["limpa"]}'))
            



arquivo = 'arquivo.json'
produto = {}
criararquivo()
with open(arquivo) as file:
    result = json.load(file)
    produto = result.copy()
menu()
selecao()

