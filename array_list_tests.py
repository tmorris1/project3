import unittest
from array_list import *

def less_than(thing1, thing2):
    return thing1 < thing2

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

    def test_empty_list(self):
        self.assertEqual(empty_list(), None)
    def test_add(self):
        self.assertEqual(add(None, 0, 1), List([1], 1, 0))
        self.assertEqual(add(List([1], 1, 0), 1, 4), List([1, 4], 2, 0))
        self.assertEqual(add(List([0, 1, 2], 3, 0), 2, 4), List([0, 1, 4, 2, None, None], 6, 2))
        self.assertEqual(add(List([0, 1, 2, None], 4, 1), 2, 7), List([0, 1, 7, 2], 4, 0))
        self.assertEqual(add(List([4, 3, 7, 4, None, None, None, None], 8, 4), 2, 10), List([4, 3, 10, 7, 4, None, None, None], 8, 3))
        self.assertRaises(IndexError, add, None, 1, 7)
        self.assertRaises(IndexError, add, List([1], 1, 0), -1, 9)
    def test_length(self):
        self.assertEqual(length(None), 0)
        self.assertEqual(length(List([1, None], 1, 0)), 1)
        self.assertEqual(length(List([1, 2, 3, 4, None, None, None], 7, 3)), 4)
    def test_get(self):
        self.assertEqual(get(List([1, None], 2, 1), 0), 1)
        self.assertEqual(get(List([2, 7, 3], 3, 0), 2), 3)
        self.assertRaises(IndexError, get, None, 0)
        self.assertRaises(IndexError, get, List([1, None], 2, 1), 2)
        self.assertRaises(IndexError, get, List([1, None, None, None, None], 5, 4), 2)
        self.assertRaises(IndexError, get, List([1, 2], 2, 0), -1)
    def test_set(self):
        self.assertEqual(set(List([1, None], 2, 0), 1, 2), List([1, 2], 2, 0))
        self.assertEqual(set(List([1, 2, 3, None], 4, 1), 2, 7), (List([1, 2, 7, None], 4, 1)))
        self.assertRaises(IndexError, set, None, 1, 3)
        self.assertRaises(IndexError, set, List([1, 2], 2, 0), 2, 2)
        self.assertRaises(IndexError, set, List([1, 2], 2, 0), -2, 9)
    def test_remove(self):
        self.assertEqual(remove(List([1, 2, 3], 3, 0), 1), (2, List([1, 3], 2, 0)))
        self.assertEqual(remove(List([1, 2, None], 3, 1), 0), (1, List([2, None], 2, 1)))
        self.assertEqual(remove(List([1, 2, 3], 3, 0), 2), (3, List([1, 2], 2, 0)))
        self.assertEqual(remove(List([0, 1, 2, 3, 4, 5, 6, 7, None, None], 10, 2), 4), (4, List([0, 1, 2, 3, 5, 6, 7, None, None], 9, 2)))
        self.assertRaises(IndexError, remove, None, 2)
        self.assertRaises(IndexError, remove, List([1, 2, 3], 3, 0), 3)
        self.assertRaises(IndexError, remove, List([1], 1, 0), -4)
    def test_repr(self):
        self.assertEqual(repr(List([1, 2, 3], 3, 0)), "List([1, 2, 3], 3, 0)")


if __name__ == "__main__":
    unittest.main()