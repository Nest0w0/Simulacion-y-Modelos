def probabilidad_bernoulli(exito,prob_exito):
	return (prob_exito**exito)*((1 - prob_exito)**(1 - exito))

def esperanza_bernoulli(prob_exito):
	return prob_exito

def varianza_bernoulli(prob_exito):
	return prob_exito*(1 - prob_exito)

if __name__ == '__main__':
	prob = 0.7
	exito = 1
	res = probabilidad_bernoulli(exit, prob)
	print("La probabilidad de bernoulli con exito en {} y probabilidad de exito en {} es: {}".format(prob,exito,res))
	res = esperanza_bernoulli(prob)
	print("La esperanza de bernoulli con probabilidad de exito {} es {}".format(prob, res))
	res = varianza_bernoulli(prob)
	print("La varianza de bernoulli con probabilidad de exito {} es {}".format(prob, res))