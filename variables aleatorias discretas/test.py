import unittest
from bernoulli import *
from binomial import *
from geometrica import *
from poisson import *
from exponencial import *

class TesterVariablesDiscretas(unittest.TestCase):

	def testBernoulli(self):
		self.assertEqual(probabilidad_bernoulli(1,0.7), 0.7)
		self.assertEqual(esperanza_bernoulli(0.7), 0.7)
		self.assertEqual(varianza_bernoulli(0.7), 0.21000000000000002)

	def testBinomial(self):
		self.assertEqual(probabilidad_binomial(4, 3, 0.8), 0.4096)
		self.assertEqual(esperanza_binomial(4, 0.8), 3.2)
		self.assertEqual(varianza_binomial(4, 0.8), 0.6399999999999999)

	def testGeometrica(self):
		self.assertEqual(probabilidad_geometrica(3, 0.5), 0.125)
		self.assertEqual(esperanza_geometrica(0.5), 2.0)
		self.assertEqual(varianza_geometrica(0.5), 2.0)

	def testPoisson(self):
		self.assertEqual(probabilidad_poisson(6,5), 0.14622280813987562)
		self.assertEqual(esperanza_poisson(5), 5)
		self.assertEqual(varianza_poisson(5), 5)

	def testExponencial(self):
		self.assertEqual(probabilidad_exponencial(4,7), 0.4352818779922407)
		self.assertEqual(esperanza_exponencial(7), 0.14285714285714285)
		self.assertEqual(varianza_exponencial(7), 0.02040816326530612)

if __name__ == '__main__':
	unittest.main()