from node import Node

class Tree:
    """Tree class for managing a binary tree."""

    def __init__(self):
        """Initialize the Tree with root set to None."""
        self.root = None

    def getRoot(self):
        """Return the root node of the tree.

        Returns:
            Node: The root node of the tree.
        """
        return self.root

    def add(self, data):
        """Add a new node with the specified data to the tree.

        Args:
            data (int): The data to add to the tree.
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Recursive helper function to add data to the tree.

        Args:
            data (int): The data to add to the tree.
            node (Node): The node from which to continue adding the data.
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Find and return the node containing the specified data.

        Args:
            data (int): The data to find within the tree.

        Returns:
            Node: The node containing the specified data, or None if not found.
        """
        if self.root is not None:
            return self._find(data, self.root)
        return None

    def _find(self, data, node):
        """Recursive helper function to find data within the tree.

        Args:
            data (int): The data to find.
            node (Node): The node from which to continue the search.

        Returns:
            Node: The node containing the specified data, or None if not found.
        """
        if data == node.data:
            return node
        elif data < node.data and node.left is not None:
            return self._find(data, node.left)
        elif data > node.data and node.right is not None:
            return self._find(data, node.right)

    def deleteTree(self):
        """Delete the entire tree, setting the root to None."""
        self.root = None

    def printTree(self):
        """Print the entire tree in an in-order manner."""
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        """Recursive helper function to print the tree in-order.

        Args:
            node (Node): The node from which to start the in-order print.
        """
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """Recursive helper function to print the tree in pre-order.

        Args:
            node (Node): The node from which to start the pre-order print.
        """
        result = []
        if node is not None:
            result.append(str(node.data))
            result.extend(self._printPreorderTree(node.left))
            result.extend(self._printPreorderTree(node.right))
        return result

    def _printPostorderTree(self, node):
        """Recursive helper function to print the tree in post-order.

        Args:
            node (Node): The node from which to start the post-order print.
        """
        result = []
        if node is not None:
            result.extend(self._printPostorderTree(node.left))
            result.extend(self._printPostorderTree(node.right))
            result.append(str(node.data))
        return result

    def useless(self):
        """A placeholder method to demonstrate a method with no practical functionality."""
        print("This is a useless method")

    def printPreorder(self):
        return ' '.join(self._printPreorderTree(self.root))

    def printPostorder(self):
        return ' '.join(self._printPostorderTree(self.root))
    
    
import unittest

class TestTree(unittest.TestCase):
    def test_find_existing(self):
        tree = Tree()
        data = [20, 10, 30, 5, 15, 25, 35]
        for num in data:
            tree.add(num)
        node = tree._find(15, tree.root)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 15)

    def test_find_non_existing(self):
        tree = Tree()
        data = [20, 10, 30, 5, 15, 25, 35]
        for num in data:
            tree.add(num)
        node = tree._find(100, tree.root)
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()
