def mostra_menor_caminho_completo(pais, inicio, fim):
    fim = pais[fim]
    caminhos = [fim]
    proximo_node = fim

    while proximo_node != inicio:
        proximo_node = pais.get(proximo_node)

        if proximo_node:
            caminhos.append(proximo_node)

    caminhos.reverse()

    return caminhos


def acha_menor_custo(custos, processados):
    custo_mais_baixo = float('inf')
    nodo_custo_mais_baixo = None

    for nodo in custos:
        custo = custos[nodo]

        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo

    return nodo_custo_mais_baixo


def djikstra(grafo, custos, pais, fim):
    processados = []
    nodo = acha_menor_custo(custos, processados)

    while nodo is not None:
        custo = custos[nodo]
        vizinhos = grafo[nodo]

        for n in vizinhos.keys():
            novo_custo = custo + vizinhos[n]

            if custos[n] > novo_custo:
                custos[n] = novo_custo
                pais[n] = nodo

        processados.append(nodo)
        nodo = acha_menor_custo(custos, processados)

    return custos[fim]


if __name__ == '__main__':
    grafo_ponderado = {}

    grafo_ponderado['inicio'] = {}
    grafo_ponderado['inicio']['A'] = 6
    grafo_ponderado['inicio']['B'] = 2

    grafo_ponderado['A'] = {}
    grafo_ponderado['A']['fim'] = 1

    grafo_ponderado['B'] = {}
    grafo_ponderado['B']['A'] = 3
    grafo_ponderado['B']['fim'] = 5

    grafo_ponderado['fim'] = {}

    custos = {}
    custos['A'] = 6
    custos['B'] = 2
    custos['fim'] = float('inf')

    pais = {}
    pais['A'] = 'inicio'
    pais['B'] = 'inicio'
    pais['fim'] = None

    custo_total = djikstra(grafo_ponderado, custos, pais, 'fim')
    print(f'Custo Total: {custo_total}')
    print('Caminho: ', end='')
    print(*mostra_menor_caminho_completo(pais, 'inicio', 'fim'), sep=' -> ')
