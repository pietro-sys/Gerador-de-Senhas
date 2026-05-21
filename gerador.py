import random
import string
import pyperclip
import os

while True:
    os.system('cls')
    print("Bem-vindo ao Gerador de Senhas!")
    print('1 - Gerar senha.')
    print('2 - Sair.')
    escolha = input("Digite o número da opção desejada: ")

    if escolha == '2':
        print("Saindo do programa. Até mais!")
        break

    elif escolha != '1':
        print("Opção inválida. Por favor, digite '1' para gerar senha ou '2' para sair.")
        continue

    else:
        pontuacao = input('Você gostaria de utilizar pontuação na sua senha? (s/n): ')
        
        if pontuacao == 's':
            obrigatorio = random.choice(string.ascii_uppercase)  
            obrigatorio += random.choice(string.digits)           
            obrigatorio += random.choice(string.punctuation)  

        if pontuacao not in ['s', 'n']:
            print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")
            continue

        try:
            if pontuacao == 's':
                caracteres = string.ascii_letters + string.digits + string.punctuation

            else:
                caracteres = string.ascii_letters + string.digits

            tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
            quantidade_senhas = int(input("Digite a quantidade de senhas que deseja gerar: "))

            if tamanho_senha <= 0 or quantidade_senhas <= 0:
                print("O tamanho da senha e a quantidade de senhas devem ser maiores que zero.")
                continue
            elif tamanho_senha < 4 and pontuacao == 's':
                print("Com pontuação o tamanho mínimo é 4.")
                continue
            else:
                print("Senhas geradas com sucesso!")

            for i in range(quantidade_senhas):
                if pontuacao == 's':

                    # Garante que a senha tenha pelo menos três caracteres obrigatórios
                    resto = ''.join(random.choice(caracteres) for _ in range(tamanho_senha - 3))
                    senha = list(obrigatorio + resto)

                    # Embaralha os caracteres para evitar padrões previsíveis
                    random.shuffle(senha)

                    # Converte a lista de caracteres de volta para uma string
                    senha = ''.join(senha)

                else:
                    senha = ''.join(random.choice(caracteres) for _ in range(tamanho_senha))
                print(f"Senha {i+1}:", senha)
                pyperclip.copy(senha)
                print("Senha copiada para o clipboard!")
            
            if tamanho_senha < 8:
                forca = "🔴 Fraca"

            elif tamanho_senha <= 12 and pontuacao == 'n':
                forca = "🟡 Média"

            elif tamanho_senha > 12 and pontuacao == 'n':
                forca = "🟡 Média"

            else:
                forca = "🟢 Forte"
            print("Força da senha:", forca)
            input('\nPressione Enter para continuar...')
            continue
        
        except ValueError:
            print("Por favor, digite um número válido.")