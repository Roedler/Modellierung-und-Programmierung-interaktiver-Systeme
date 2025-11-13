from Hausaufgaben.Aufgabe_4.Aufgabe_4_2.Tree import Tree, Node


def aufgabe_4_2():
    print("--- Instanz Baum (a) ---")
    tree_a = Tree(Node(10,
                  Node(5,
                       Node(2, Node(1), Node(4)),
                       Node(7, Node(6), Node(8))
                       ),
                  Node(15,
                       Node(12, Node(11), Node(14)),
                       Node(17, Node(16), Node(20))
                       )
                  ))

    tree_a.print_console_tree()
