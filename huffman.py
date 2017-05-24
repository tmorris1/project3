import array_list
import linked_list
from huffman_bits_io import *
import sys
# string -> List
# takes in a string representing a file name and returns a List of the number of occurences of each character
def count(filename):
    my_file = open(filename, "r")
    l = array_list.List([0] * 256, 256, 0)
    for line in my_file:
        for char in line:
            l.array[ord(char)] += 1
    return l


# a HuffmanTree is one of:
# - Node(char, count, left, right)
# - Leaf(char, count)
class Node:
    def __init__(self, char, count, left, right):
        self.char = char # the character associated with the Node
        self.count = count # the number of occurences
        self.left = left # the left subtree
        self.right = right # the right subtree

    def __eq__(self, other):
        return ((type(other) == Node)
          and self.char == other.char
          and self.count == other.count
          and self.left == other.left
          and self.right == other.right
        )

    def __repr__(self):
        return ("Node({!r}, {!r}, {!r}, {!r})".format(self.char, self.count, self.left, self.right))

class Leaf:
    def __init__(self, char, count):
        self.char = char # the character in the leaf
        self.count = count # the number of occurences of the character

    def __eq__(self, other):
        return ((type(other) == Leaf)
          and self.char == other.char
          and self.count == other.count
        )

    def __repr__(self):
        return ("Leaf({!r}, {!r})".format(self.char, self.count))


# HuffmanTree -> string
# traverses the HuffmanTree in a pre-order traversal, and appends the character of each visited Leaf to a string
def tree_to_string(tree, s =""):
    if type(tree) == Leaf:
        s += chr(tree.char)
    else:
        s = tree_to_string(tree.left, s)
        s = tree_to_string(tree.right, s)
    return s


# HuffmanTree HuffmanTree -> boolean
# returns True if the first HuffmanTree comes before the second, False otherwise
def comes_before(t1, t2):
    if t1.count != t2.count:
        return t1.count < t2.count
    else:
        return t1.char < t2.char

# AnyList -> HuffmanTree
# takes in an AnyList of sorted Leaves and builds a HuffmanTree
def build_tree(leaves):
    if linked_list.length(leaves) > 1:
        new_node = merge(leaves.first, leaves.rest.first)
        leaves = linked_list.remove(leaves, 0)[1]
        leaves = linked_list.remove(leaves, 0)[1]
        leaves = linked_list.insert_sorted(leaves, new_node, comes_before)
        return build_tree(leaves)
    else:
        return leaves.first


# List -> AnyList
# takes in an array of character occurences, and returns a sorted linked list of the list values as Leaves
def sorted_leaves(l):
    new = None
    index = 0
    for val in l.array:
        if val != 0:
            new = linked_list.insert_sorted(new, Leaf(index, val), comes_before)
        index += 1
    return new

# HuffmanTree HuffmanTree -> HuffmanTree
# takes in two HuffmanTrees and returns them merged
def merge(t1, t2):
    total = t1.count + t2.count
    if t1.char < t2.char:
        char = t1.char
    else:
        char = t2.char
    if comes_before(t1, t2):
        return Node(char, total, t1, t2)
    else:
        return Node(char, total, t2, t1)

# HuffmanTree -> List
# takes in a HuffmanTree and returns a List of the corresponding character codes
def character_codes(t, s = "", l = array_list.List([None] * 256, 256, 0)):
    if type(t) == Leaf:
        l.array[t.char] = s
    else:
        character_codes(t.left, s + "0", l)
        character_codes(t.right, s + "1", l)
    return l

# string string -> string
# takes in a string representing the name of the input file and a string representing the name of an output file, and writes the text from the input file to the output file using Huffman encoding
def huffman_encode(in_file, out_file):
    try:
        my_in = open(in_file, "r")
    except FileNotFoundError:
        print("File not found.")
        return
    hb_writer = HuffmanBitsWriter(out_file)
    s = ""
    counted = count(in_file)
    leaves = sorted_leaves(counted)
    if leaves != None:
        tree = build_tree(leaves)
        chars = tree_to_string(tree)
        hb_writer.write_byte(len(chars))
        code = character_codes(tree).array
        for i in range(0, array_list.length(counted)):
            if counted.array[i] > 0:
                hb_writer.write_byte(i)
                hb_writer.write_int(counted.array[i])
        for line in my_in:
            for char in line:
                s += code[ord(char)]
        hb_writer.write_code(s)
    hb_writer.close()

# string string -> string
# takes in a string representing an input file of a Huffman encoding, a writes the decoded file to the file with the name of the second string
def huffman_decode(in_file, out_file):
    try:
        hb_reader = HuffmanBitsReader(in_file)
    except FileNotFoundError:
        print("File not found.")
        return
    out = open(out_file, "w")
    try:
        number_of_chars = hb_reader.read_byte()
    except struct.error:
        out.close()
        return
    counted = array_list.List([0] * 256, 256, 0)
    total_occurences = 0
    chars = ""
    encoded = ""
    decoded = ""
    for i in range(0, number_of_chars):
        char = hb_reader.read_byte()
        char_occurence = hb_reader.read_int()
        counted.array[char] = char_occurence
        total_occurences += char_occurence
        chars += chr(char)
    if number_of_chars == 1:
        decoded += chars * total_occurences
    else:
        leaves = sorted_leaves(counted)
        if leaves != None:
            tree = build_tree(leaves)
            code = character_codes(tree).array
            total_digits = total_ones_and_zeros(code, counted)
            for i in range(0, total_digits):
                bit = hb_reader.read_bit()
                if bit == True:
                    encoded += "1"
                else:
                    encoded += "0"
        decoded = decode(tree, encoded)
    out.write(decoded)
    out.close()

# array -> List
# counts the total number of ones and zeroes in the encoded file
def total_ones_and_zeros(code, counted):
    s = ""
    index = 0
    for val in counted.array:
        if val != 0:
            s += (code[index] * val)
        index += 1
    return(len(s))


# HuffmanTree string -> string
# decodes the string of ones and zeros
def decode(tree, encoded):
    decoded = ""
    temp_tree = tree
    for val in range(0, len(encoded) + 1):
        if type(temp_tree) == Leaf:
            decoded += chr(temp_tree.char)
            temp_tree = tree
        if val < len(encoded) and encoded[val] == "0":
            temp_tree = temp_tree.left
        elif val < len(encoded) and encoded[val] == "1":
            temp_tree = temp_tree.right
    return decoded








#huffman_encode("txt1", "out")
#huffman_encode("txt2", "out2")
#huffman_encode("txt3", "out3")
#huffman_encode("txt4", "out4")
#huffman_encode("txt5", "out5")
#huffman_decode("out", "out_1")
#huffman_decode("out2", "out2_1")
#huffman_decode("out3", "out3_1")
#huffman_decode("out4", "out4_1")
#huffman_decode("out5", "out5_1")
#huffman_decode("blah", "two")