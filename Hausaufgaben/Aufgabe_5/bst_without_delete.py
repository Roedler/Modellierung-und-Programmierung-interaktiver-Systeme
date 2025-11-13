import random # used for test routines


class Node:
    def __init__(self, number, left=None, right=None):
        """
        Construct a new 'Node' object for a binary search tree which stores numbers.

        :param number: The number to be stored
        :param left: left child of the node
        :param right: right child of the node
        :return: returns nothing
        """
        self.data = number  # content we want to store
        self.left  = left
        self.right = right

    def print_sorted(self):
        """
        Prints the contents of the node and its children in sorted order.

        return: returns nothing
        """
        if self is None: return
        if self.left is not None: self.left.print_sorted()
        print(self.data)
        if self.right is not None: self.right.print_sorted()

    def search(self, search_number):
        """
        Searches in the node and its children the node containing a certain number.

        :param search_number: The number to be searched
        :return: returns the node containing search_number or None if not found
        """
        if self is None: return None
        elif self.data == search_number: return self
        elif search_number < self.data and self.left is not None: return self.left.search(search_number)
        elif search_number > self.data and self.right is not None: return self.right.search(search_number)
        else: return None


    def add(self, new_number):
        """
        Adds a new node in the subtree containing a certain number.
        If the number is already in the subtree, nothing happens.

        :param new_number: The number to be added
        :return: returns nothing
        """
        if new_number < self.data:
            if self.left is None: self.left = Node(new_number)
            else: self.left.add(new_number)
        elif new_number > self.data:
            if self.right is None: self.right = Node(new_number)
            else: self.right.add(new_number)







class Tree():
    def __init__(self, root=None):
        """
        Construct a new 'Tree' object for a binary search tree which stores numbers.

        :param root: The root node of the tree. If None the tree starts empty.
        :return: returns nothing
        """
        self.root = root

    def print_sorted(self):
        """
        Prints the content of the tree in sorted order.

        return: returns nothing
        """
        if self.root is not None: self.root.print_sorted()

    def search(self, search_number):
        """
        Searches in the tree the node containing a certain number.

        :param search_number: The number to be searched
        :return: returns the node containing search_number or None if not found
        """
        if self.root is None: return None
        return self.root.search(search_number)


    def add(self, new_number):
        """
        Adds a new node in the tree containing a certain number.
        If the number is already in the tree, nothing happens.

        :param new_number: The number to be added
        :return: returns nothing
        """
        if self.root is None: self.root = Node(new_number)
        else: self.root.add(new_number)








tree1 = Tree(Node(10,
                 Node(5,
                      Node(2,
                           Node(1), Node(4)),
                      Node(7,
                           Node(6), Node(8))),
                 Node(15,
                      Node(12,
                           Node(11), Node(14)),
                      Node(17,
                           Node(16), Node(20)))
                 )
             )
print("tree1:")
tree1.print_sorted()

for i in range(-2, 22):
    print(i, ": ", tree1.search(i))





tree2 = Tree(Node(1, None, Node(2, None, Node(4, None,
                                         Node(7, None, Node(18, None, Node(20)))))))

print("\ntree2:")
tree2.print_sorted()

for i in range(-2, 22):
    print(i, ": ", tree2.search(i))



tree3 = Tree()
for i in range(20):
    tree3.add(i)

print("tree3:")
tree3.print_sorted()

for i in range(-2, 22):
    print(i, ": ", tree3.search(i))


tree4 = Tree()
for i in random.sample(range(20), 20):
    tree4.add(i)

print("tree4:")
tree4.print_sorted()

for i in range(-2, 22):
    print(i, ": ", tree4.search(i))



