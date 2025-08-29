import random


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
    numeorHexadecimal = ""
    flag = True
    hex = ["A", "B", "C", "D", "E", "F"]

    while flag:
        resto = numero % 16
        if resto >= 10:
            resto = resto - 10
            numeorHexadecimal = hex[resto] + numeorHexadecimal
        else:
            numeorHexadecimal = str(resto) + numeorHexadecimal
        numero //= 16
        if numero == 0:
            flag = False
    return numeorHexadecimal


##*
# print("Inicio del juego")
# print("elije el modo de juego")
# print("1. Firewall" \
# "2. Servidor" \
# "3. Memoria")
# modo = input("opcion: ")
# if modo == "1":
#     print("El código es:", Firewall())
# elif modo == "2":
#     print("El código es:", Servidor())
# elif modo == "3":
#     print("El código es:", Memoria())
# else:
#     print("Modo de juego no válido.")
