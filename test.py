import unittest
from descriptiva import *

class TesterDescriptiva(unittest.TestCase):
	
	def testMedia(self):
		self.assertEqual(media([1,2,3]), 2)
		self.assertEqual(media([10, 25, 47, 96]), 44.5)

	def testModa(self):
		self.assertEqual(moda([2,2,4,4,4,4,6]), 4)
		self.assertEqual(moda([1,1,1,9,9,9,9]), 9)

	def testMediana(self):
		self.assertEqual(mediana([1,3,5]), 3)
		self.assertEqual(mediana([1,5,6,10]), 5.5)

	def testRango(self):
		self.assertEqual(rango([0,1,9,28,13]), 28)
		self.assertEqual(rango([10,11,12,13,15]), 5)

	def testVarianza(self):
		self.assertEqual(varianza([5,10,17,21]), 50.916666666666664)
		self.assertEqual(varianza([14,15,15,15,15,15,15,16,21]), 4.25)

	def testDesviacion(self):
		self.assertEqual(desviacion([5,10,17,21]), 7.135591542869215)
		self.assertEqual(desviacion([14,15,15,15,15,15,15,16,21]), 2.0615528128088303)

if __name__ == '__main__':
	unittest.main()