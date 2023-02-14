from unittest import TestCase
import pytest

from PyDSA.LinkedList.Stack import Stack


class StackTestCase(TestCase):
    def setUp(self):
        self.stack = Stack()
        self.__range = 10

    #
    #   INSERTING AND TESTING
    #   LENGTH AND EMPTY
    #

    def insert(self):
        # 9,8,7,6,5,4,3,2,1,0
        for i in range(0, self.__range):
            self.stack.append(i)
            
    def test_after_insert_length(self):
        self.insert()
        assert len(self.stack) == self.__range

    def test_after_insert_remove_5(self):
        self.insert()
        assert self.stack.remove(5) == None
    
    def test_after_insert_remove_15(self):
        self.insert()
        
        try:
            self.stack.remove(15)
        except:
            assert True 
    
    def test_after_insert_empty(self):
        self.insert()
        assert self.stack.is_empty() == False


    def test_case_1(self):
        self.insert()
        assert 10 == len(self.stack)

        # first last item
        data = self.stack.pop() 
        assert data == 9
        assert 9 == len(self.stack)


    def test_case_2(self):
        self.insert()
        with Stack() as q:
            for i in range(self.__range):
                q.append(i)
            
            assert len(q) == len(self.stack)
            assert q == self.stack
            assert q.pop() == self.stack.pop()

    def test_case_3(self):
        self.stack.append(1)
        assert len(self.stack) == 1
        self.stack.remove(1)
        assert len(self.stack) == 0
        self.stack.append(11)
        self.stack.remove(1)

    def test_set_and_get_item(self):
        self.insert()
        assert self.stack[0] == 9
        self.stack[0] = "Nitish"
        assert self.stack[0] == "Nitish"




    #
    #   REMOVING ALL ELEMENT AND TESTING
    #   LENGTH AND EMPTY
    #   
    def remove_all(self):
        self.insert()
        for i in self.stack:
            # self.stack.pop()
            self.stack.remove(i)

    
    def test_after_remove_length(self):
        self.remove_all()
        assert len(self.stack) == 0
    
    def test_after_remove_empty(self):
        self.remove_all()
        assert self.stack.is_empty() == True
    
    

    def test_empty_stack_exception(self):
        self.remove_all()
        try:
            self.stack.pop()
        except:
            assert True
