import random
import string

while True:
    print("Bem-vindo ao Gerador de Senhas!")
    pontuacao = input('Você gostaria de utilizar pontuação na sua senha? (s/n): ')
    if pontuacao == 's':
        obrigatorio = random.choice(string.ascii_uppercase)  
        obrigatorio += random.choice(string.digits)           
        obrigatorio += random.choice(string.punctuation)      
    try:
        if pontuacao == 's':
            caracteres = string.ascii_letters + string.digits + string.punctuation
        else:
            caracteres = string.ascii_letters + string.digits

        tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
        quantidade_senhas = int(input("Digite a quantidade de senhas que deseja gerar: "))
        if tamanho_senha <= 0 or quantidade_senhas <= 0:
            print("O tamanho da senha e a quantidade de senhas devem ser maiores que zero.")
        else:
            print("Senhas geradas com sucesso!")
        for i in range(quantidade_senhas):
            if pontuacao == 's':
                resto = ''.join(random.choice(caracteres) for _ in range(tamanho_senha - 3))
                senha = list(obrigatorio + resto)
                random.shuffle(senha)
                senha = ''.join(senha)
            else:
                senha = ''.join(random.choice(caracteres) for _ in range(tamanho_senha))
            print(f"Senha {i+1}:", senha)
        
        if tamanho_senha < 8:
            forca = "🔴 Fraca"
        elif tamanho_senha <= 12 and pontuacao == 'n':
            forca = "🟡 Média"
        elif tamanho_senha > 12 and pontuacao == 'n':
            forca = "🟡 Média"
        else:
            forca = "🟢 Forte"
        print("Força da senha:", forca)
        break
    except ValueError:
        print("Por favor, digite um número válido.")