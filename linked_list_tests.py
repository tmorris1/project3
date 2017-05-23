import unittest

from linked_list import *


def less_than(thing1, thing2):
    return thing1 < thing2


def less_than(v1, v2):
    return v1 < v2
class TestList(unittest.TestCase):
     #Note that this test doesn't assert anything! It just verifies your
      #class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

class TestCase(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(empty_list(), None)
    def test_add(self):
        self.assertEqual(add(None, 0, 1), Pair(1, None))
        self.assertEqual(add(Pair("s1", None), 0 ,0), Pair(0, Pair("s1", None)))
        self.assertEqual(add(Pair(1, Pair(2, None)), 0, 0), Pair(0, Pair(1, Pair(2, None))))
        self.assertEqual(add(Pair(1, Pair(2, None)), 1, "dog"), Pair(1, Pair("dog", Pair(2, None))))
        self.assertEqual(add(Pair(2, Pair(7, None)), 2, 4), Pair(2, Pair(7, Pair(4, None))))
        self.assertRaises(IndexError, add, Pair(1, None), 4, 0)
        self.assertRaises(IndexError, add, Pair(1, None), -1, 2)
    def test_length(self):
        self.assertEqual(length(None), 0)
        self.assertEqual(length(Pair(2, Pair(7, None))), 2)
    def test_get(self):
        self.assertEqual(get(Pair(1, Pair(2, None)), 1), 2)
        self.assertEqual(get(Pair(1, Pair(2, None)), 0), 1)
        self.assertEqual(get(Pair(1, Pair(2, Pair(3, None))), 1), 2)
        self.assertRaises(IndexError, get, None, 0)
        self.assertRaises(IndexError, get, Pair(1, None), -1)
        self.assertRaises(IndexError, get, Pair(1, Pair(2, None)), 3)
    def test_set(self):
        self.assertEqual(set(Pair(1, None), 0, 2), Pair(2, None))
        self.assertEqual(set(Pair(1, Pair(2, None)), 1, 4), Pair(1, Pair(4, None)))
        self.assertEqual(set(Pair(1, Pair(2, Pair(3, None))), 1, 7), Pair(1, Pair(7, Pair(3, None))))
        self.assertRaises(IndexError, set, None, 0, 0)
        self.assertRaises(IndexError, set, Pair(1, None), -1, 12)
        self.assertRaises(IndexError, set, Pair(1, Pair(2, None)), 3, 4)
    def test_helper_remove(self):
        self.assertEqual(helper_remove(Pair(1, None), 0), None)
        self.assertEqual(helper_remove(Pair(1, Pair(2, None)), 1), Pair(1, None))
        self.assertEqual(helper_remove(Pair(1, Pair(2, Pair(3, None))), 1), Pair(1, Pair(3, None)))
        self.assertRaises(IndexError, helper_remove, None, 0)
        self.assertRaises(IndexError, helper_remove, Pair(1, None), 1)
        self.assertRaises(IndexError, helper_remove, Pair(1, None), -1)
    def test_remove(self):
        self.assertEqual(remove(Pair(1, None), 0), (1, None))
        self.assertEqual(remove(Pair(1, Pair(2, None)), 1), (2, Pair(1, None)))
        self.assertEqual(remove(Pair(1, Pair(2, Pair(3, None))), 1), (2, Pair(1, Pair(3, None))))
        self.assertRaises(IndexError, remove, None, 0)
        self.assertRaises(IndexError, remove, Pair(1, None), 1)
        self.assertRaises(IndexError, remove, Pair(1, None), -1)
    def test_insert_sorted(self):
        self.assertEqual(insert_sorted(Pair(0, Pair(2, Pair(4, Pair(5, None)))), 1, less_than), Pair(0, Pair(1, Pair(2, Pair(4, Pair(5, None))))))
        self.assertEqual(insert_sorted(None, 1, less_than), Pair(1, None))
        self.assertEqual(insert_sorted(Pair(1, Pair(2, Pair(3, None))), 0, less_than), Pair(0, Pair(1, Pair(2, Pair(3, None)))))
        self.assertEqual(insert_sorted(Pair(0, Pair(1, Pair(2, None))), 7, less_than), Pair(0, Pair(1, Pair(2, Pair(7, None)))))





if __name__ == "__main__":
    unittest.main()