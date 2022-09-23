import unittest
import cubic

class TestCubic(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(cubic.cube(2), 8)
        self.assertEqual(cubic.cube(-2),-8)

if __name__ == '__main__':
    unittest.main()