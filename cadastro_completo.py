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
    options = ['Ver produto cadrastrado',
               'Cadrastrar nova Produto', 'Sair do sistema', 'Remover Produto']
    for i, k in enumerate(options):
        print(
            f'{cores["amarelo"]}{i + 1}{cores["limpa"]} - {cores["azul"]}{k}{cores["limpa"]}')
    print('-' * 30)


def cadrastrar():
    # vai abrir o arquivo pra ver se ja exite
    adicionar_produto = str(input('Digite o Produto: ').title())
    adicionar_quantidade = int(
        input(f'Digite a quantidade {adicionar_produto} '))
    # abrindo arquivo para checar
    with open(arquivo,) as file:
        result = json.load(file)
        # checar se arquivo ja exites
        existe = False
        for i in result.items():
            if i[0] == adicionar_produto:
                existe = True
    try:
        # se nao exitir vai adicionar
        if existe == False:
            with open(arquivo, 'r+') as file:
                print('Registrando . . .')
                final_product[adicionar_produto] = adicionar_quantidade
                json_produto = json.dumps(final_product)
                file.write(f'{json_produto}\n')
                sleep(0)
                print(
                    f'{cores["verde"]}{adicionar_produto}{cores["limpa"]} registrado com sucesso')
        else:
            print(f'Produto {adicionar_produto} ja exite')

    except:
        print('Erro, falha no registro')
    else:
        menu()


def lerarquivo():
    try:
        with open(arquivo) as file:
            header('PRODUTOS CADASTRADOS')
            print(f'{"Produtos"} \t{"Quantidade"}')
            result = json.load(file)
            for i, k in result.items():
                if len(i) >= 7:
                    print(f'{i} \t\t{k}')
                else:
                    print(f'{i} \t\t\t{k}')

        menu()
    except:
        print('Erro, arquivo nao encontrado')
    else:
        return True


def criararquivo():
    if not lerarquivo():
        with open('arquivo.json', 'wt+') as file:
            file.write('{"Produto": 0}')
            print('criei o arquivo')
            menu()
    else:
        pass


def deletar():
    with open(arquivo, 'rt') as file:
        print(' Produto tal foi deletado')


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
                print(
                    f'{cores["vermelho"]}Por favor selecione corretamente{cores["limpa"]}')
                opcao = int(
                    input(f'{cores["amarelo"]}Sua Opção: {cores["limpa"]}'))
        opcao = int(
            input(f'{cores["amarelo"]}Selecione sua opção: {cores["limpa"]}'))


arquivo = 'arquivo.json'


def copy_list():
    criararquivo()
    produto = {}
    with open(arquivo) as file:
        result = json.load(file)
        produto = result.copy()
    return produto


produto = {}
final_product = copy_list()

selecao()
