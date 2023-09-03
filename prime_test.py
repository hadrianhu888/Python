import unittest
import math 
import prime 
from prime import *

class TestPrimeFunctions(unittest.TestCase):
    
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))
        
    def test_list_primes(self):
        self.assertEqual(list_primes(10), [2, 3, 5, 7])
        self.assertEqual(list_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(list_primes(0), [])
        self.assertEqual(list_primes(1), [])
        
    def test_print_next_prime(self):
        # We capture the stdout using the io.StringIO class
        from io import StringIO
        import sys
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        print_next_prime(3)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue().strip(), "5")

        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        print_next_prime(17)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue().strip(), "19")
        
if __name__ == '__main__':
    unittest.main()
