"""

ESTO LO USO COMO GUIA, AUNQUE LA VERDAD ES QUE TIENE HARTOS FALLOS
ANTES DE ENTREGAR EL PROGRAMA LO VOY A BORRAR OBVIAMENTE

"""

import random

# ============================================================================
# SECCIÓN 1: FUNCIONES DE CONVERSIÓN DE OTRAS BASES A DECIMAL
# ============================================================================

def binario_a_decimal(cadena_binaria):
    """
    Convierte un número binario (base 2) a decimal (base 10).
    
    Algoritmo:
    1. Recorremos la cadena de derecha a izquierda
    2. Cada dígito se multiplica por 2^posición
    3. Sumamos todos los resultados
    
    Ejemplo: 1011 = 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0 = 8 + 0 + 2 + 1 = 11
    
    Args:
        cadena_binaria (str): Número en binario como string (ej: "1011")
    
    Returns:
        int: Número convertido a decimal
    """
    
    # Verificación de entrada válida
    if not cadena_binaria:
        return 0
    
    # Verificar que solo contenga 0s y 1s
    for digito in cadena_binaria:
        if digito not in '01':
            raise ValueError(f"Entrada inválida: '{digito}' no es un dígito binario válido")
    
    resultado = 0  # Acumulador para el resultado final
    longitud = len(cadena_binaria)
    
    # Recorremos cada dígito de la cadena
    for i in range(longitud):
        # Obtenemos el dígito actual (de izquierda a derecha)
        digito = int(cadena_binaria[i])
        
        # Calculamos la posición desde la derecha
        # Por ejemplo, en "1011", el primer '1' está en posición 3
        posicion = longitud - 1 - i
        
        # Calculamos el valor: dígito * (base ^ posición)
        # En binario, base = 2
        valor_posicional = digito * (2 ** posicion)
        
        # Sumamos al resultado
        resultado += valor_posicional
        
        # Debug: Descomenta para ver el proceso paso a paso
        # print(f"Posición {posicion}: {digito} * 2^{posicion} = {valor_posicional}")
    
    return resultado


def octal_a_decimal(cadena_octal):
    """
    Convierte un número octal (base 8) a decimal (base 10).
    
    Algoritmo:
    1. Recorremos la cadena de derecha a izquierda
    2. Cada dígito se multiplica por 8^posición
    3. Sumamos todos los resultados
    
    Ejemplo: 157 = 1*8^2 + 5*8^1 + 7*8^0 = 64 + 40 + 7 = 111
    
    Args:
        cadena_octal (str): Número en octal como string (ej: "157")
    
    Returns:
        int: Número convertido a decimal
    """
    
    # Verificación de entrada válida
    if not cadena_octal:
        return 0
    
    # Verificar que solo contenga dígitos del 0 al 7
    for digito in cadena_octal:
        if digito not in '01234567':
            raise ValueError(f"Entrada inválida: '{digito}' no es un dígito octal válido")
    
    resultado = 0  # Acumulador para el resultado final
    longitud = len(cadena_octal)
    
    # Recorremos cada dígito de la cadena
    for i in range(longitud):
        # Obtenemos el dígito actual
        digito = int(cadena_octal[i])
        
        # Calculamos la posición desde la derecha
        posicion = longitud - 1 - i
        
        # Calculamos el valor: dígito * (base ^ posición)
        # En octal, base = 8
        valor_posicional = digito * (8 ** posicion)
        
        # Sumamos al resultado
        resultado += valor_posicional
        
        # Debug: Descomenta para ver el proceso paso a paso
        # print(f"Posición {posicion}: {digito} * 8^{posicion} = {valor_posicional}")
    
    return resultado


def hexadecimal_a_decimal(cadena_hex):
    """
    Convierte un número hexadecimal (base 16) a decimal (base 10).
    
    Algoritmo:
    1. Recorremos la cadena de derecha a izquierda
    2. Cada dígito se multiplica por 16^posición
    3. Los dígitos A-F se convierten a 10-15
    4. Sumamos todos los resultados
    
    Ejemplo: 2AF = 2*16^2 + 10*16^1 + 15*16^0 = 512 + 160 + 15 = 687
    
    Args:
        cadena_hex (str): Número en hexadecimal como string (ej: "2AF")
    
    Returns:
        int: Número convertido a decimal
    """
    
    # Verificación de entrada válida
    if not cadena_hex:
        return 0
    
    # Convertimos a mayúsculas para simplificar
    cadena_hex = cadena_hex.upper()
    
    # Diccionario para mapear caracteres hexadecimales a valores decimales
    hex_a_dec = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    
    # Verificar que todos los caracteres sean válidos
    for caracter in cadena_hex:
        if caracter not in hex_a_dec:
            raise ValueError(f"Entrada inválida: '{caracter}' no es un dígito hexadecimal válido")
    
    resultado = 0  # Acumulador para el resultado final
    longitud = len(cadena_hex)
    
    # Recorremos cada dígito de la cadena
    for i in range(longitud):
        # Obtenemos el valor decimal del carácter actual
        valor_digito = hex_a_dec[cadena_hex[i]]
        
        # Calculamos la posición desde la derecha
        posicion = longitud - 1 - i
        
        # Calculamos el valor: dígito * (base ^ posición)
        # En hexadecimal, base = 16
        valor_posicional = valor_digito * (16 ** posicion)
        
        # Sumamos al resultado
        resultado += valor_posicional
        
        # Debug: Descomenta para ver el proceso paso a paso
        # print(f"Posición {posicion}: {cadena_hex[i]} ({valor_digito}) * 16^{posicion} = {valor_posicional}")
    
    return resultado


# ============================================================================
# SECCIÓN 2: SISTEMA DE DESAFÍO (MODALIDAD 2)
# ============================================================================

class SistemaDesafio:
    """
    Clase que maneja el sistema de desafío de descifrado.
    Incluye niveles, puntuación y validación de respuestas.
    """
    
    def __init__(self):
        """Inicializa el sistema de desafío con valores por defecto."""
        self.nivel_actual = 1
        self.puntuacion = 0
        self.intentos_totales = 0
        self.intentos_correctos = 0
        self.racha_actual = 0  # Número de aciertos consecutivos
        self.mejor_racha = 0   # Mejor racha de aciertos
        
    def obtener_estadisticas(self):
        """
        Retorna las estadísticas actuales del jugador.
        
        Returns:
            dict: Diccionario con todas las estadísticas
        """
        porcentaje_acierto = 0
        if self.intentos_totales > 0:
            porcentaje_acierto = (self.intentos_correctos / self.intentos_totales) * 100
            
        return {
            'nivel': self.nivel_actual,
            'puntuacion': self.puntuacion,
            'intentos_totales': self.intentos_totales,
            'intentos_correctos': self.intentos_correctos,
            'porcentaje_acierto': porcentaje_acierto,
            'racha_actual': self.racha_actual,
            'mejor_racha': self.mejor_racha
        }
    
    def mostrar_estadisticas(self):
        """Muestra las estadísticas formateadas en pantalla."""
        stats = self.obtener_estadisticas()
        print("\n" + "="*50)
        print("📊 ESTADÍSTICAS DE LA ACADEMIA CYBERSECURE")
        print("="*50)
        print(f"🎖️  Nivel Actual: {stats['nivel']}")
        print(f"🏆 Puntuación: {stats['puntuacion']} puntos")
        print(f"📈 Intentos Totales: {stats['intentos_totales']}")
        print(f"✅ Intentos Correctos: {stats['intentos_correctos']}")
        print(f"📊 Porcentaje de Acierto: {stats['porcentaje_acierto']:.1f}%")
        print(f"🔥 Racha Actual: {stats['racha_actual']}")
        print(f"⭐ Mejor Racha: {stats['mejor_racha']}")
        print("="*50)
    
    def validar_respuesta(self, codigo_original, base_original, respuesta_usuario):
        """
        Valida si la respuesta del usuario es correcta.
        
        Args:
            codigo_original (str): El código mostrado al usuario
            base_original (str): La base del código ('binario', 'octal', 'hexadecimal')
            respuesta_usuario (int): La respuesta en decimal del usuario
        
        Returns:
            tuple: (es_correcto, valor_correcto, puntos_ganados)
        """
        # Calculamos el valor correcto según la base
        valor_correcto = 0
        
        if base_original == 'binario':
            valor_correcto = binario_a_decimal(codigo_original)
        elif base_original == 'octal':
            valor_correcto = octal_a_decimal(codigo_original)
        elif base_original == 'hexadecimal':
            valor_correcto = hexadecimal_a_decimal(codigo_original)
        
        # Verificamos si la respuesta es correcta
        es_correcto = (respuesta_usuario == valor_correcto)
        
        # Calculamos puntos ganados
        puntos_ganados = 0
        if es_correcto:
            # Puntos base según el nivel
            puntos_base = 10 * self.nivel_actual
            
            # Bonus por racha
            bonus_racha = min(self.racha_actual * 5, 50)  # Máximo 50 puntos de bonus
            
            # Bonus por dificultad (más puntos para hex > octal > binario)
            bonus_dificultad = {
                'binario': 0,
                'octal': 5,
                'hexadecimal': 10
            }
            
            puntos_ganados = puntos_base + bonus_racha + bonus_dificultad.get(base_original, 0)
        
        return es_correcto, valor_correcto, puntos_ganados
    
    def procesar_intento(self, codigo_original, base_original, respuesta_usuario):
        """
        Procesa un intento de descifrado y actualiza las estadísticas.
        
        Args:
            codigo_original (str): El código mostrado al usuario
            base_original (str): La base del código
            respuesta_usuario (int): La respuesta del usuario
        
        Returns:
            dict: Información sobre el resultado del intento
        """
        # Validamos la respuesta
        es_correcto, valor_correcto, puntos_ganados = self.validar_respuesta(
            codigo_original, base_original, respuesta_usuario
        )
        
        # Actualizamos estadísticas
        self.intentos_totales += 1
        
        if es_correcto:
            self.intentos_correctos += 1
            self.puntuacion += puntos_ganados
            self.racha_actual += 1
            
            # Actualizamos mejor racha si es necesario
            if self.racha_actual > self.mejor_racha:
                self.mejor_racha = self.racha_actual
            
            # Subimos de nivel cada 5 aciertos
            if self.intentos_correctos % 5 == 0:
                self.nivel_actual += 1
                mensaje_nivel = f"🎉 ¡FELICIDADES! Has subido al nivel {self.nivel_actual}"
            else:
                mensaje_nivel = None
        else:
            self.racha_actual = 0  # Reiniciamos la racha
            mensaje_nivel = None
        
        return {
            'es_correcto': es_correcto,
            'valor_correcto': valor_correcto,
            'puntos_ganados': puntos_ganados,
            'mensaje_nivel': mensaje_nivel
        }
    
    def ejecutar_desafio(self, codigo, base, tipo_sistema):
        """
        Ejecuta un desafío completo de descifrado.
        
        Args:
            codigo (str): El código a descifrar
            base (str): La base del código
            tipo_sistema (str): El tipo de sistema (firewall/servidor/memoria)
        """
        print("\n" + "="*60)
        print("🔐 DESAFÍO DE DESCIFRADO - ACADEMIA CYBERSECURE")
        print("="*60)
        print(f"📡 Sistema objetivo: {tipo_sistema.upper()}")
        print(f"🎯 Nivel actual: {self.nivel_actual}")
        print(f"🏆 Puntuación actual: {self.puntuacion} puntos")
        print("-"*60)
        
        # Mostramos el código a descifrar
        print(f"\n💻 Código interceptado en base {base}: {codigo}")
        print("\n⚡ ByteMaster te desafía a convertir este código a decimal")
        print("❓ ¿Cuál es el valor en decimal?")
        
        # Pedimos la respuesta con manejo de errores
        while True:
            try:
                respuesta = input("\n👉 Tu respuesta: ")
                respuesta_int = int(respuesta)
                break
            except ValueError:
                print("❌ Error: Debes ingresar un número entero válido")
        
        # Procesamos el intento
        resultado = self.procesar_intento(codigo, base, respuesta_int)
        
        # Mostramos el resultado
        print("\n" + "-"*60)
        if resultado['es_correcto']:
            print("✅ ¡CORRECTO! Has descifrado el código exitosamente")
            print(f"🎯 Puntos ganados: +{resultado['puntos_ganados']}")
            print(f"🔥 Racha actual: {self.racha_actual} aciertos consecutivos")
            
            if resultado['mensaje_nivel']:
                print("\n" + resultado['mensaje_nivel'])
        else:
            print("❌ INCORRECTO - Acceso denegado")
            print(f"💡 El valor correcto era: {resultado['valor_correcto']}")
            print(f"😔 Racha perdida. Tenías {self.racha_actual} aciertos")
        
        print("="*60)
        
        # Preguntamos si quiere ver estadísticas
        ver_stats = input("\n¿Deseas ver tus estadísticas? (s/n): ").lower()
        if ver_stats == 's':
            self.mostrar_estadisticas()
        
        return resultado['es_correcto']


# ============================================================================
# SECCIÓN 3: FUNCIONES AUXILIARES PARA VALIDACIÓN
# ============================================================================

def validar_entrada_menu(opciones_validas):
    """
    Valida que la entrada del usuario esté dentro de las opciones válidas.
    
    Args:
        opciones_validas (list): Lista de opciones válidas
    
    Returns:
        str: La opción validada
    """
    while True:
        opcion = input("\n👉 Ingresa tu opción: ").strip().lower()
        if opcion in opciones_validas:
            return opcion
        else:
            print(f"❌ Opción inválida. Las opciones válidas son: {', '.join(opciones_validas)}")


def limpiar_pantalla():
    """Simula limpiar la pantalla (imprime líneas en blanco)."""
    print("\n" * 2)


# ============================================================================
# SECCIÓN 4: FUNCIONES DE PRUEBA (TESTING)
# ============================================================================

def probar_conversiones():
    """
    Función de prueba para verificar que las conversiones funcionan correctamente.
    Incluye casos de prueba conocidos.
    """
    print("\n🧪 EJECUTANDO PRUEBAS DE CONVERSIÓN...")
    print("="*50)
    
    # Casos de prueba para binario a decimal
    pruebas_binario = [
        ("1010", 10),
        ("11111", 31),
        ("100000", 32),
        ("111111", 63),
        ("1", 1),
        ("0", 0)
    ]
    
    print("\n📌 Pruebas Binario → Decimal:")
    for binario, esperado in pruebas_binario:
        resultado = binario_a_decimal(binario)
        estado = "✅" if resultado == esperado else "❌"
        print(f"  {estado} {binario} → {resultado} (esperado: {esperado})")
    
    # Casos de prueba para octal a decimal
    pruebas_octal = [
        ("10", 8),
        ("77", 63),
        ("777", 511),
        ("1", 1),
        ("0", 0),
        ("144", 100)
    ]
    
    print("\n📌 Pruebas Octal → Decimal:")
    for octal, esperado in pruebas_octal:
        resultado = octal_a_decimal(octal)
        estado = "✅" if resultado == esperado else "❌"
        print(f"  {estado} {octal} → {resultado} (esperado: {esperado})")
    
    # Casos de prueba para hexadecimal a decimal
    pruebas_hex = [
        ("A", 10),
        ("F", 15),
        ("10", 16),
        ("FF", 255),
        ("FFF", 4095),
        ("2AF", 687),
        ("1", 1),
        ("0", 0)
    ]
    
    print("\n📌 Pruebas Hexadecimal → Decimal:")
    for hexa, esperado in pruebas_hex:
        resultado = hexadecimal_a_decimal(hexa)
        estado = "✅" if resultado == esperado else "❌"
        print(f"  {estado} {hexa} → {resultado} (esperado: {esperado})")
    
    print("\n✨ Pruebas completadas")
    print("="*50)


# ============================================================================
# EJEMPLO DE USO Y DEMOSTRACIÓN
# ============================================================================

if __name__ == "__main__":
    """
    Código de ejemplo para demostrar cómo usar las funciones.
    Este bloque solo se ejecuta si el archivo se ejecuta directamente,
    no cuando se importa como módulo.
    """
    
    print("="*60)
    print("🎮 DEMO - PARTE B: CONVERSIONES Y SISTEMA DE DESAFÍO")
    print("="*60)
    
    # Ejecutar pruebas automáticas
    opcion = input("\n¿Deseas ejecutar las pruebas automáticas? (s/n): ").lower()
    if opcion == 's':
        probar_conversiones()
    
    # Demo del sistema de desafío
    print("\n" + "="*60)
    print("🎯 DEMO DEL SISTEMA DE DESAFÍO")
    print("="*60)
    
    sistema = SistemaDesafio()
    
    # Simulamos algunos desafíos
    demos = [
        ("1011", "binario", "firewall"),
        ("157", "octal", "servidor"),
        ("2AF", "hexadecimal", "memoria")
    ]
    
    for codigo, base, tipo in demos:
        print(f"\n📋 Demo: Código {codigo} en base {base}")
        continuar = input("Presiona Enter para continuar con el desafío...")
        sistema.ejecutar_desafio(codigo, base, tipo)
        
        otra = input("\n¿Continuar con otro desafío? (s/n): ").lower()
        if otra != 's':
            break
    
    # Mostramos estadísticas finales
    print("\n🏁 SESIÓN FINALIZADA")
    sistema.mostrar_estadisticas()
    
    print("\n💡 Nota: Esta es la PARTE B del laboratorio.")
    print("   Recuerda integrarla con la PARTE A para completar el sistema.")