from django.test import SimpleTestCase

from app import calculator


class CalculatorTest(SimpleTestCase):

    def test_add_numbers(self):
        res = calculator.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = calculator.subtract(10, 15)
        self.assertEqual(res, -5)

    def test_subtract_numbers_in_postive(self):
        res = calculator.subtract(10, 6)
        self.assertEqual(res, 4)

    def test_subtract_numbers_in_0(self):
        res = calculator.subtract(0, 6)
        self.assertEqual(res, -6)
