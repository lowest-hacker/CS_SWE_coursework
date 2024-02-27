# Name: Casey Lowe
# OSU Email: lowecas@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment #3
# Due Date: November 7th, 2023
# Description: Implementing a Singly Linked List datastructure by implementing the following methods:
# insert_front(), insert_back(), insert_at_index(), remove_at_index(), remove(), count(), find(), slice()
# Each of these methods are implemented with the use of a front sentinel node.


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        This method adds a new node at the beginning of the list (right after the front sentinel).
        """
        # create a new node
        new_node = SLNode(value)

        new_node.next = self._head.next
        # head node points to the new node
        self._head.next = new_node

    def insert_back(self, value: object) -> None:
        """
        This method adds a new node at the end of the list.
        """
        new_node = SLNode(value)
        # find the last node in the list
        node = self._head
        while node.next is not None:
            node = node.next
        # last node now points to the new node
        node.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a new value at the specified index position in the linked list while index 0 refers to
        the beginning of the list. Raise a custom "SLLException" if the provided index is invalid.
        """
        if index < 0 or index > self.length():
            raise SLLException
        previous_node = self._head
        count = 0
        while count != index:
            previous_node = previous_node.next
            count += 1
        new_node = SLNode(value)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def remove_at_index(self, index: int) -> None:
        """
        This method removes the node at the specified index position from the linked list.
        If the provided index is invalid, raises “SLLException”.
        """

        if index < 0 or index >= self.length():
            raise SLLException('Invalid index position')

        current = self._head
        prev = None

        for i in range(index + 1):
            prev = current
            current = current.next

        prev.next = current.next

    def remove(self, value: object) -> bool:
        """
        Traverse the list from the beginning to the end, and remove the first node that matches the
        provided value. Return True if a node is removed from the list and return False otherwise.
        """
        node = self._head
        next_node = self._head.next
        while node.next is not None:
            if node.next.value == value:
                node.next = next_node.next
                return True
            else:
                node = next_node
                next_node = next_node.next
        return False

    def count(self, value: object) -> int:
        """
        This method counts the number of elements in the list that match the provided value.
        Returns this number.
        """
        count = 0
        # Start from the first node
        current = self._head.next

        while current is not None:
            if current.value == value:
                count += 1
            current = current.next

        return count

    def find(self, value: object) -> bool:
        """
        Return a Boolean value based on whether or no the provided value exists in the list.
        """
        node = self._head
        while node.next is not None:
            if node.value == value:
                return True
            node = node.next
        if node.value == value:
            return True
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        This method returns a new LinkedList object that contains the requested number of nodes from the original list,
        starting with the node located at the requested start index.
        N is the number of nodes in the linked list.
        Valid start_index is in the range of [0, N-1] inclusive.

        If start_index is invalid or if there are not enough nodes between the start_index and end index, the method
        raises a SLLException.
        """
        if start_index < 0 or start_index >= self.length() or size > (self.length() - start_index) or size < 0:
            raise SLLException

        newLinkedList = LinkedList()
        current = self._head.next
        # go to the node at the start_index
        for i in range(start_index):
            current = current.next

        index = 0
        while index < size:
            newLinkedList.insert_at_index(index, current.value)
            current = current.next
            index += 1

        return newLinkedList


if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
