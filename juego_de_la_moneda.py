import random

def apostar(MONTO_INICIAL):
	if (random.randint(1,6)) % 2 == 0:
		return MONTO_INICIAL
	else:
		return -MONTO_INICIAL


def jugar(MONTO_INICIAL):
	dinero_actual = MONTO_INICIAL
	print("Dinero inicial antes de apostar: {}".format(dinero_actual))
	numero_apuestas = 1
	while dinero_actual > 0:
		dinero_actual += apostar(MONTO_INICIAL)
		print("Apuesta: {} || Dinero: {}".format(numero_apuestas, dinero_actual))
		numero_apuestas += 1

	return numero_apuestas

def simular(MONTO_INICIAL, CANTIDAD_DE_JUEGOS):
	resultados = []
	for i in range(1, CANTIDAD_DE_JUEGOS + 1):
		print("Simulación N°{}".format(i))
		resultados.append(jugar(MONTO_INICIAL))
		print()
		print("======================================================")
		print()

	return resultados

def promedio_estadistico(resultados, CANTIDAD_DE_JUEGOS):
	suma = 0
	for i in resultados:
		suma += i

	return suma/CANTIDAD_DE_JUEGOS

if __name__ == "__main__":
	MONTO_INICIAL = 100
	CANTIDAD_DE_JUEGOS = 100

	promedio = promedio_estadistico(simular(MONTO_INICIAL, CANTIDAD_DE_JUEGOS), CANTIDAD_DE_JUEGOS) 
	print("El promedio de turnos que tardaron los {} jugadores en quedarse sin dinero es: {}".format(CANTIDAD_DE_JUEGOS, promedio))
	print()


"""
Realizado por: Nestor Aguilar (C.I: 28.316.308)
Dado que el docente no redactó un enunciado formal del ejercicio, a continuación
presento el planteamiento:

Este juego de la moneda se basa en una apuesta que funciona de la siguiente
manera: un jugador apuesta una cantidad de dinero fija y se tira un dado,
si el resultado del dado es par le devuelven el doble de su dinero, pero si 
el resultado es impar, se queda sin el dinero que apostó. En cada intento,
nuestro ludópata apostará la misma cantidad, hasta que se quede sin dinero.

Este programa va a simular cuantos intentos les tomaría a N cantidad de 
jugadores quedarse sin dinero, y sacar un promedio estadístico para evaluar si
es un juego que vale la pena jugar.
"""