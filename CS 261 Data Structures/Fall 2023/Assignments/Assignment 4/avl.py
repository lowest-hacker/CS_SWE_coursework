
# Name: Casey Lowe
# OSU Email: lowecas@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment #4 AVL
# Due Date: 11/19/2023
# Description: Implementation of add() and remove() functions with helper functions to assist in the reduction of code.


import random
from queue_and_stack import Queue, Stack
from bst import BSTNode, BST


class AVLNode(BSTNode):
    """
    AVL Tree Node class. Inherits from BSTNode
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(value)

        # new variables needed for AVL
        self.parent = None
        self.height = 0

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'AVL Node: {}'.format(self.value)


class AVL(BST):
    """
    AVL Tree class. Inherits from BST
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(start_tree)

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        super()._str_helper(self._root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                # check for correct height (relative to children)
                left = node.left.height if node.left else -1
                right = node.right.height if node.right else -1
                if node.height != 1 + max(left, right):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self._root:
                        return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Add a node to this AVL tree
        """
        # check if value exists in tree, return if true
        if super().contains(value):
            return

        curr = self.get_root()
        parent = None

        while curr is not None:
            parent = curr
            if value < curr.value:
                curr = curr.left
            else:
                curr = curr.right

        new_node = AVLNode(value)
        new_node.parent = parent

        # assign new node to root as necessary
        if parent is None:
            self._root = new_node
        elif value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        self._update_height(new_node)
        self._repeatBalance(new_node)

    def remove(self, value: object) -> bool:
        """
        Remove the node with ``value`` from this tree
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
                if current_node.left is not None and current_node.right is None:
                    self._remove_no_subtrees(parent, current_node)
                elif current_node.left is not None or current_node.right is None:
                    self._remove_one_subtree(parent, current_node)
                else:
                    self._remove_two_subtrees(parent, current_node)
                return True
        return False

    def _remove_one_subtree(self, remove_parent: AVLNode, remove_node: AVLNode) -> \
            None:
        """
        Remove a node with a single subtree
        """
        # get tree of removed_node
        if remove_node.right is not None:
            child = remove_node.right
            remove_node.right = None
        else:
            child = remove_node.left

            # determine if removed node is root
        if remove_parent is None:
            self._root = child
            return

            # find which side of the parent the removed node exists on
        if remove_node.value > remove_parent.value:
            # node is on right side of parent
            remove_parent.right = child
        else:
            remove_parent.left = child

    def _remove_two_subtrees(self, parent: AVLNode, node: AVLNode) -> AVLNode:
        """
        Remove a node with two subtrees
        """
        # remove node that has two subtrees
        # need to find inorder successor and its parent (make a method!)
        if node.right is not None:
            initial_right = node.right
            parent = node
            while initial_right.left is not None:
                parent = initial_right
                initial_right = initial_right.left
            if node.right is not initial_right:
                parent.left = initial_right.right
                initial_right.right = node.right
            initial_right.left = node.left
            if parent is None:
                self._root = initial_right
            elif parent.value > node.value:
                parent.left = initial_right
            else:
                parent.right = initial_right

    def _balance_factor(self, node: AVLNode) -> int:
        """
        Return the balance factor of ``node``.
        """
        # handle invalid node
        if node is None:
            return 0

        right_height = 0
        left_height = 0

        if node.right is not None:
            right_height = node.right.height + 1
        if node.left is not None:
            left_height = node.left.height + 1

        return right_height - left_height

    def _get_height(self, node: AVLNode) -> int:
        """
        Gets the height of the subtree of which ``node`` is the root.
        Returns 0 if no subtree tree exists.
        """
        # handle case where no tree exists
        if node is None:
            return 0

        # handle case where node has no children
        if node.left is None and node.right is None:
            return 0

        left = node.left.height if node.left is not None else 0
        right = node.right.height if node.right is not None else 0
        height = max(left, right) + 1

        return height

    def _rotate_left(self, node: AVLNode) -> AVLNode:
        """
        Rotate the subtree, rooted at ``node`` to the left
        """
        new_parent = node.right

        # update root if needed
        if node.parent is None:
            self._root = new_parent
            new_parent.parent = None
        else:
            new_parent.parent = node.parent
            if node.parent.left is node:
                node.parent.left = new_parent
            elif node.parent.right is node:
                node.parent.right = new_parent

        node.parent = new_parent
        node.right = new_parent.left
        new_bottom = new_parent.left

        # make sure parent is accounted for
        if new_parent.left is not None:
            new_parent.left.parent = node
        new_parent.left = node

        # update height starting at lowest node
        if new_bottom is not None:
            self._update_height(new_bottom)
        else:
            self._update_height(node)

        return new_parent

    def _rotate_right(self, node: AVLNode) -> AVLNode:
        """
        Rotate the subtree, rooted at ``node`` to the right
        """
        new_parent = node.left

        # update root if needed
        if node.parent is None:
            self._root = new_parent
            new_parent.parent = None
        else:
            new_parent.parent = node.parent
            if node.parent.left is node:
                node.parent.left = new_parent
            elif node.parent.right is node:
                node.parent.right = new_parent

        node.parent = new_parent
        node.left = new_parent.right
        new_bottom = new_parent.right

        # make sure parent is accounted for
        if new_parent.right is not None:
            new_parent.right.parent = node
        new_parent.right = node

        # update height starting at lowest node
        if new_bottom is not None:
            self._update_height(new_bottom)
        else:
            self._update_height(node)

        return new_parent

    def _update_height(self, node: AVLNode) -> None:
        """
        Update the height of ``node`` and all ``node`` parents up to the root
        """
        while node is not None:
            node.height = self._get_height(node)
            node = node.parent

    def _repeatBalance(self, node: AVLNode) -> None:
        """
        Repeatbalance the ``node`` subtree
        """
        while node is not None:
            # node is right-heavy
            if self._balance_factor(node) >= 2:
                # RL, RR rotation
                if self._balance_factor(node.right) <= -1:
                    self._rotate_right(node.right)
                node = self._rotate_left(node)
            # node is left-heavy
            elif self._balance_factor(node) <= -2:
                # LR, LL
                if self._balance_factor(node.left) >= 1:
                    self._rotate_left(node.left)
                node = self._rotate_right(node)
            else:
                node = node.parent

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        tree = AVL(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 20, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL()
        for value in case:
            tree.add(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = AVL(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = AVL(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL(case)
        for value in case[::2]:
            tree.remove(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('remove() stress test finished')

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = AVL([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = AVL()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
