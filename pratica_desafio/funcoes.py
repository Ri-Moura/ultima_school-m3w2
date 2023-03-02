def decorator_imprimir(func):
    """
    Decorator que imprime os parâmetros e o resultado de uma função.
    """
    def wrapper(*args, **kwargs):
        """
        Função interna que é responsável por imprimir os parâmetros e o resultado da função original.
        """
        # Armazena os argumentos da função original em variáveis separadas.
        capital, taxa, tempo = args
        
        # Executa a função original.
        result = func(*args, **kwargs)
        
        # Imprime os parâmetros e o resultado da função original.
        print(f"CAPITAL: {capital}, TAXA: {taxa}, TEMPO: {tempo}, RESULTADO: {result}")
        
        # Retorna o resultado da função original.
        return result
    return wrapper

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    """
    Função que calcula juros simples.
    """
    return capital * (taxa / 100) * tempo