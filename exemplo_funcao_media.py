'''
Temos uma lista dinâmica onde cada item é um dicionário,
em cada dicionário está o nome e as notas de alunos,
porém, as notas estão dispostas em listas dinâmicas dentro do dicionário.
'''

alunos = [
    {"nome":"Rafael", "notas":[8, 9, 10]},
    {"nome":"Aline", "notas":[5, 7, 6]},
    {"nome":"Carla", "notas":[10, 9]},
    {"nome":"Marcos", "notas":[3, 4, 5, 6]},
]

print("\nExibindo cada item do dicionário:")
for aluno in alunos:
    print(aluno)

print("\nExibindo os itens do dicionário com uma melhor manipulação de dados:")
for aluno in alunos:
    print(f"Aluno: {aluno['nome']} - Notas: {aluno['notas']}")


def calcular_media(notas):
    total_notas = 0
    for nota in notas:
        total_notas += nota
    media = total_notas / len(notas)
    return media


print("\nFazendo uso da função calcular_media e formatando a saída de dados:")
for aluno in alunos:
    nome = aluno["nome"]
    notas = aluno["notas"]
    media = calcular_media(notas)
    print(f"Nome: {nome} - Notas: {notas} - Média: {media}")
