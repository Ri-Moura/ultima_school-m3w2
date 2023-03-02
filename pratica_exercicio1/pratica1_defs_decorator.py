import time

def tempo_de_execucao(func):
    """
    Decorator que mede o tempo de execução de uma função.
    """
    def wrapper(*args, **kwargs):
        """
        Função interna que é responsável por medir o tempo de execução da função original.
        """
        # Armazena o momento em que a função começou a ser executada.
        inicio = time.perf_counter()
        
        # Executa a função original.
        result = func(*args, **kwargs)
        
        # Armazena o momento em que a função terminou de ser executada.
        fim = time.perf_counter()
        
        # Armazena o nome da função original.
        funcao = args[0]
        
        # Calcula o tempo de execução da função.
        tempo = fim - inicio
        
        # Imprime o tempo de execução da função.
        print(f"A função {funcao} levou {tempo:.6f} segundos para ser executada.")
        
        # Retorna o resultado da função original.
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
