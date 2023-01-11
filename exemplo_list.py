frutas = ["Maçã", "Uva", "Banana", "Manga", "Laranja", "Limão"]

print(frutas)
print(type(frutas))
print("Conteúdo do índice 1: ", frutas[1])
print("Total de frutas armazenadas: ", len(frutas))
print("Temos Manga? ", "Manga" in frutas)
print("Temos Morango? ", "Morango" in frutas)

# ---

frutas.append("Morango")  # adiciona item ao final da lista
print("\n", frutas)
print("Temos Morango? ", "Morango" in frutas)
print("Índice para Laranja em frutas: ", frutas.index("Laranja"))

frutas.remove("Uva")
print("\n", frutas)
print("Índice para Laranja em frutas: ", frutas.index("Laranja"))

del frutas[4]
print("\nQuem foi removido?")
print(frutas)

# ---

frutas.insert(2, "Abacaxi")
print("\n", frutas)
print("Índice para Laranja em frutas: ", frutas.index("Laranja"))
print("Qual o índice do Abacaxi? ", frutas.index("Abacaxi"))

print("\n", frutas)
frutas[3] = "Acerola"
print(frutas)

print("\n", frutas)
print(f"Total de itens no list: {len(frutas)}")

# ---

ft = input("\nDigite uma fruta: ")
if (ft in frutas):
    print(f"{ft} existe no list frutas")
else:
    print(f"{ft} não existe no list frutas")

print("\n", frutas)
print("Quantidade do item \"Laranja\" no list frutas: ", frutas.count("Laranja"))
print("Quantidade do item \"Uva\" no list frutas: ", frutas.count("Uva"))

# ---

print("\n", frutas)
frutas.reverse()
print(frutas)

print("\n", frutas)
frutas.sort()
print(frutas)
