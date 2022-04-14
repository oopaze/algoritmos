def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0

    for index, item in enumerate(arr):
        if item < menor:
            menor = item
            menor_indice = index

    return menor_indice


def ordenacao_por_selecao(arr):
    novo_array = []

    for _ in range(len(arr)):
        menor = busca_menor(arr)
        novo_array.append(arr.pop(menor))

    return novo_array


if __name__ == "__main__":
    arr = [9, 4, 1, 78, 6, 34, 2, 434, 34, 343, 5, 12, 42]
    print(ordenacao_por_selecao(arr))
