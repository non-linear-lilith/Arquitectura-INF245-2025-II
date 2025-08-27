
def binario_a_decimal(cadena_binaria: str) -> int:
    resultado = 0
    longitud: int = len(cadena_binaria)
    for i in range(longitud):
        if(cadena_binaria[longitud-i-1]=='1'):

            resultado =resultado + 2**(i)
 
    return resultado
