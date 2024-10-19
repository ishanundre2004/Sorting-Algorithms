import heapq

class Prim:
    @staticmethod
    def minimum_spanning_tree(graph):
        start_vertex = list(graph.keys())[0]
        visited = set()
        min_heap = [(0, start_vertex)]
        total_cost = 0

        while min_heap:
            cost, vertex = heapq.heappop(min_heap)

            if vertex in visited:
                continue

            visited.add(vertex)
            total_cost += cost

            for neighbor, weight in graph[vertex].items():
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor))

        return total_cost

# Example usage
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1},
    }
    print("Prim's Algorithm Cost:", Prim.minimum_spanning_tree(graph))
