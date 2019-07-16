class Node():
    """ Node class for A* Pathfinding algorithm """

    def __init__(self, node, cost, parent=None, heuristic=None):
        """
        node        : current node being evaluated
        parent      : parent node relative to 'node'
        cost        : transition cost
        heuristic   : heuristic function used to calculate h(n)
        """
        self.parent = parent
        self.node = node
        self.cost = cost
        self.g = 0
        self.h = 0
        self.f = self.g + self.h

    def __eq__(self, other):
        """ Equal to comparaison method"""
        return self.node == other.node

    def __lt__(self, other):
        """ Lesser than comparaison method """
        return self.f < other.f

    def __gt__(self, other):
        """ Greater than comparaison method """
        return self.f > other.f
