def pesquisa_em_largura(grafo, start='inicio', steps=1, fim='fim'):
    itens = grafo[start]

    for path in itens:
        if path == fim:
            return steps

    for path in itens:
        valor = pesquisa_em_largura(grafo, start=path, steps=steps + 1, fim=fim)

        if valor:
            return valor


if __name__ == '__main__':
    grafo = {}
    grafo['inicio'] = ['A', 'B']
    grafo['A'] = ['C', 'fim']
    grafo['B'] = ['C', 'D']
    grafo['C'] = []
    grafo['D'] = ['fim']

    grafo_secondary = {}
    grafo_secondary['jato'] = ['gato', 'tato']
    grafo_secondary['tato'] = ['gato', 'chato']
    grafo_secondary['gato'] = ['grato', 'gado']
    grafo_secondary['grato'] = ['gado']
    grafo_secondary['chato'] = ['gado']

    print(pesquisa_em_largura(grafo))
    print(pesquisa_em_largura(grafo_secondary, start='jato', fim='gado'))
