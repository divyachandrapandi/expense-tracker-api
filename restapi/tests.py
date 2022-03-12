# from django.test import TestCase
from unittest import TestCase


# Create your tests here.
def sum_of_integers(a, b):
    return a + b


class Testsum(TestCase):
    def test_sum(self):
        self.assertEqual(sum_of_integers(3, 2), 5)
