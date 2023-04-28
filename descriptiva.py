import csv
import stats

def media(lista_edades):
	return stats.mean(lista_edades)

def moda(lista_edades):
	return stats.mode(lista_edades)

def mediana(lista_edades):
	return stats.median(lista_edades)

def rango(lista_edades):
	return abs(max(lista_edades) - min(lista_edades))

def varianza(lista_edades):
	return stats.variance(lista_edades)

def desviacion(lista_edades):
	return stats.stdev(lista_edades)

if __name__ == "__main__":
	lista_edades = []
	
	with open('edades.csv') as csv_file:
		reader = csv.DictReader(csv_file)
		for row in reader:
			lista_edades.append(int(row.get('edades')))

	
	print('La media de los datos es: {}'.format(media(lista_edades)))
	print('La moda de los datos es: {}'.format(moda(lista_edades)))
	print('La mediana de los datos es: {}'.format(mediana(lista_edades)))
	print('El rango de los datos es: {}'.format(rango(lista_edades)))
	print('La varianza de los datos es: {}'.format(varianza(lista_edades)))
	print('La desviación de los datos es: {}'.format(desviacion(lista_edades)))