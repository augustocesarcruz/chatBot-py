import os


def processar_resposta(resposta,nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}fffffffff{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}fffffffff{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}fffffffff{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}fffffffff{os.linesep}')
    else:
            print('Digite apenas 1, 2, 3 ou 4')

def start():
    # Apresentar o chatbot
    print('Olá! Bem vindo ao meu chatBot')
    # Pedir o nome
    nome = input('Digite seu nome: ')
    # Pedir o e-mail
    email = input('Digite seu e-mail: ')
    while True:
    # Oferecer o menu de opções
      resposta = input(
        f'O que gostaria de saber?{os.linesep}[1] - Vale a pena aprender Java?{os.linesep}[2] - Quanto tempo leva para conseguir um emprego com Java?{os.linesep}[3] - Quando vou saber que estou BOM o suficiente para conseguir um emprego?{os.linesep}[4] - Onde me recomenda estudar Java para conseguir um emprego hoje?{os.linesep}')
        # Processar a resposta enviada
      processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()