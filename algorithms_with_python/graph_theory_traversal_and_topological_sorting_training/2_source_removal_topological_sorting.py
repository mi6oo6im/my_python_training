def find_dependencies(graph):
    result = {}

    for node, children in graph.items():
        if node not in result:
            result[node] = 0

        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1

    return result


nodes = int(input())

graph = {}

for _ in range(nodes):
    composite_line = input()
    node = composite_line.split('->')[0].strip()
    values = composite_line.split('->')[1].strip()
    graph[node] = [] if not values else values.split(', ')

dependencies_by_node = find_dependencies(graph)
has_cycles = False
sorted_nodes = []

while dependencies_by_node:
    try:
        node_to_remove = next(filter(lambda n: dependencies_by_node[n] == 0, dependencies_by_node))
    except StopIteration:
        has_cycles = True
        break
    for child in graph[node_to_remove]:
        dependencies_by_node[child] -= 1

    del dependencies_by_node[node_to_remove]
    sorted_nodes.append(node_to_remove)
if has_cycles:
    print('Invalid topological sorting')
else:
    print('Topological sorting:', ', '.join(sorted_nodes))