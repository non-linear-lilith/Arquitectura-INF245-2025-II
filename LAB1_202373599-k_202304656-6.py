"""
Plantilla de trabajo en pareja para la Tarea 1.

Usa estas secciones para dividir el trabajo entre ROL1 y ROL2.
Rellena con funciones reales a medida que avancen.
"""

# ==========================
# ROL1 — Módulo A (Owner)
# Sugerido: Entrada/Salida y orquestación
# ==========================

def modulo_a_main(inputs):
	"""TODO(ROL1): Implementar la orquestación inicial.
	- Validar y parsear inputs
	- Llamar a funciones del módulo B cuando corresponda
	- Manejar errores y mensajes al usuario
	"""
	raise NotImplementedError("Pendiente implementación por ROL1")


# ==========================
# ROL2 — Módulo B (Owner)
# Sugerido: Lógica/algoritmo principal
# ==========================

def modulo_b_core(data):
	"""TODO(ROL2): Implementar la lógica principal.
	- Algoritmo base
	- Validaciones avanzadas y métricas
	- Retornar resultados estructurados
	"""
	raise NotImplementedError("Pendiente implementación por ROL2")


# ==========================
# Tests rápidos (ambos)
# Nota: Reemplazar por un framework de tests si el curso lo exige
# ==========================

def _self_check():
	"""Pequeña prueba de humo local (opcional).
	Ajustar o eliminar cuando haya tests formales.
	"""
	try:
		modulo_a_main({})
	except NotImplementedError:
		pass
	try:
		modulo_b_core({})
	except NotImplementedError:
		pass


if __name__ == "__main__":
	# Ejecuta chequeo de humo si se corre directamente
	_self_check()

