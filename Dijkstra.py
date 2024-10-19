import heapq

class Dijkstra:
    @staticmethod
    def shortest_path(graph, start):
        min_heap = [(0, start)]
        distances = {vertex: float('inf') for vertex in graph}
        distances[start] = 0

        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances

# Example usage
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1},
    }
    print("Dijkstra's Algorithm:", Dijkstra.shortest_path(graph, 'A'))
