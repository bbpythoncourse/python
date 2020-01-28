def vertexDegree(graph):
    D = {} 
    for v in graph:
        D[v] = len(g[v])
    return D

g = { 'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B'] }

print(vertexDegree(g))