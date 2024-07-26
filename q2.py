def dijkstra(graph, source):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[source] = 0
    visited = set()

    while len(visited) < len(graph):
        min_distance = float("infinity")
        min_vertex = None
        for vertex in distances:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        if min_vertex is None:
            break

        for neighbor, weight in graph[min_vertex].items():
            if neighbor not in visited:
                new_distance = distances[min_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        visited.add(min_vertex)

    return distances


graph = {0: {1: 4, 2: 1}, 1: {3: 1}, 2: {1: 2, 3: 5}, 3: {}}
source = 0

shortest_paths = dijkstra(graph, source)
print(shortest_paths)
