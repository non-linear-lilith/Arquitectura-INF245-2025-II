#import ModuloA 
#lo comente porque tiene unas instrucciones que se ejecutan siempre y no verlas me ayuda a ordenarme mejor
#igualmente creo que solo se entrega este archivo, así que cuando terminemos tendremos que pasar todo
# a este archivo, por lo mismo modularizar lo que mas pueda.
import ModuloB

def main():
    binario = "1101"
    decimal = ModuloB.binario_a_decimal(binario)
    print(f"El número binario {binario} en decimal es {decimal}")

    octal = "100"
    decimal_octal = ModuloB.oct_to_decimal(octal)
    print(f"El número octal {octal} en decimal es {decimal_octal}")
    
    hexadecimal = "1A3Ff"
    decimal_hex = ModuloB.hex_to_decimal(hexadecimal)
    print(f"El número hexadecimal {hexadecimal} en decimal es {decimal_hex}")

if __name__ == "__main__":
    main()