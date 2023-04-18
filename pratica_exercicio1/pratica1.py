import time

def tempo_de_execucao(func):
    def wrapper(*args, **kwargs):
        inicio=time.perf_counter()
        result = func(*args, **kwargs)
        fim=time.perf_counter()
        
        funcao=func.__name__
        
        tempo = fim - inicio
        
        print(f"A função {funcao} levou {tempo:.6f} segundos para ser executada.")
        
        return result
    return wrapper

@tempo_de_execucao
def funcao_x(funcao):
    """
    Função de exemplo que `stopa` por 2 segundos.
    """
    time.sleep(2)
    return funcao

@tempo_de_execucao
def funcao_y(funcao):
    """
    Função de exemplo que `stopa` por 7 segundos.
    """
    time.sleep(7)
    return funcao

@tempo_de_execucao
def funcao_z(funcao):
    """
    Função de exemplo que `stopa` por 12 segundos.
    """
    time.sleep(12)
    return funcao
