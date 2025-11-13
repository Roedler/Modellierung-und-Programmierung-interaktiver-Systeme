from Hausaufgaben.Aufgabe_4.Aufgabe_4_2.Tree import Tree


def search_in_tree(node: Tree, value):
    if node is None:
        return False

    if node.data == value:
        return True
    elif value < node.data:
        return search_in_tree(node.left, value)
    else:
        return search_in_tree(node.right, value)
