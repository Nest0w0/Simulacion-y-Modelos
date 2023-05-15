from math import e

def factorial(n):
	if n == 1 or n == 0:
		return 1
	else:
		return n*factorial(n-1)

def probabilidad_poisson(num_ocurrencias, frecuencia):
	return ((e**(-frecuencia))*(frecuencia**(num_ocurrencias)))/(factorial(num_ocurrencias))

def esperanza_poisson(frecuencia):
	return frecuencia

def varianza_poisson(frecuencia):
	return frecuencia


if __name__ == '__main__':
	num_ocurrencias_esperadas = 6
	frecuencia = 5
	res = probabilidad_poisson(num_ocurrencias_esperadas,frecuencia)
	print("La probabilidad de Poisson para la ocurrencia de {} eventos cuando normalmente ocurren {} es: {}".format(num_ocurrencias_esperadas, frecuencia, res))
	res = esperanza_poisson(frecuencia)
	print("La esperanza de Poisson para eventos con ocurrencia {} es: {}".format(frecuencia, res))
	res = varianza_poisson(frecuencia)
	print("La varianza de Poisson para eventos con ocurrencia {} es: {}".format(frecuencia, res))