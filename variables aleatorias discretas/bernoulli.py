def probabilidad_bernoulli(exito,prob_exito):
	return (prob_exito**exito)*((1 - prob_exito)**(1 - exito))

def esperanza_bernoulli(prob_exito):
	return prob_exito

def varianza_bernoulli(prob_exito):
	return prob_exito*(1 - prob_exito)

if __name__ == '__main__':
	print(probabilidad_bernoulli(1, 0.3))
	print(esperanza_bernoulli(0.7))
	print(varianza_bernoulli(0.7))