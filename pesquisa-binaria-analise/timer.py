import time

def timer(func):
  def wrapper(*args, **kwargs):
    agora = time.time()
    resultado = func(*args, **kwargs)
    final = time.time()

    print(f"{final - agora:.5f}s")
    return resultado
  
  return wrapper