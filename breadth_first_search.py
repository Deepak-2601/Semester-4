def bfs(graph, start_node, end_node):
    visited_node = []
    queue = [start_node]
    predecessor_nodes = {}
    while queue:
        current_node = queue.pop(0)
        visited_node.append(current_node)
        for neighbours in graph[current_node]:
            if neighbours not in visited_node:
                queue.append(neighbours)
                predecessor_nodes[neighbours] = current_node
    print(shortest_path(predecessor_nodes, start_node, end_node))


def shortest_path(predecessor_nodes, start_nodes, end_node):
    path = [end_node]
    current_nodes = end_node
    while current_nodes != start_nodes:
        current_nodes = predecessor_nodes[current_nodes]
        path.append(current_nodes)
    path.reverse()
    return path


test_graph = {'0': ['3', '5', '9'],
              '1': ['6', '7', '4'],
              '2': ['10', '5'],
              '3': ['0'],
              '4': ['1', '5', '8'],
              '5': ['2', '0', '4'],
              '6': ['1'],
              '7': ['1'],
              '8': ['4'],
              '9': ['0'],
              '10': ['2'],
              }
bfs(test_graph, '0', '1')
