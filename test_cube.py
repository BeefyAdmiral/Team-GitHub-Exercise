import unittest
import cubic

class TestCubic(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(cubic.multiplication(20, 5), 100)
        self.assertEqual(cubic.multiplication(-2, 1),-2)
        self.assertEqual(cubic.multiplication(-1,-3), 3)
        
if __name__ == '__main__':
    unittest.main()