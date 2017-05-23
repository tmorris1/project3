# an AnyList is one of:
# - None
# - Pair(first, rest)
class Pair:
    def __init__(self, first, rest):
        self.first = first # the first value in the Pair
        self.rest = rest # the rest of the Pair

    def __eq__(self, other):
        return ((type(other) == Pair)
          and self.first == other.first
          and self.rest == other.rest
        )

    def __repr__(self):
        return ("Pair({!r}, {!r})".format(self.first, self.rest))


# None -> AnyList
# takes no arguments and returns an empty list
def empty_list():
    return None


# AnyList int val -> AnyList
# inserts a value at a given index in a linked list
def add(anylist, index, val, current_index = 0):
    if (anylist == None and index != current_index) or index < 0:
        raise IndexError
    elif anylist == None:
        return Pair(val, None)
    elif 0 <= index:
        if index == current_index:
            return Pair(val, anylist)
        else:
            return Pair(anylist.first, add(anylist.rest, index, val, current_index + 1))



# AnyList -> int
# returns an int representing the number of elements in an AnyList
def length(anylist):
    if anylist == None:
        return 0
    else:
        return 1 + length(anylist.rest)


# AnyList int -> int
# takes in an AnyList and an index and returns the value in the list at the given index
def get(anylist, index, current_index = 0):
    if anylist == None or index < 0:
        raise IndexError
    else:
        if index == current_index:
            return anylist.first
        else:
            return get(anylist.rest, index, current_index + 1)


# AnyList int val -> int
# takes in an AnyList, an index and a value of any type and replaces the value in the AnyList at the given index with the given value
def set(anylist, index, value, current_index = 0):
    if anylist == None or index < 0:
        raise IndexError
    else:
        if index == current_index:
            return Pair(value, anylist.rest)
        else:
            return Pair(anylist.first, set(anylist.rest, index, value, current_index + 1))

# AnyList int int -> AnyList
# returns a lsit with the element at the given index removed
def helper_remove(anylist, index, current_index = 0):
    if index <0 or anylist == None:
        raise IndexError
    if index == current_index:
        return anylist.rest
    return Pair(anylist.first, helper_remove(anylist.rest, index , current_index + 1))

# AnyList int -> tuple
# takes in an Anylist and an index, removes the value in the AnyList at the given index, and returns a tuple containing the value that was removed and the new AnyList
def remove(anylist, index, current_index = 0):
    return (get(anylist, index), helper_remove(anylist, index))


# AnyList val -> AnyList
# takes in a sorted AnyList and a value and inserts the value in the appropriate position
def insert_sorted(l, val, comes_before):
    if l == None:
        return Pair(val, None)
    elif comes_before(val, l.first):
        return add(l, 0, val)
    else:
        return Pair(l.first, insert_sorted(l.rest, val, comes_before))
