verbos = {
    "pular": "elevar-se do chão por impulso dos pés e das pernas",
    "cair": "ir ao chão",
    "devolver": "entregar ou enviar de volta"
}

print(verbos)
print(type(verbos))
print(verbos["cair"])  # ir ao chão


carro = {
    "fabricante": "VW",
    "modelo": "Fusca",
    "cor": "Verde",
    "ano": 1975,
    "donos": ["João", "José", "Maria"]
}
# OBS: Dentro do dicionário carro, "donos" possui conteúdo de lista dinâmica
print(carro)
print(carro["modelo"])  # Fusca


print(carro["donos"])
carro["donos"].append("Maria")  # Adiciona um item ao LIST donos.
print(carro["donos"])
print(carro["donos"][1])  # José

carro['km'] = 115000  # Adiciona uma chave/valor ao final do dicionário
print(carro)

carro['km'] = 173000  # Modifica o valor de uma chave já existente
print(carro)


carro.update({"cor": "Amarelo"})
print(carro)

del carro["km"]
print(carro)

removido = carro.pop("cor")
print(carro)
print(removido)


print(carro.keys())  # Somente as chaves
print(carro.values())  # Somente os valores

print(carro.items())  # Separa chave/valor em tuplas dentro de uma lista

print(carro.get("fabricante"))  # VW
print(carro.get("cor", "Azul")) # Exibe o valor da chave. Se a chave não existir, ele exibe o valor padrão (nesse caso, azul)
print(len(carro)) # 4 -> Total de itens chave/valor (fabricante, modelo, ano, donos)


carro.clear()  # limpa todos os itens do dicionário carro
print(carro)  # {}
