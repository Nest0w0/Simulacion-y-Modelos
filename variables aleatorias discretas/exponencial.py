from math import e

def probabilidad_exponencial(num_ocurrencias, frecuencia):
	return (1 - (e**(- num_ocurrencias / frecuencia)))

def esperanza_exponencial(frecuencia):
	return 1/frecuencia

def varianza_exponencial(frecuencia):
	return 1/(frecuencia**2)

if __name__ == '__main__':
	print(probabilidad_exponencial(4,7))
	print(esperanza_exponencial(7))
	print(varianza_exponencial(7))