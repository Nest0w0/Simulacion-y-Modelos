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
	print(probabilidad_poisson(6,5))
	print(esperanza_poisson(5))
	print(varianza_poisson(5))