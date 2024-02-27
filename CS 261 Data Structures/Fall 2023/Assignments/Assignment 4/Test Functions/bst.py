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
        """
        Add a new node with value ``value`` to this BST

        :param value: the value to be added to this BST
        """
        curr = self._root
        parent = None
        while curr is not None:
            parent = curr
            if value < curr.value:
                curr = curr.left
            else:
                curr = curr.right

        new_node = BSTNode(value)
        if parent is None:  # if BST is empty, create root
            self._root = new_node
        elif value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

    def remove(self, value: object) -> bool:
        """
        Remove a node with ``value`` from this BST
        :param value: the value of the node to remove
        """
        node, parent = self.find(value)

        # handle case when value is not found
        if node is None and parent is None:
            return False

        if node.left is None and node.right is None:
            self._remove_no_subtrees(parent, node)
        elif node.left is not None and node.right is None:
            self._remove_one_subtree(parent, node)
        elif node.right is not None and node.left is None:
            self._remove_one_subtree(parent, node)
        else:
            self._remove_two_subtrees(parent, node)
        return True

    def _remove_no_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Remove a node with no subtrees
        :param remove_parent: the parent of the node to remove
        :param remove_node: the node to be removed
        """
        # handle root node
        if remove_parent is None:
            self._root = None
            return

        if remove_node.value > remove_parent.value:
            remove_parent.right = None
        else:
            remove_parent.left = None

    def _remove_one_subtree(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Remove a node with a single subtree
        :param remove_parent: the parent of the node to remove
        :param remove_node: the node to be removed
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

    def _remove_two_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Remove a node with two subtrees from this BST

        :param remove_parent: the parent of the node to be removed
        :param remove_node: the node to be removed
        """
        # find successor and successor parent
        successor, successor_parent = self.get_successor(remove_node)
        # set successor's left node to the left node of the removed node
        successor.left = remove_node.left

        # handle where successor is not immediately to right of removed node
        if successor is not remove_node.right:
            successor_parent.left = successor.right
            successor.right = remove_node.right

        # handle case where successor becomes root
        if remove_parent is None:
            self._root = successor
            return
        elif remove_node.value < remove_parent.value:
            remove_parent.left = successor
        else:
            remove_parent.right = successor

    def find(self, value: object) -> (BSTNode, BSTNode):
        """
        Find and return the first occurrence of the node with ``value``
        and its parent

        :param value: the value to find

        :return: a tuple containing the node and its parent (node, parent)
        """
        # handle empty BST
        if self.is_empty():
            return None, None

        # create stack to keep track of nodes
        stack = Stack()
        curr = self._root
        count = 0
        while curr is not None:
            stack.push(curr)
            count += 1
            if value < curr.value:
                curr = curr.left
            elif value > curr.value:
                curr = curr.right
            else:
                # the node has been found
                if count >= 2:
                    return stack.pop(), stack.pop()
                elif stack.is_empty():
                    return None, None
                else:
                    return stack.pop(), None

        # node not found
        return None, None

    def contains(self, value: object) -> bool:
        """
        Determine whether this BST contains ``value``

        :param value: the value to search for in this BST
        """
        node, parent = self.find(value)

        # check if None was returned
        if node is None:
            return False

        # check if possible parent was returned
        if node.value == value:
            return True
        return False

    def inorder_traversal(self) -> Queue:
        """
        Traverse this BST in-order

        :returns: a queue whose values represent the in-order traversal of
        this BST
        """
        # define initial values
        curr = self._root
        queue = Queue()

        # recursively return queue
        return self._traverse_inorder(curr, queue)

    def _traverse_inorder(self, node: BSTNode, queue: Queue) -> Queue:
        """
        Helper method for ``inorder_traversal()`` to allow for recursive calls

        :param node: the BST node to evaluate
        :param queue: the queue which stores each node in-order

        :returns: the queue with in-order values
        """
        if node is not None:
            self._traverse_inorder(node.left, queue)
            queue.enqueue(node.value)
            self._traverse_inorder(node.right, queue)
        return queue

    def find_min(self) -> object:
        """
        Find and return the minimum value stored in this BST

        :returns: the minimum value stored in this BST
        """
        # handle case with empty BST
        if self.is_empty():
            return None

        curr = self._root
        while curr.left is not None:
            curr = curr.left
        return curr.value

    def find_max(self) -> object:
        """
        Find and return the maximum value stored in this BST

        :returns: the maximum value stored in this BST
        """
        # handle case with empty BST
        if self.is_empty():
            return None

        curr = self._root
        while curr.right is not None:
            curr = curr.right
        return curr.value

    def is_empty(self) -> bool:
        """
        Determine if this BST is empty

        :returns: true if empty, false otherwise
        """
        return self._root is None

    def make_empty(self) -> None:
        """
        Remove all the nodes from this tree
        """
        self._root = None

    def get_successor(node: BSTNode) -> (BSTNode, BSTNode):
        """
        Find the in-order successor, and the successor's parent, of ``node``
        """
        # handle invalid node
        if node is None:
            return None, None

        # find in-order successor of node
        successor = node.right
        successor_parent = node
        while successor.left is not None:
            successor_parent = successor
            successor = successor.left
        return successor, successor_parent
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

    print('Local - method remove() example 0')
    print("-------------------------------")
    test_cases = (
        ((1, -87, 12, 18, -11, -42, 55, -40, 27, 92), 1),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

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
