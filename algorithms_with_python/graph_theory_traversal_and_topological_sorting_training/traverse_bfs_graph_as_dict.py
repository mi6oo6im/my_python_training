from collections import deque
# if we switch from queue to stack we get dfs instead of bfs


def bfs(node, graph, visited):
    if node in visited:
        return

    queue = deque([node])
    visited.add(node)

    while queue:
        curr_node = queue.popleft()
        print(curr_node, end=' ')

        for child in graph[curr_node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)


graph = {
    7: [19, 21, 14],
    19: [1, 12, 31, 21],
    21: [14],
    14: [23, 6],
    1: [7],
    12: [],
    31: [21],
    23: [21],
    6: []
}

visited = set()

for node in graph:
    bfs(node, graph, visited)