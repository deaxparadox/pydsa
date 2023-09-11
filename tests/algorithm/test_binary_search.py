from unittest import TestCase
import pytest
import random


from pydsa.algorithm import binary_search

def simple_array():
    return [1, 2, 3, 4, 5]

def generate_array_random():
    return [random.randint(1, 100) for _ in range(10)]


class TestBinarySearch(TestCase):
    def test_return_index(self):
        """
        binary serach algorithm search for element 
        and return the index.
        """

        array = simple_array()
        self.assertEqual(binary_search(3, array), 2)
    
    def test_return_none_empty_array(self):
        """
        binary serach algorithm search empty element
        """

        with pytest.raises(Exception):
            array = []
            self.assertEqual(binary_search(3, array), None)

    def test_return_none_element_not_in_array(self):
        """
        binary serach algorithm search for element, not 
        in array
        """

    def test_search_element_from_start(self):
        """
        binary search algorithm search for element, 
        from the starting
        """

        array = simple_array()
        self.assertEqual(binary_search(1, array), 0)

    
    def test_search_element_from_end(self):
        """
        binary search algorithm search for element, 
        from the starting
        """

        array = simple_array()
        self.assertEqual(binary_search(5, array), 4)