import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

print("========== GERADOR DE SENHAS ==========")
print("")
while True:
    try:
        print("Escolha o tamanho da senha que deseja gerar: ")
        tamanho = int(input("Digite um número (ex: 12): "))
        senha = gerar_senha(tamanho)
        print(f"Senha gerada: {senha}")
        print("\nDeseja gerar outra senha? (s/n)")
        resposta = input().lower()
        if resposta != 's':
            print("Obrigado por usar o gerador de senhas. Até a próxima!")
            break
    except ValueError:
        print("\nPor favor, digite um número válido.")