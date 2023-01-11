nomes = {"João", "Maria", "Pedro", "José", "Ana"}
print(type(nomes))  # set
print(nomes)

nomes.add("Jorge")
print(nomes)

nomes.remove("Jorge")
print(nomes)

nomes.add("Maria")  # Não consegue adicionar item repetido
print(nomes)


nomes2 = {"Vanessa", "Jéssica", "Maria", "Ana", "Simone"}
print(nomes2)

uniao = nomes.union(nomes2)  # União dos 2 conjuntos (sem repetições)
print(uniao)

itersecao = nomes.intersection(nomes2)  # Interseção
print(itersecao)
