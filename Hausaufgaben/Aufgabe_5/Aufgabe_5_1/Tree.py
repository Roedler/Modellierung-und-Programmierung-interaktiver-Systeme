class Node:
    def __init__(self, number, left=None, right=None):
        self.data = number # content we want to store
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        self.root = root

    def print_console_tree(self):
        self._print_console_recursive(self.root, 0)

    def _print_console_recursive(self, node, level):
        if node is None:
            return

        indent_space = "      "

        self._print_console_recursive(node.right, level + 1)

        print(f"{indent_space * level}└── {node.data}")

        self._print_console_recursive(node.left, level + 1)

    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            temp_node = self._find_min_node(node.right)
            node.data = temp_node.data
            node.right = self._delete_recursive(node.right, temp_node.data)

        return node

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
