import secrets
import string

def gerar_senha(tamanho):
    grupos = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation,
    ]

    #seleciona pelo menos um caractere de cada grupo
    senha = [secrets.choice(grupo) for grupo in grupos]
    caracteres = ''.join(grupos)
    senha.extend(secrets.choice(caracteres) for i in range(tamanho - len(senha)))

    #embaralha a senha para evitar padrões
    for indice in range(len(senha) - 1, 0, -1):
        troca = secrets.randbelow(indice + 1)
        senha[indice], senha[troca] = senha[troca], senha[indice]

    return ''.join(senha)

print("========== GERADOR DE SENHAS ==========")
print("")
while True:
    try:
        print("Escolha o tamanho da senha que deseja gerar: ")
        tamanho = int(input("Digite um número (ex: 12): "))
        if tamanho < 8:
            print("O tamanho mínimo para garantir complexidade é 8.")
            continue
        senha = gerar_senha(tamanho)
        print(f"Senha gerada: {senha}")
        print("\nDeseja gerar outra senha? (s/n)")
        resposta = input().lower()
        if resposta != 's':
            print("Obrigado por usar o gerador de senhas. Até a próxima!")
            break
    except ValueError:
        print("\nPor favor, digite um número válido.")