import os

# - vars
restaurantes=[ # - dicionários
    {'nome':'Plaza','categoria':'japonesa','ativo':False},
    {'nome':'Pizza Suprema','categoria':'italiana','ativo':True},
    {'nome':'Gilbertos','categoria':'brasileira','ativo':False}
    ]

# - init
def exibir_nome_do_programa():
    print('''
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --\n
█▀▀ █▀▀█ █▀▀█ █▀▀▄ 　 ░▀░ █▀▀▄ 　 █░░█ █▀▀█ █▀▄▀█ █▀▀ 
█▀▀ █░░█ █░░█ █░░█ 　 ▀█▀ █░░█ 　 █▀▀█ █░░█ █░▀░█ █▀▀ 
▀░░ ▀▀▀▀ ▀▀▀▀ ▀▀▀░ 　 ▀▀▀ ▀░░▀ 　 ▀░░▀ ▀▀▀▀ ▀░░░▀ ▀▀▀ 
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --''')
    
def exibir_opcoes():
    print('1. Cadastrar restaurante') 
    print('2. Listar restaurante')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida=int(input('Escolha uma opção: '))
        if opcao_escolhida==1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida==2:
            listar_restaurantes()
        elif opcao_escolhida==3:
            alterar_estado_restaurante()
        elif opcao_escolhida==4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

# - options
# - 1
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante=input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria=input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante={'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    voltando_ao_menu()
# - 2
def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante=restaurante['nome']
        categoria_restaurante=restaurante['categoria']
        status_restaurante='ativado' if restaurante['ativo'] else 'desativado'

        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {status_restaurante}')
    voltando_ao_menu()
# - 3
def  alterar_estado_restaurante():
    exibir_subtitulo('Alterando o estado do restaurante')
    nome_restaurante=input('Digite o nome do restaurante que deseja alterar: ')
    restaurante_encontrado=False

    for restaurante in restaurantes:
        if nome_restaurante==restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo']=not restaurante['ativo']
            mensagem=f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
        if not restaurante_encontrado:
            mensagem=f'O restaurante {nome_restaurante} não foi encontrado.'
    print(mensagem)

# - return/finish
def exibir_subtitulo(texto):
    if texto=='main':
        os.system('cls') # os.system('clear') no mac
    else:
        os.system('cls')
        linha='*' * (len(texto))
        print(linha)
        print(texto)
        print(linha)
        print()

def finalizar_app():
    exibir_subtitulo('main')
    print('Encerrando o programa...\n')

def voltando_ao_menu():
    input('\nDigite qualquer tecla para voltar ao menu principal...')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltando_ao_menu()

# -- -- -- -- --

# - main
def main():
    exibir_subtitulo('main')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__=='__main__':
    main()