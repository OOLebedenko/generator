import unittest
from iter_myrange import MyRange


class TestIntegrator(unittest.TestCase):

    def test_one_parameter(self):
        self.assertEqual(list(MyRange(4)), list(range(4)))
        self.assertEqual(list(MyRange(-4)), list(range(-4)))

    def test_two_parameters(self):
        self.assertEqual(list(MyRange(1, 3)), list(range(1, 3)))
        self.assertEqual(list(MyRange(-1, -3)), list(range(-1, -3)))
        self.assertEqual(list(MyRange(-3, -1)), list(range(-3, -1)))

    def test_three_parameters(self):
        self.assertEqual(list(MyRange(1, 5, 2)), list(range(1, 5, 2)))
        self.assertEqual(list(MyRange(-1, 5, 2)), list(range(-1, 5, 2)))
        self.assertEqual(list(MyRange(-1, -5, 2)), list(range(-1, -5, 2)))
        self.assertEqual(list(MyRange(-1, -5, -2)), list(range(-1, -5, -2)))
        self.assertEqual(list(MyRange(-1, 5, -2)), list(range(-1, 5, -2)))
        self.assertEqual(list(MyRange(1, -5, -2)), list(range(1, -5, -2)))

    def test_given_zero_step(self):
        self.assertRaises(ValueError, list, MyRange(1, -5, 0))

    def test_no_integer(self):
        with self.assertRaises(TypeError):
            MyRange("")

    def test_given_argument(self):
        with self.assertRaises(TypeError):
            MyRange()
        with self.assertRaises(TypeError):
            MyRange(1, 2, 3, 4)

