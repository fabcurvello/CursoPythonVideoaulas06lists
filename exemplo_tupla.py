sudeste = ("RJ", "ES", "SP", "MG")  # Criação da tupla.
print(type(sudeste))
print(sudeste)

print(sudeste[0])  # RJ
print(sudeste[-1])  # MG (o último)
print(sudeste[:2])  # RJ, ES (0, 1, 2 -> exceto o próprio 2)
print(sudeste[1:3])  # ES, SP(1, 2, 3 -> exceto o próprio 3)
print(sudeste[::2])  # RJ, SP (1 a cada 2 posições)

print(len(sudeste))  # 4 ->Total de itens
print(sudeste.index("SP"))  # 2
print(sudeste.count("SP"))  # 1 -> Quantos itens SP existem na tupla
