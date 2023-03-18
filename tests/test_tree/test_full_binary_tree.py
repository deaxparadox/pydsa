import unittest
import pytest

from PyDSA.Tree.FullBinaryTree import (
    isFullTree as isFull,
    Node
) 


class TestTree(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Node(1)
        

    @pytest.mark.order(1)
    def test_root(self):
        self.assertEqual(isFull(self.root), True)

    @pytest.mark.order(2)
    def test_root_with_leftchild(self):
        self.root.leftChild = Node(3)
        self.assertEqual(
            isFull(self.root), False
        )

    @pytest.mark.order(3)
    def test_root_complete(self):
        self.root.leftChild = Node(3)
        self.root.rightChild = Node(2)
        self.assertEqual(
            isFull(self.root), True
        )

    def test_left_leftchild_(self):
        self.root.leftChild = Node(3)
        self.root.rightChild = Node(2)
        self.root.leftChild.leftChild = Node(4)

        self.assertEqual(
            isFull(self.root), False, "if test passed then, it acutally failed"
        )
