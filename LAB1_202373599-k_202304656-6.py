import json
import random

RESULTS_FILE = "game_results.json"

# Functions from ModuloA
def GenerarRandom(numero1, numero2):
    numero = random.randint(numero1, numero2)
    return numero

def Firewall():
    numero = GenerarRandom(1, 64)
    return DecimalBinario(numero)

def Servidor():
    numero = GenerarRandom(1, 512)
    return DecimalOctal(numero)

def Memoria():
    numero = GenerarRandom(1, 4095)
    return DecimalHexadecimal(numero)

def DecimalBinario(numero):
    numeroBinario = ""
    flag = True

    while flag:
        resto = numero % 2
        numeroBinario = str(resto) + numeroBinario
        numero //= 2
        if numero == 0:
            flag = False
    return numeroBinario

def DecimalOctal(numero):
    numeroOctal = ""
    flag = True

    while flag:
        resto = numero % 8
        numeroOctal = str(resto) + numeroOctal
        numero //= 8
        if numero == 0:
            flag = False
    return numeroOctal

def DecimalHexadecimal(numero):
    numeroHexadecimal = ""
    flag = True
    hex = ["A", "B", "C", "D", "E", "F"]

    while flag:
        resto = numero % 16
        if resto < 10:
            numeroHexadecimal = str(resto) + numeroHexadecimal
        else:
            numeroHexadecimal = hex[resto - 10] + numeroHexadecimal
        numero //= 16
        if numero == 0:
            flag = False
    return numeroHexadecimal

# Functions from ModuloB
def binario_a_decimal(cadena_binaria: str) -> int:
    resultado = 0
    cadena_binaria = cadena_binaria.strip()
    
    if not cadena_binaria:
        raise ValueError("Entrada inválida: la cadena está vacía")
    
    for digito in cadena_binaria:
        if digito not in '01':
            raise ValueError(f"Carácter inválido: {digito}")
        
    longitud: int = len(cadena_binaria)
    for i in range(longitud):
        if(cadena_binaria[longitud-i-1]=='1'):
            resultado += 2**i
    return resultado

def oct_to_decimal(cadena_octal: str) -> int:
    cadena_octal = cadena_octal.strip()
    resultado = 0
    oct_to_dec: dict[str,int] = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7
    }
    
    for digito in cadena_octal:
        if digito not in oct_to_dec:
            raise ValueError(f"Carácter inválido para octal: {digito}")
    
    longitud: int = len(cadena_octal)
    for i in range(longitud):
        resultado += oct_to_dec[cadena_octal[longitud-i-1]] * (8**i)
    return resultado

def hex_to_decimal(cadena_hex: str) -> int:
    cadena_hex = cadena_hex.strip()
    cadena_hex = cadena_hex.upper()
    resultado = 0
    hex_a_dec: dict[str, int] = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    
    longitud: int = len(cadena_hex)
    for digito in cadena_hex:
        if digito not in hex_a_dec:
            raise ValueError(f"Carácter inválido para hexadecimal: {digito}")
        
    for i in range(longitud):
        resultado += hex_a_dec[cadena_hex[longitud-i-1]] * (16**i)
    return resultado

# Game functions
def cargar_resultados():
    try:
        with open(RESULTS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "record": 0,
            "last_play_level": 1,
            "successful_binary": 0,
            "successful_octal": 0,
            "successful_hex": 0
        }

def guardar_resultados(resultados):
    with open(RESULTS_FILE, "w") as f:
        json.dump(resultados, f, indent=4)

def juego():
    resultados = cargar_resultados()
    gamemode = {
        '1': ("Firewall",
            Firewall,
            "binario",
            binario_a_decimal,
            "successful_binary"),
        '2': ("Servidor", 
            Servidor,
            "octal",
            oct_to_decimal,
            "successful_octal"),
        '3': ("Memoria",
            Memoria,
            "hexadecimal",
            hex_to_decimal,
            "successful_hex")
    }
    print("\n" * 50)
    print(f"Tu récord actual: {resultados['record']}")
    print(f"La ultima vez que jugaste llegaste al nivel: {resultados['last_play_level']}")
    print(f"Respuestas correctas por modo de juego:")
    print(f"  - Firewall (binario): {resultados['successful_binary']}")
    print(f"  - Servidor (octal): {resultados['successful_octal']}")
    print(f"  - Memoria (hexadecimal): {resultados['successful_hex']}")

    nivel = 1
    while True:
        print(f"Nivel actual: {nivel}")
        if(nivel == (resultados['record']+1)):
            print("¡Felicidades! Has alcanzado un nuevo récord.")
        
        while True:
            modo = input(f"Elige el modo de juego:\n1. Firewall (binario)\n2. Servidor (octal)\n3. Memoria (hexadecimal)\ne. Salir (terminar run)\nOpción: ").strip()
            
            if modo == 'e':
                break
            elif modo in ['1', '2', '3']:
                break
            else:
                print("Modo de Juego no válido. Por favor ingrese 1, 2, 3 o e.")
        
        if modo == 'e':
            break
            
        print("Modo de Juego: " + gamemode[modo][0])

        numero_a_traducir = gamemode[modo][1]()
        respuesta_correcta = str(gamemode[modo][3](numero_a_traducir))
        print(f"Usted debe traducir el numero {numero_a_traducir} del {gamemode[modo][2]} a entero")

        while True:
            respuesta = input("Ingrese su respuesta o ingrese \"e\" ( de exit) para salir: ").strip()
            if respuesta == "e":
                break
            elif respuesta.isdigit() or (respuesta.startswith('-') and respuesta[1:].isdigit()):
                break
            else:
                print("Por favor ingrese solo números o 'e' para salir.")
        
        if respuesta == "e":
            break
        
        if respuesta == respuesta_correcta:
            print("\n" + "¡Respuesta correcta!" + "\n" * 4)
            resultados[gamemode[modo][4]] += 1
            nivel += 1
            if nivel > resultados['record']:
                resultados['record'] = nivel
        else:
            while True:
                print("Respuesta incorrecta, vuelva a intentarlo, o RINDASE Y LARGUESE (e)")
                respuesta = input("Ingrese su respuesta o ingrese \"e\" ( de exit) para salir: ").strip()
                if respuesta == "e":
                    break
                elif not (respuesta.isdigit() or (respuesta.startswith('-') and respuesta[1:].isdigit())):
                    print("Por favor ingrese solo números o 'e' para salir.")
                    continue
                elif respuesta == respuesta_correcta:
                    print("¡Respuesta correcta!")
                    resultados[gamemode[modo][4]] += 1
                    nivel += 1
                    if nivel > resultados['record']:
                        resultados['record'] = nivel
                    break

    resultados['last_play_level'] = nivel
    guardar_resultados(resultados)
    
def main():
    print("¡Bienvenido al Desafio del Legendario ByteMaster©!")
    print("¿Que desea hacer ahora?")
    print("1. Jugar")
    print("2. Salir")
    
    while True:
        opcion = input("Opción: ").strip()
        if opcion in ['1', '2']:
            break
        else:
            print("Opción no válida. Por favor ingrese 1 o 2.")
    
    if opcion == "1":
        flag_playing = True
        while flag_playing:
            juego()
            print("Menu principal")
            
            while True:
                continuar = input("¿Continuar jugando en un nuevo nivel? (s/n): ").strip().lower()
                if continuar in ['s', 'n']:
                    break
                else:
                    print("Opción no válida, por favor ingrese 's' para sí o 'n' para no.")
            
            if continuar == 'n':
                print("Gracias por jugar. ¡Hasta luego!")
                flag_playing = False
                
    elif opcion == "2":
        print("¡Hasta luego!")

if __name__ == "__main__":
    main()