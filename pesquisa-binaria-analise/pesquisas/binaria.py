from timer import timer

@timer
def pesquisa_binaria(lista, valor_procurado):
  baixo = 0
  alto = len(lista) - 1

  while baixo <= alto:
    meio = (alto + baixo) // 2
    chute = lista[meio]

    if chute == valor_procurado:
      return meio

    elif chute > valor_procurado:
      alto = meio - 1
    
    elif chute < valor_procurado:
      baixo = meio + 1

  return None
