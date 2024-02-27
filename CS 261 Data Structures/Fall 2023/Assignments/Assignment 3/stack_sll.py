# Name: Casey Lowe
# OSU Email: lowecas@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment #3
# Due Date: November 7th, 2023
# Description: Implementing a Stack ADT class by using a chain of Singly-Linked Nodes as the underlying
# storage for the following Stack ADT methods: push() pop() top()


from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Add a new value to the top of the stack.
        """
        #  creating the new node
        new_node = SLNode(value)
        new_node.next = self._head
        self._head = new_node

    def pop(self) -> object:
        """
        Remove the top element from the stack and return its value. Raise a custom "StackException"
        if the stack is empty.
        """
        #  verifying the stack to be empty or not before proceeding to remove the top element
        if self.is_empty() is True:
            raise StackException
        else:
            value_to_pop = self._head.value
            self._head = self._head.next
            return value_to_pop

    def top(self) -> object:
        """
        Return the value from the top of the stack without removing it.
        If the stack is empty, raise StackException.
        """
        if self.is_empty():
            raise StackException("Stack is empty")

        return self._head.value

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
