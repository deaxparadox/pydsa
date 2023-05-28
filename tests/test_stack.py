from unittest import TestCase
import pytest
import threading

from pydsa.linear.stack import Stack


class StackTestCase(TestCase):
    def setUp(self):
        self.stack = Stack()
        self.__range = 10
        for i in range(self.__range):
            self.stack.append(i)
    
    def test_stack_removing_last_item(self):
        self.assertEqual(self.stack.pop(), self.__range - 1)

    def test_stack_15_item_not_in_stack(self):
        self.assert_(self.stack.remove(15), "item not found in stack")

    def test_stack_removing_1(self):
        self.assertEqual(self.stack.remove(1), None, "Removed 1")
    
    def test_stack_removing_all_items(self):
        for i in self.stack:
            self.stack.pop()

    