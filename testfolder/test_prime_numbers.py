import unittest
from primenumbers import primeNumbers
import sys


class TestPrimeNumbers(unittest.TestCase):
    def test_answer(self):
        """test if the list produced is correct"""
        self.assertEqual(primeNumbers(9),[1, 2, 3, 5, 7])
    
    def test_IsInteger(self):
        """test is argument provided by user is an int"""
        with self.assertRaises(TypeError):
            primeNumbers([])
            
    def test_notNegative(self):
        """makes sure user does not give out negative urgument"""
        with self.assertRaises(TypeError):
            primeNumbers(-1)
            
    def test_ZeroIsNotPrime(self):
        """makes sure that Zero is not counted as a prime number"""
        self.assertListEqual(primeNumbers(0),[],"Zero should not be a primenumber")
       
    def test_Nincluded(self):
        """checks that if the number n is a prime number its included in the list"""
        self.assertNotEqual(primeNumbers(7),[1, 2, 3, 5],"If N is prime number it should be included in the list")
        
    def test_returnsList(self):
        """asserts that the result returned is a list"""
        self.assertIsInstance(primeNumbers(1),list,"The result of the function should be a list")
    def test_floatNotAllowed(self):
        """Makes sure that floats are not  accepted"""
        with self.assertRaises(TypeError):
            primeNumbers(7.7)           
        
    def test_hasPrimeOnly(self):
        """make sure that only prime numbers are in the list"""
        self.assertNotIn(4,primeNumbers(10), msg="this are not prime numbers")
        
    def test_oneIsPrime(self):
        """test that one is a prime number"""
        self.assertIn(1,primeNumbers(3))
    
    """"@unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(primeNumbers(7),[1, 2, 3, 5])  """
    
    @unittest.skipIf(sys.platform.startswith("win"), "requires Windows")    
    def test_windows(self):
        """runs only when user is not on windows"""
        self.assertIn(1,primeNumbers(3))
        
    def test_ListCount(self):
        """"counts number of item in list returned"""
        self.assertItemsEqual(primeNumbers(9),[1, 2, 3, 5, 7])
    
       
        
if __name__ == '__main__':
    unittest.main() 