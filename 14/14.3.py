from graph import Graph

def save_edges(graph, filename):
    with open(filename, 'w') as f:
        for i, v in enumerate(graph):
            adj = graph[v]
            for u in adj:
                f.write(str(i) + ' ' + str(list(graph.keys()).index(u)) + '\n')

g = { 'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B'] }
save_edges(g, 'data.txt')