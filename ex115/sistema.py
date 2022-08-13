from lib.arquivo import *
from lib.interface import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arqexiste(arq):
    criararq(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        lerarquivo(arq)
        sleep(2)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        cadastro(arq, input('Nome: '), leiaint('Idade: '))
    elif resp == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(2)
