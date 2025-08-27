
def binario_a_decimal(cadena_binaria: str) -> int:
    resultado = 0
    longitud: int = len(cadena_binaria)
    for i in range(longitud):
        bit = int(cadena_binaria[longitud - 1 - i])
        resultado += bit * (2 ** i)
    return resultado
