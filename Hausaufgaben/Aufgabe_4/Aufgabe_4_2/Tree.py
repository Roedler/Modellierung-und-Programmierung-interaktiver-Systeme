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
