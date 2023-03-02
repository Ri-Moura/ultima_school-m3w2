def decorator_imprimir(func):
    def wrapper(*args, **kwargs):
        capital, taxa, tempo = args
        result = func(*args, **kwargs)
        print(f"CAPITAL: {capital}, TAXA: {taxa}, TEMPO: {tempo}, RESULTADO: {result}")
        return result
    return wrapper

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

