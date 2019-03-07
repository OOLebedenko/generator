import unittest
from generator_myrange import myrange


class TestGenerator(unittest.TestCase):

    def test_one_parameter(self):
        self.assertEqual(list(myrange(4)), list(range(4)))
        self.assertEqual(list(myrange(-4)), list(range(-4)))

    def test_two_parameters(self):
        self.assertEqual(list(myrange(1, 3)), list(range(1, 3)))
        self.assertEqual(list(myrange(-1, -3)), list(range(-1, -3)))
        self.assertEqual(list(myrange(-3, -1)), list(range(-3, -1)))

    def test_three_parameters(self):
        self.assertEqual(list(myrange(1, 5, 2)), list(range(1, 5, 2)))
        self.assertEqual(list(myrange(-1, 5, 2)), list(range(-1, 5, 2)))
        self.assertEqual(list(myrange(-1, -5, 2)), list(range(-1, -5, 2)))
        self.assertEqual(list(myrange(-1, -5, -2)), list(range(-1, -5, -2)))
        self.assertEqual(list(myrange(-1, 5, -2)), list(range(-1, 5, -2)))
        self.assertEqual(list(myrange(1, -5, -2)), list(range(1, -5, -2)))

    def test_given_zero_step(self):
        self.assertRaises(ValueError, list, myrange(1, -5, 0))

    def test_no_integer(self):
        self.assertRaises(TypeError, myrange(""))

    def test_given_argument(self):
        self.assertRaises(TypeError, myrange())
        self.assertRaises(TypeError, myrange(1, 2, 3, 4))
