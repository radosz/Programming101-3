from copy import deepcopy


class DirectedGraph:

    def __init__(self):
        self.graph = {}

    def add_nodes(self, lst_node_a, values):
        for person, value in zip(lst_node_a, values):
            if not isinstance(value, list):
                if person not in self.graph:
                    self.graph[person] = [x for x in set([value])]
            elif isinstance(value, list):
                if person not in self.graph:
                    self.graph[person] = [x for x in set(value)]

    def add_edge(self, node_a, node_b):
        if node_a not in self.graph:
            self.graph[node_a] = []
        if node_b not in self.graph:
            self.graph[node_b] = []
        if node_b not in self.graph[node_a]:
            self.graph[node_a].append(node_b)

    def get_neighbors_for(self, node):
        return deepcopy(self.graph[node])

    def path_between(self, node_a, node_b):
        queue = self.get_neighbors_for(node_a)

        if node_b in self.get_neighbors_for(node_a):
            return True

        visited = []
        while queue and queue[0] not in visited:
            visited.append(queue.pop(0))
            if node_b in self.get_neighbors_for(visited[-1]):
                return True
        return False


def main():
    g = DirectedGraph()
    g.graph = {
        0: [1, 2],
        1: [2, 3, 0],
        2: [3, 5],
        3: [4, 1],
        4: [0],
        6: [],
        7: [6]
    }

    print(g.path_between(0, 3))  # True
    print(g.path_between(3, 0))  # True
    print(g.path_between(0, 7))  # False
    print(g.path_between(0, 5))  # True
    print(g.path_between(0, 3))  # True
    print(g.path_between(1, 0))  # True
    print(g.path_between(3, 1))  # True
    print(g.path_between(4, 0))  # True
    print(g.add_edge(9, 10))
    print(g.path_between(9, 10))  # True
    print(g.path_between(10, 9))  # False

if __name__ == '__main__':
    main()
