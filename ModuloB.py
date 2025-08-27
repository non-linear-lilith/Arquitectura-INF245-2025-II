
def binario_a_decimal(cadena_binaria: str) -> int:
    resultado = 0
    cadena_binaria = cadena_binaria.strip()
    #chekea un input valido
    if not cadena_binaria:
        raise ValueError("Entrada inválida: la cadena está vacía")
    for digito in cadena_binaria:
        if digito not in '01':
            raise ValueError(f"Entrada inválida: '{digito}' no es un dígito binario válido")
        
    longitud: int = len(cadena_binaria)
    for i in range(longitud):
        if(cadena_binaria[longitud-i-1]=='1'):
            resultado =resultado + 2**(i)
    return resultado


def oct_to_decimal(cadena_octal: str) -> int:
    cadena_octal = cadena_octal.strip()
    resultado = 0
    oct_to_dec:dict[str,int] = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7
    }
    for digito in cadena_octal:
        if digito not in '01234567':
            raise ValueError(f"Entrada inválida: '{digito}' no es un dígito octal válido")
    longitud: int = len(cadena_octal)
    for i in range(longitud):
        resultado += oct_to_dec[cadena_octal[longitud-i-1]] * (8**(i))
    return resultado



def hex_to_decimal(cadena_hex: str) -> int:
    cadena_hex = cadena_hex.strip()
    cadena_hex = cadena_hex.upper()
    resultado = 0
    hex_a_dec:dict[str, int] = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    longitud: int = len(cadena_hex)
    for digito in cadena_hex:
        
        if digito not in hex_a_dec:
            raise ValueError(f"Entrada inválida: '{digito}' no es un dígito hexadecimal válido")
    for i in range(longitud):
        digito = hex_a_dec[cadena_hex[longitud-i-1]]
        resultado += digito * (16**(i))
    return resultado

