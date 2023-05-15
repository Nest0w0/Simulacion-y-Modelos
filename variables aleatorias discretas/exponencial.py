from math import e

def probabilidad_exponencial(num_ocurrencias, frecuencia):
	return (1 - (e**(- num_ocurrencias / frecuencia)))

def esperanza_exponencial(frecuencia):
	return 1/frecuencia

def varianza_exponencial(frecuencia):
	return 1/(frecuencia**2)

if __name__ == '__main__':
	num_ocurrencias_esperadas = 4
	frecuencia = 7
	res = probabilidad_exponencial(num_ocurrencias_esperadas,frecuencia)
	print("La probabilidad exponencial para {} eventos con una frecuencia de {} es: {}".format(num_ocurrencias_esperadas, frecuencia, res))
	res = esperanza_exponencial(frecuencia)
	print("La esperanza exponencial para una frecuencia de {} es: {}".format(frecuencia, res))
	res = varianza_exponencial(frecuencia)
	print("La varianza exponencial para una frecuencia de {} es: {}".format(frecuencia, res))