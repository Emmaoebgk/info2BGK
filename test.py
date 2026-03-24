import unittest
from informatika2.info2ora import adding, solve_equalison, solve_quadratic


class MyTestCase(unittest.TestCase):
    def test_adding_function(self):
        self.assertEqual(3, adding(num1= 1, num2=2)) # add assertion here

    def test_solve_equation(self):
        self.assertEqual(2,solve_equalison(2,-4))
        self.assertIsNone(solve_equalison(0,-4))

    def test_solve_quadratic(self):
        self.assertEqual((None,None),solve_quadratic(0,1,2))
        x1, x2 = solve_quadratic(1,2,1)
        self.assertEqual(-1,x1)
        self.assertIsNone(x2)
        x1, x2 = solve_quadratic(1,2,2)
        self.assertIsNone(x1)
        self.assertIsNone(x2)


        x1, x2 = solve_quadratic(1,4,1)





if __name__ == '__main__':
    unittest.main()
