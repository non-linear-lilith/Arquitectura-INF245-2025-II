
def binario_a_decimal(cadena_binaria: str) -> int:
    resultado = 0
    longitud: int = len(cadena_binaria)
    for i in range(longitud):
        if(cadena_binaria[longitud-i-1]=='1'):
            resultado =resultado + 2**(i)
    return resultado

def oct_to_decimal(cadena_octal: str) -> int:
    resultado = 0
    longitud: int = len(cadena_octal)
    for i in range(longitud):
        resultado += int(cadena_octal[longitud-i-1]) * 8**i
    return resultado

def hex_to_decimal(cadena_hex: str) -> int:
    resultado = 0
    longitud: int = len(cadena_hex)
    for i in range(longitud):
        digito = cadena_hex[longitud-i-1]
        if '0' <= digito <= '9':
            resultado += (ord(digito) - ord('0')) * 16**i
        elif 'A' <= digito <= 'F':
            resultado += (ord(digito) - ord('A') + 10) * 16**i
    return resultado