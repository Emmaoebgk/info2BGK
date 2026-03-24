import unittest
from informatika2.sajat import is_prime


class IsPrime(unittest.TestCase):
    def test_is_prime_if_called_with_str(self):
        self.assertIsNone (is_prime("asd"))




if __name__ == '__main__':
    unittest.main()
