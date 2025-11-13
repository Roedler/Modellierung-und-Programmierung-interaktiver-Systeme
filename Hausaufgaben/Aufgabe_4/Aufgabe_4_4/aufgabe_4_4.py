from Hausaufgaben.Aufgabe_4.Aufgabe_4_2.Tree import Tree
from Hausaufgaben.Aufgabe_4.Aufgabe_4_4.TreeSearch import search_in_tree


def aufgabe_4_4():
    tree_a = Tree(10,
                  Tree(5,
                       Tree(2, Tree(1), Tree(4)),
                       Tree(7, Tree(6), Tree(8))
                       ),
                  Tree(15,
                       Tree(12, Tree(11), Tree(14)),
                       Tree(17, Tree(16), Tree(20))
                       )
                  )

    print("\n--- Baum (a) wird durchsucht: ---")
    tree_a.print_tree()

    searchData = [
        10, 7, 20, 9, 3
    ]

    print("\n--- Suchergebnisse: ---")
    for value in searchData:
        print(f"Suche nach {value}: {search_in_tree(tree_a, value)}")
