def probabilidad_geometrica(num_primer_exito, prob_exito):
	return ((1 - prob_exito)**(num_primer_exito - 1))*prob_exito

def esperanza_geometrica(prob_exito):
	return 1/prob_exito

def varianza_geometrica(prob_exito):
	return (1 - prob_exito)/(prob_exito**2)

if __name__ == '__main__':
	print(probabilidad_geometrica(3,0.5))
	print(esperanza_geometrica(0.8))
	print(varianza_geometrica(0.8))