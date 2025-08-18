# lista = [3,9,11,65,4,3,12,62,79,12,17,21,5,1,9,123]

lista = [7, 12, 5, 9]

tamanho = len(lista)

print("Tamanho da Lista: ", tamanho)

for passos in range(tamanho):
    change = False

    for j in range(0, tamanho - 1 - passos):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            change = True
    if not change:
        break
print(lista)
