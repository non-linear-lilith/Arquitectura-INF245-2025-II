import json
import random

RESULTS_FILE = "game_results.json"


#
# Nombre: GenerarRandom
# Input: numero1 (entero), numero2 (entero)
# Resumen: Genera un numero entero aleatorio dentro de un rango especifico, incluyendo los limites.
# Output: Un numero entero aleatorio (entero)
#
def GenerarRandom(numero1, numero2):
    numero = random.randint(numero1, numero2)
    return numero
#
# Nombre: Firewall
# Input: Ninguno
# Resumen: Genera un número entero aleatorio entre 1 y 64 y lo convierte a su representación binaria.
# Output: El número binario (string)
#
def Firewall():
    numero = GenerarRandom(1, 64)
    return DecimalBinario(numero)
#
# Nombre: Servidor
# Input: Ninguno
# Resumen: Genera un numero entero aleatorio entre 1 y 512 y lo convierte a su representacion octal.
# Output: El numero octal (string)
#
def Servidor():
    numero = GenerarRandom(1, 512)
    return DecimalOctal(numero)
#
# Nombre: Memoria
# Input: Ninguno
# Resumen: Genera un numero entero aleatorio entre 1 y 4095 y lo convierte a su representacion hexadecimal.
# Output: El numero hexadecimal (string)
#
def Memoria():
    numero = GenerarRandom(1, 4095)
    return DecimalHexadecimal(numero)
#
# Nombre: DecimalBinario
# Input: numero (entero)
# Resumen: Convierte un numero entero a su representacion binaria usando divisiones sucesivas.
# Output: El numero binario (string)
#
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
#
# Nombre: DecimalOctal
# Input: numero (entero)
# Resumen: Convierte un numero entero a su representacion octal usando divisiones sucesivas.
# Output: El numero octal (string)
#
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
#
# Nombre: DecimalHexadecimal
# Input: numero (entero)
# Resumen: Convierte un numero entero a su representacion hexadecimal usando divisiones sucesivas y si el resto es 10 o mas busca su letra
# correspondiente en hex.
# Output: El numero hexadecimal (string)
#
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

#
# Nombre: binario_a_decimal
# Input: cadena_binaria (string)
# Resumen: Convierte una cadena binaria a su equivalente decimal. La funcion primero valida que la cadena
# no este vacia y que solo contenga los caracteres '0' y '1'. Luego, recorre la cadena de derecha a izquierda,
# sumando potencias de 2 por cada '1' que encuentra.
# Output: El numero decimal (entero)

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
#
# Nombre: oct_to_decimal
# Input: cadena_octal (string)
# Resumen: Convierte una cadena de numeros octales a su equivalente decimal. La funcion valida la entrada y luego suma las potencias de 8 correspondientes a cada digito.
# Output: El numero decimal (entero)
#
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
#
# Nombre: hex_to_decimal
# Input: cadena_hex (string)
# Resumen: Convierte una cadena de numeros hexadecimales a su equivalente decimal. La funcion valida la entrada y luego suma las potencias de 16 correspondientes a cada digito.
# Output: El numero decimal (entero)
#
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

#
# Nombre: cargar_resultados
# Input: Ninguno
# Resumen: Carga los datos de un archivo JSON. Si el archivo no existe, devuelve un diccionario con los valores iniciales.
# Output: Un diccionario con los datos del juego (dict)
#
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
#
# Nombre: guardar_resultados
# Input: resultados (dict)
# Resumen: Guarda un diccionario en un archivo en formato JSON.
# Output: Ninguno
#
def guardar_resultados(resultados):
    with open(RESULTS_FILE, "w") as f:
        json.dump(resultados, f, indent=4)
#
# Nombre: juego
# Input: Ninguno
# Resumen: Funcion principal del juego. Carga los resultados, muestra las estadisticas, y ejecuta el ciclo de juego para la conversion de numeros.
# Output: Ninguno
#
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
#
# Nombre: main
# Input: Ninguno
# Resumen: Funcion principal del programa. Muestra el menu inicial y gestiona el flujo del juego, permitiendo al usuario jugar multiples partidas o salir.
# Output: Ninguno
#
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