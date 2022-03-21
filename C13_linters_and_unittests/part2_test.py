import unittest
from part2 import my_area_function, my_func


class TestMyAreaFunction(unittest.TestCase):

    def test_negative(self):
        self.assertRaises(ValueError, my_area_function, -2, 2)

    def test_square_area(self):
        self.assertEqual(my_area_function(2, 2), 4)

    def test_type(self):
        self.assertRaises(TypeError, my_area_function, 2, '2')

    def test_return_type(self):
        self.assertRaises(TypeError, my_area_function, 2, True)

    def test_example(self):
        self.assertEqual(my_func -2, 2, None)


if __name__ == '__main__':
    unittest.main()
