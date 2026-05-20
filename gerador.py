import random
import string

while True:
    print("Bem-vindo ao Gerador de Senhas!")
    pontuacao = input('Você gostaria de utilizar pontuação na sua senha? (s/n): ')
    try:
        if pontuacao == 's':
            caracteres = string.ascii_letters + string.digits + string.punctuation
        else:
            caracteres = string.ascii_letters + string.digits

        tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
        quantidade_senhas = int(input("Digite a quantidade de senhas que deseja gerar: "))
        for i in range(quantidade_senhas):
            senha = ''.join(random.choice(caracteres) for _ in range(tamanho_senha))
            print(f"Senha {i+1}:", senha)
        break
    except ValueError:
        print("Por favor, digite um número válido.")