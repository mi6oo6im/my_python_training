def dfs(node, graph, visited):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited)

    print(node, end=' ')


graph = [
    [6, 3],
    [2, 4, 6, 3, 5],
    [4, 1, 5],
    [5, 1, 0],
    [6, 1, 2],
    [2, 1, 3],
    [4, 1, 0]
]

visited = [False] * len(graph)

for child in range(len(graph)):
    dfs(child, graph, visited)