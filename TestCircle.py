import unittest

from Circle import *

class TestCircle(unittest.TestCase):

   def test_area(self):
      circle_a=Circle(x=12.56, y=2, r=2)
       
      self.assertEqual(12.56, circle_a.test_area())
      
   def test_length(self):
      circle_a=Circle(x=12.56, y=2, r=2)
       
      self.assertEqual(circle_a.x, circle_a.length())  
         
if __name__=="__main__":
   unittest.main()

