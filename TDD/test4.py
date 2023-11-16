import unittest

class TestAdd(unittest.TestCase):
    def test_add(self):
        print(dir(self))
        
        self.assertEqual(1 + 2, 3)
        self.assertTrue(10 == 10)
        self.assertFalse(1 == 10)
        self.assertGreater(10, 1)
        self.assertLess(1, 10)
        self.assertIn(1, [1, 2, 3, 4, 5])
        self.assertIsInstance('a', str)


if __name__ == '__main__':
    unittest.main()