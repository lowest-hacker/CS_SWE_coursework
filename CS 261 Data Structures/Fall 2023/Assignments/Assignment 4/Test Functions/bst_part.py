# Name: Casey Lowe
# OSU Email: lowecas@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment #4 - AVL
# Due Date: 11/20/2023
# Description: BST


import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value  # to store node's data
        self.left = None  # pointer to root of left subtree
        self.right = None  # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Override string method; display in pre-order
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.

        This is intended to be a troubleshooting method to help find any
        inconsistencies in the tree after the add() or remove() operations.
        A return of True from this method doesn't guarantee that your tree
        is the 'correct' result, just that it satisfies bst ordering.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """Adds a new value to the tree"""
        new_node = BSTNode(value)
        current_node = self._root
        while current_node is not None:  # runs until the desired node is reached
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                current_node = current_node.left

            elif value >= current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                current_node = current_node.right

    def remove(self, value: object) -> bool:
        """
         Remove a value from the tree. Return True if the value is removed and return False otherwise.
        """
        new_node = BSTNode(value)
        if self._root is None:
            return False
        current_node = self._root
        parent = None
        while current_node is not None:
            if new_node.value < current_node.value:
                parent = current_node
                current_node = current_node.left
            elif new_node.value > current_node.value:
                parent = current_node
                current_node = current_node.right
            else:
                if current_node.left is None and current_node.right is None:
                    self._remove_no_subtrees(parent, current_node)
                elif current_node.left is None or current_node.right is None:
                    self._remove_one_subtree(parent, current_node)
                else:
                    self._remove_two_subtrees(parent, current_node)
                return True
        return False

    # Consider implementing methods that handle different removal scenarios; #
    # you may find that you're able to use some of them in the AVL.          #
    # Remove these comments.                                                 #
    # Remove these method stubs if you decide not to use them.               #
    # Change these methods in any way you'd like.                            #

    def _remove_no_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Helper function for remove() when the node to remove has no subtrees.
        """
        # remove node that has no subtrees (no left or right nodes)
        if remove_node.left is None and remove_node.right is None:
            if remove_parent is not None and remove_node == remove_parent.left:
                remove_parent.left = None
            elif remove_parent is not None and remove_node == remove_parent.right:
                remove_parent.right = None
            else:
                self._root = None

    def _remove_one_subtree(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Helper function for remove() when the node to remove, has one subtree either on the left or right.
        """
        # remove node that has a left or right subtree (only)
        if remove_node.left is not None:
            child = remove_node.left
        else:
            child = remove_node.right
        if remove_parent is not None and remove_node == remove_parent.left:
            remove_parent.left = child
        elif remove_parent is not None and remove_node == remove_parent.right:
            remove_parent.right = child
        else:
            self._root = child
        return self._root

    def _remove_two_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Helper function for remove() when the node to remove has two subtrees on both sides.
        """
        # remove node that has two subtrees
        # need to find inorder successor and its parent (make a method!)
        if remove_node.right is not None:
            initial_right = remove_node.right
            parent = remove_node
            while initial_right.left is not None:
                parent = initial_right
                initial_right = initial_right.left
            if remove_node.right is not initial_right:
                parent.left = initial_right.right
                initial_right.right = remove_node.right
            initial_right.left = remove_node.left
            if remove_parent is None:
                self._root = initial_right
            elif remove_parent.value > remove_node.value:
                remove_parent.left = initial_right
            else:
                remove_parent.right = initial_right

    def contains(self, value: object) -> bool:
        """Determines if the binary tree contains the given value"""
        current = self._root
        # runs until the value is found
        while current is not None:
            if value < current.value:
                current = current.left
            elif value >= current.value:
                # if the value is found, return True
                if current.value == value:
                    return True
                current = current.right
        return False

    def in_order_traversal(self) -> Queue:
        """In order, traversal function outputs the values of the BST in the que as it is traversed FROM THE BOTTOM.
        A helper function is used to help with recursive calls"""

        # initialize new_queue
        new_queue = Queue()
        # call helper and using the root node and que as arguments
        self.in_order_traversal_helper(self._root, new_queue)
        return new_queue

    def in_order_traversal_helper(self, current_node, new_queue):
        """helper function for in order traversal"""

        # return once traversal is completed
        if current_node is None:
            return

        else:
            # move node left
            self.in_order_traversal_helper(current_node.left, new_queue)
            # add value
            new_queue.enqueue(current_node.value)
            # move node right
            self.in_order_traversal_helper(current_node.right, new_queue)

    def find_min(self) -> object:
        """
        Return the lowest value in the tree. Return None if the tree is empty.
        """
        if self.is_empty():
            return None
        else:
            current_node = self._root
            while current_node.left is not None:
                current_node = current_node.left
            return current_node.value

    def find_max(self) -> object:
        """
        Return the highest value in the tree. Return None if the tree is empty.
        """
        if self.is_empty():
            return None
        else:
            current_node = self._root
            while current_node.right is not None:
                current_node = current_node.right
            return current_node.value

    def is_empty(self) -> bool:
        """
        Return True if the tree is empty and return False otherwise.
        """
        if self._root is None:
            return True
        else:
            return False

    def make_empty(self) -> None:
        """
        Remove all the nodes from the tree.
        """
        self._root = None


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
