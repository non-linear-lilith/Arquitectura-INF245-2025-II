import ModuloA
import ModuloB

def main():
    binario = "1101"
    decimal = ModuloB.binario_a_decimal(binario)
    print(f"El número binario {binario} en decimal es {decimal}")

    octal = "100"
    decimal_octal = ModuloB.oct_to_decimal(octal)
    print(f"El número octal {octal} en decimal es {decimal_octal}")
    
    hexadecimal = "1A3F"
    decimal_hex = ModuloB.hex_to_decimal(hexadecimal)
    print(f"El número hexadecimal {hexadecimal} en decimal es {decimal_hex}")

if __name__ == "__main__":
    main()