import heapq

def dijkstra(start, final):
    graph = {
        "A": [("B", 2), ("D", 1)],
        "B": [("C", 2), ("E", 2), ("F", 4)],
        "C": [("F", 4)],
        "D": [("G", 5)],
        "E": [("H", 1)],
        "F": [("E", 3)],
        "G": [("F", 7), ("H", 6)],
        "H": [],
    }

    cost = {}
    pq = []
    heapq.heappush(pq, (0, start)) 

    while pq:
        cur_cost, cur_value = heapq.heappop(pq)
        if cur_value not in cost:

            cost[cur_value]=cur_cost
            for next_value, edge_cost in graph[cur_value]:
                next_cost = cur_cost + edge_cost
                heapq.heappush(pq,(next_cost,next_value))
    
    return cost[final]

print(dijkstra("A", "H"))