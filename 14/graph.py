class Edge:
    """Klasa dla krawędzi skierowanej z wagą."""

    def __init__(self, source, target, weight=1):
        """Konstruktor krawędzi.."""
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        """Zwraca reprezentacje napisowa krawędzi.."""
        if self.weight == 1:
            return "Edge(%s, %s)" % (
                repr(self.source), repr(self.target))
        else:
            return "Edge(%s, %s, %s)" % (
                repr(self.source), repr(self.target), repr(self.weight))

    def __cmp__(self, other):
        """Porównywanie krawędzi."""
        if self.weight > other.weight:
            return 1
        if self.weight < other.weight:
            return -1
        if self.source > other.source:
            return 1
        if self.source < other.source:
            return -1
        if self.target > other.target:
            return 1
        if self.target < other.target:
            return -1
        return 0

    def __hash__(self):
        """Krawędzie są hashowalne."""
        # return hash(repr(self))
        return hash((self.source, self.target, self.weight))

    def __invert__(self):
        """Zwraca krawędź o przeciwnym kierunku."""
        return Edge(self.target, self.source, self.weight)


class Graph:
    """Klasa dla grafu ważonego, skierowanego lub nieskierowanego."""

    def __init__(self, n, directed=False):
        self.n = n                      # kompatybilność
        self.directed = directed        # bool, czy graf skierowany

    def v(self):                        # zwraca liczbę wierzchołków
        return self.n

    def e(self):                        # zwraca liczbę krawędzi

    def is_directed(self):              # bool, czy graf skierowany
        return self.directed

    def add_node(self, node): pass      # dodaje wierzchołek

    def has_node(self, node): pass      # bool

    def del_node(self, node): pass      # usuwa wierzchołek

    def add_edge(self, edge): pass      # wstawienie krawędzi

    def has_edge(self, edge): pass      # bool

    def del_edge(self, edge): pass      # usunięcie krawędzi

    def weight(self, edge): pass        # zwraca wagę krawędzi

    def iternodes(self): pass           # iterator po wierzchołkach

    def iteradjacent(self, node): pass  # iterator po wierzchołkach sąsiednich

    def iteroutedges(self, node): pass  # iterator po krawędziach wychodzących

    # iterator po krawędziach przychodzących
    def iterinedges(self, node): pass

    def iteredges(self):                # iterator po krawędziach

    def copy(self): pass                # zwraca kopię grafu

    def transpose(self): pass           # zwraca graf transponowany

    def complement(self): pass          # zwraca dopełnienie grafu

    def subgraph(self, nodes): pass     # zwraca podgraf indukowany


class EdgeIterator:

    __init__(self, graph):
        self.graph = graph

    def __iter__(self):
        self.current = 
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
