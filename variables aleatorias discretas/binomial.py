def factorial(n):
	if n == 1 or n == 0:
		return 1
	else:
		return n*factorial(n-1)

def combinacion(m,n):
	return factorial(m)/(factorial(m - n)*factorial(n))

def probabilidad_binomial(num_intentos, num_exitos, prob_exito):
	return combinacion(num_intentos, num_exitos)*(prob_exito**num_exitos)*((1 - prob_exito)**(num_intentos - num_exitos))

def esperanza_binomial(num_intentos, prob_exito):
	return num_intentos*prob_exito

def varianza_binomial(num_intentos, prob_exito):
	return num_intentos*prob_exito*(1 - prob_exito)

if __name__ == '__main__':
	num_intentos = 4
	num_exitos_esperados = 3
	prob = 0.8
	res = probabilidad_binomial(num_intentos, num_exitos_esperados, prob)
	print("La probabilidad binomial con {} intentos, {} exitos esperados y una probabilidad de exito de {} es: {}".format(num_intentos, num_exitos_esperados, prob, res))
	res = esperanza_binomial(4, 0.8)
	print("La esperanza binomial con {} intentos y una probabilidad de exito de {} es: {}".format(num_intentos, prob, res))
	res = varianza_binomial(4, 0.8)
	print("La varianza binomial con {} intentos y una probabilidad de exito de {} es: {}".format(num_intentos, prob, res))