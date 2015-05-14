def connection_level(graph, panda1, panda2):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([panda1])

    if panda1 not in graph.keys() or panda2 not in graph.keys():
        return -1

    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == panda2:
            return len(path) - 1
        # enumerate all adjacent nodes, construct a new path and push it into
        # the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
