from unittest import TestCase

from pydsa.linear.double import List

class Test_Double(TestCase):
    def setUp(self) -> None:
        self.list = List()

    def add_10(self) -> None:
        for i in range(10):
            self.list.append(i)

    def test_length(self) -> None:
        self.add_10()
        self.assertEqual(len(self.list), 10)
