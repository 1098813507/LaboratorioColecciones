import unittest
import statistics
from custom_functions import temperature_methods

class test_1(unittest.TestCase):

   def test_calcular_promedio(self):
       santander=[30,29,27,28,24,19,20,24,23,22,21,20]
       promedio=temperature_methods.promedio_temperature(santander)
       self.assertEqual(promedio,268.6)

   def test_mejor_temperatura(self):
       departamento_1=[30,29,27,28,24,19,20,24,23,22,21,20]
       cal_1=temperature_methods.temperature_best(departamento_1)
       self.assertEqual(cal_1,30)

   def test_desviacion_estandar(self):
       departamento_2=[30,29,27,28,24,19,20,24,23,22,21,20]
       s=statistics.stdev(departamento_2)
       self.assertEqual(s,3.6161289922912)


if __name__ == '__main__':
   unittest.main()
