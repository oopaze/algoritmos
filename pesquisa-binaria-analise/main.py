from pesquisas.simples import pesquisa_simples
from pesquisas.binaria import pesquisa_binaria

if __name__ == '__main__':
  lista_ordenada = list(range(0, 10000000))

  valor_procurado = 9999999

  pesquisa_binaria(lista_ordenada, valor_procurado)
  pesquisa_simples(lista_ordenada, valor_procurado)
