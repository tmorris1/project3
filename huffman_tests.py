import unittest
from huffman import *

class TestList(unittest.TestCase):
    def test_tree_to_string(self):
        self.assertEqual(tree_to_string(Leaf("b", 2)), "b")
        self.assertEqual(tree_to_string(Node("c", 3, Leaf("d", 1), Leaf("c", 2))), "dc")
        self.assertEqual(tree_to_string(Node(" ", 13, Node(" ", 6, Leaf(" ", 3), Leaf("b", 3)), Node("a", 7, Node("c", 3, Leaf("d", 1), Leaf("c", 2)), Leaf("a", 4)))), " bdca")
    def test_comes_before(self):
        self.assertEqual(comes_before(Node("c", 3, Leaf("d", 1), Leaf("c", 2)), Leaf("a", 4)), True)
        self.assertEqual(comes_before(Leaf("d", 1), Leaf("c", 2)), True)
        self.assertEqual(comes_before(Leaf("b", 3), Leaf(" ", 3)), False)
        self.assertEqual(comes_before(Node(" ", 6, Leaf(" ", 3), Leaf("b", 3)), Node("a", 7, Leaf("c", 3), Leaf("a", 4))), True)
    def test_build_tree(self):
        l1 = sorted_leaves(count("txt1"))
        self.assertEqual(build_tree(l1), Node(32, 13, Node(32, 6, Leaf(32, 3), Leaf(98, 3)), Node(97, 7, Node(99, 3, Leaf(100, 1), Leaf(99, 2)), Leaf(97, 4))))
    def test_sorted_leaves(self):
        l1 = count('txt1')
        l2 = count('txt2')
        self.assertEqual(sorted_leaves(l1), linked_list.Pair(Leaf(100, 1), linked_list.Pair(Leaf(99, 2), linked_list.Pair(Leaf(32, 3), linked_list.Pair(Leaf(98, 3), linked_list.Pair(Leaf(97, 4), None))))))
        self.assertEqual(sorted_leaves(l2), linked_list.Pair(Leaf(97, 1), linked_list.Pair(Leaf(98, 1), linked_list.Pair(Leaf(99, 1), linked_list.Pair(Leaf(10, 2), None)))))
    def test_make_nodes(self):
        self.assertEqual(merge(Node("c", 3, Leaf("d", 1), Leaf("c", 2)), Leaf("a", 4)), Node("a", 7, Node("c", 3, Leaf("d", 1), Leaf("c", 2)), Leaf("a", 4)))
        self.assertEqual(merge(Leaf("d", 1), Leaf("c", 2)), Node("c", 3, Leaf("d", 1), Leaf("c", 2)))
        self.assertEqual(merge(Leaf(" ", 3), Leaf("b", 3)), Node(" ", 6, Leaf(" ", 3), Leaf("b", 3)))
    def test_character_codes(self):
        l1 = array_list.List([None] * 256, 256, 0)
        l1.array[ord(" ")] = "00"
        l1.array[ord("b")] = "01"
        l1.array[ord("c")] = "101"
        l1.array[ord("d")] = "100"
        l1.array[ord('a')] = "11"
        self.assertEqual(character_codes(Node(32, 13, Node(32, 6, Leaf(32, 3), Leaf(98, 3)), Node(97, 7, Node(99, 3, Leaf(100, 1), Leaf(99, 2)), Leaf(97, 4)))), l1)
        self.assertEqual(build_tree(sorted_leaves(count("txt1"))),Node(32, 13, Node(32, 6, Leaf(32, 3), Leaf(98, 3)), Node(97, 7, Node(99, 3, Leaf(100, 1), Leaf(99, 2)), Leaf(97, 4))))



if __name__ == "__main__":
    unittest.main()