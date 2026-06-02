#cli do gerador de senhas 
import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

print("========== GERADOR DE SENHAS ==========")

while True:
    print("\nEscolha o tamanho da senha que deseja gerar: ")
    tamanho = int(input("Digite um número (ex: 12): "))
    senha = gerar_senha(tamanho)
    print(f"Senha gerada: {senha}")