import heapq


# Dijkstra's Algorithm
def dijkstra(graph, start):

    n = len(graph)

    # Initialize distances with infinity
    distances = [float('inf')] * n

    # Priority Queue
    priority_queue = [(0, start)]

    distances[start] = 0

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if a shorter distance is already found
        if current_distance > distances[current_node]:
            continue

        # Check all neighbouring vertices
        for neighbor, weight in graph[current_node]:

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance

                heapq.heappush(
                    priority_queue,
                    (distance, neighbor)
                )

    return distances


# Build Graph using User Input
def build_graph():

    n = int(input("Enter the number of vertices: "))
    m = int(input("Enter the number of edges: "))

    graph = [[] for _ in range(n)]

    print("Enter edges in the format: source destination weight")

    for i in range(m):

        u, v, w = map(int, input().split())

        # Undirected weighted graph
        graph[u].append((v, w))
        graph[v].append((u, w))

    return graph


# Main Function
def main():

    graph = build_graph()

    start = int(input("Enter the starting vertex: "))

    distances = dijkstra(graph, start)

    print(f"\nShortest distances from vertex {start}:")

    for i, d in enumerate(distances):

        print(f"Vertex {i}: {d}")


# Program Execution
if __name__ == "__main__":
    main()
