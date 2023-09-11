from unittest import TestCase
import pytest
import random


from pydsa.algorithm import linear_serach

def simple_array():
    return [1, 2, 3, 4, 5]

def generate_array_random():
    return [random.randint(1, 100) for _ in range(10)]


class TestLinearSearch(TestCase):
    def test_return_index(self):
        """
        linear serach algorithm search for element 
        and return the index.
        """

        array = simple_array()
        self.assertEqual(linear_serach(3, array), 2)
    
    def test_return_none_empty_array(self):
        """
        linear serach algorithm search empty element
        """

        with pytest.raises(Exception):
            array = []
            self.assertEqual(linear_serach(3, array), None)

    def test_return_none_element_not_in_array(self):
        """
        linear serach algorithm search for element, not 
        in array
        """

        array = simple_array()
        self.assertEqual(linear_serach(7, array), None)