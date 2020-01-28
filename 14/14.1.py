
def list_nodes(graph):
    return list(graph.keys())


def list_edges(graph):
    """"Zwraca listę krawędzi (2-krotek) grafu skierowanego bez wag."""
    L = []
    for source in graph:
        for target in graph[source]:
            L.append((source, target))
    return L

def count_nodes(graph): 
    return len(graph)

def count_edges(graph): 
    return int(len(list_edges(graph)) / 2)



g = { 'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B'] }

print("wierzcholki: " + str(list_nodes(g)))
print("krawedzie: " + str(list_edges(g)))
print("liczba krawedzi: " + str(count_nodes(g)))
print("liczba wierzcholkow: " + str(count_edges(g)))
