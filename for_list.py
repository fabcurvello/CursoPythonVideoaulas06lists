'''
Exemplo para verificar se uma letra inserida pelo usuário
é encontrada em um list de letras, informando todas as
posições encontradas ou se não localizou a letra no list.
'''

# Observe que o list contém letras repetidas, maiúsculas e minúsculas
letras_diversas = ["R", "i", "o", "D", "e", "J", "a", "n", "e", "i", "r", "o"]
localizacao = []
total_encontradas = 0
print(letras_diversas)

pesquisa = input("Digite uma letra para pesquisa em letras_diversas: ")

# index recebe o NÚMERO da posição atual do laço, de zero ao último índice do list
for index in range(len(letras_diversas)):

    # se a letra que está na posição index de letras_diversas em minúscula (lower)
    # for igual a pesquisa em minúscula
    if (letras_diversas[index].lower() == pesquisa.lower()):
        print(letras_diversas[index], " encontrada na posição ", index)
        total_encontradas = total_encontradas + 1
        localizacao.append(index)

# se total_encotradas terminar valendo 0 então a tentativa não foi encontrada no list
if (total_encontradas == 0):
    print(f"--- {pesquisa} não localizada em letras_diversas ---")
else:
    print(f"--- {pesquisa} foi encontrada {total_encontradas} vez(es) em letras_diversas ---")
    print(localizacao)

mensagens = [
    "Olá Mundo!",
    "Python é melhor que Java",
    "Na verdade TUDO depende do Banco de Dados",
    "Alguém aqui falou em programação No-Code?"
]

for mensagem in mensagens:
    print(mensagem)

for indice, mensagem in enumerate(mensagens):
    print(f"{indice} - {mensagem}")
