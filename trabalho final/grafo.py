#construção de um grafo
grafo = { 
    "A": {
        "info": [4, False, False, 0],
        "vizinhos": [("B", 3), ("C", 5)]
    },
    "B": {
        "info": [5, False, False, 0],
        "vizinhos": [("A", 3), ("D", 2)]
    },
    "C": {
        "info": [5, False, False, 0],
        "vizinhos": [("A", 5), ("D", 4)]
    },
    "D": {
        "info": [4, False, False, 0],
        "vizinhos": [("B", 2), ("C", 4), ("E", 6)]
    },
    "E": {
        "info": [6, False, False, 0],
        "vizinhos": [("D", 6), ("F", 1)]
    },
    "F": {
        "info": [5, False, False, 0],
        "vizinhos": [("E", 1), ("G", 3)]
    },
    "G": {
        "info": [6, False, False, 0],
        "vizinhos": [("F", 3), ("H", 2)]
    },
    "H": {
        "info": [4, False, False, 0],
        "vizinhos": [("G", 2), ("I", 4)]
    },
    "I": {
        "info": [5, False, False, 0],
        "vizinhos": [("H", 4), ("J", 5)]
    },
    "J": {
        "info": [5, False, False, 0],
        "vizinhos": [("I", 5)]
    }
}


# grafo = {
#     'A': [[3, False, False, 0], [('B', 1), ('C', 2), ('G', 5), ('F', 3)]],
#     'B': [[2, False, False, 0], [('B', 1), ('C', 4), ('H', 4)]],
#     'C': [[1, False, False, 0], [('A', 3), ('E', 4)]], 
#     'D': [[4, False, False, 0], [('B', 2), ('I', 1), ('D', 3)]],
#     'E': [[5, False, False, 0], [('H', 2), ('G', 4), ('I', 1)]],
#     'F': [[6, False, False, 0], [('C', 3), ('D', 2), ('H', 1)]],
#     'G': [[6, False, False, 0], [('A', 5), ('I', 5),('B', 2), ('C', 4), ('D', 1)]],
#     'H': [[5, False, False, 0], [('E', 4), ('G', 2), ('E', 1), ('D', 3)]],
#     'I': [[4, False, False, 0], [('E', 1), ('G', 5), ('H', 2), ('F', 3)]],
# }

print(grafo)