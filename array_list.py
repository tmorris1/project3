# a List is one of
# - None
# - List(array, total_capacity, empty_spaces)
class List:
    def __init__(self, array, total_capacity, empty_spaces):
        self.array = array # a python list
        self.total_capacity = total_capacity # an int representing the total number of spaces in the array
        self.empty_spaces = empty_spaces # an int representing the number of empty spaces in the array

    def __eq__(self, other):
        return ((type(other) == List)
          and self.array == other.array
          and self.total_capacity == other.total_capacity
          and self.empty_spaces == other.empty_spaces
        )

    def __repr__(self):
        return ("List({!r}, {!r}, {!r})".format(self.array, self.total_capacity, self.empty_spaces))


# None -> None
# returns None
def empty_list():
    return None


# List value int -> List
# takes in a List, a value of any type, and an int representing an index, and adds the value into the array of the List at the given index
def add(lst, index, value):
    if  (lst == None and index != 0) or (lst != None and index > lst.total_capacity) or index < 0:
        raise IndexError
    elif lst == None:
        return List([value], 1, 0)

    length = lst.total_capacity
    empty_spaces = lst. empty_spaces
    if lst.empty_spaces - 1 < 0:
        new_array = [None] * (lst.total_capacity * 2)
        length = lst.total_capacity * 2
        empty_spaces = lst.empty_spaces + lst.total_capacity
    else:
        new_array = [None] * lst.total_capacity

    current_index = 0
    for val in lst.array:
        if current_index < index:
            new_array[current_index] = lst.array[current_index]
            current_index += 1
        elif current_index == index:
            new_array[index] = value
            if current_index + 1 < length:
                new_array[current_index + 1] = lst.array[current_index]
                current_index += 1
        else:
            if current_index + 1 < length:
                new_array[current_index + 1] = lst.array[current_index]
            current_index += 1
    if index == lst.total_capacity - lst.empty_spaces:
        new_array[index] = value
    empty_spaces -= 1

    return List(new_array, length, empty_spaces)




# List -> int
# takes in a List and returns the number of values in the array
def length(lst):
    if lst == None:
        return 0
    else:
        return lst.total_capacity - lst.empty_spaces

# List int -> value
# takes in a List and an int representing an index and returns the value at the given index
def get(lst, index):
    if lst == None or index < 0 or index > (lst.total_capacity - lst.empty_spaces - 1):
        raise IndexError
    else:
        return lst.array[index]

# List int val -> List
# takes in a List, an int representing an index, and any value, and returns the List with the value at the given index
def set(lst, index, value):
    if lst == None or index < 0 or (lst != None and index >= (lst.total_capacity- lst.empty_spaces)):
        raise IndexError
    new_array = [None] * lst.total_capacity
    current_index = 0
    for val in lst.array:
        if current_index == index:
            new_array[index] = value
        else:
            new_array[current_index] = lst.array[current_index]
        current_index += 1
    return List(new_array, lst.total_capacity, lst.empty_spaces)


# List int -> tuples
# takes in a List and an int representing an index and removes the value in the list at the given index, then returns a tuple containing the removed value and the new List
def remove(lst, index):
    if index < 0 or (lst != None and (index > (lst.total_capacity - lst.empty_spaces - 1))) or lst == None:
        raise IndexError
    else:
        new_array = [None] * (lst.total_capacity -1)
        current_index = 0
        for val in lst.array:
            if index == current_index:
                current_index += 1
            elif index < current_index:
                new_array[current_index - 1] = lst.array[current_index]
                current_index += 1
            else:
                new_array[current_index] = lst.array[current_index]
                current_index += 1
    return (lst.array[index], List(new_array, lst.total_capacity - 1, lst.empty_spaces))