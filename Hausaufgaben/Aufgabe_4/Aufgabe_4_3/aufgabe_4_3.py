from Hausaufgaben.Aufgabe_4.Aufgabe_4_2.Tree import Tree, Node


def aufgabe_4_3():
    print("--- Instanz Baum (b) ---")
    tree_b = Tree(Node(1,
                  None,
                  Node(2,
                       None,
                       Node(4,
                            None,
                            Node(7,
                                 None,
                                 Node(18,
                                      None,
                                      Node(20)
                                      )
                                 )
                            )
                       )
                  ))

    tree_b.print_console_tree()
