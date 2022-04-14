from timer import timer

@timer
def pesquisa_simples(lista, valor_procurado):
  for index, item in enumerate(lista):
    if item == valor_procurado:
      return index

  return None