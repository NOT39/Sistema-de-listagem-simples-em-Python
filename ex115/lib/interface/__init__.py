cor = {'normal': '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m'}


def leiaint(entrada):
    while True:
        try:
            opc = int(input(entrada))
        except (TypeError, ValueError):
            print('ERRO! Digite um número inteiro válido.')
            continue
        except Exception as erro:
            print(f'O erro encontrado foi {erro}')
            continue
        else:
            return opc


def linha(tam=30):
    print('-'*tam)


def cabecalho(msg):
    linha()
    print(msg.center(30))
    linha()


def menu(lista, msg='MENU PRINCIPAL'):
    cabecalho(msg)
    for c, opc in enumerate(lista):
        print(f'{cor["amarelo"]}{c+1}{cor["normal"]} - {cor["azul"]}{opc}{cor["normal"]}')
    linha()
    esc = leiaint(f'{cor["amarelo"]}Sua opção: {cor["normal"]}')
    return esc
