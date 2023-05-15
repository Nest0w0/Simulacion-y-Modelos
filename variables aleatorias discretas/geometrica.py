def probabilidad_geometrica(num_primer_exito, prob_exito):
	return ((1 - prob_exito)**(num_primer_exito - 1))*prob_exito

def esperanza_geometrica(prob_exito):
	return 1/prob_exito

def varianza_geometrica(prob_exito):
	return (1 - prob_exito)/(prob_exito**2)

if __name__ == '__main__':
	num_primer_exito = 3
	prob = 0.5
	res = probabilidad_geometrica(num_primer_exito,prob)
	print("La probabilidad geométrica para el primer éxito en el intento n°{} y con probabilidad de exito {} es: {}".format(num_primer_exito, prob, res))
	res = esperanza_geometrica(prob)
	print("La esperanza geométrica para una probabilidad de éxito {} es: {}".format(prob, res))
	res = varianza_geometrica(prob)
	print("La varianza geométrica para una probabilidad de exito {} es: {}".format(prob, res))