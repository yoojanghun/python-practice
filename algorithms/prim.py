# PRIM’S ALGORITHM
# 최소 신장 트리를 구하는 알고리즘
# greedy algorithm의 한 종류
# 아무 정점 하나를 선택하여 MST에 추가
# MST와 직접 연결된 외부 정점 중 가장 가까운 정점을 MST에 추가
# 모든 정점이 MST에 추가될 때까지 반복

# 후보 Edge의 가중치들로 Min-heap을 구성하고 계속 업데이트 하면 효율적

import heapq
n = 7
visited = [False] * n
def prim(graph, start):
    total_weight = 0
    min_heap = [(0, start)]                         # (weight, start)

    while min_heap:
        weight, node = heapq.heappop(min_heap)      # heap에서 최소 찾음
        if visited[node]:
            continue

        visited[node] = True
        total_weight += weight

        for next_node, next_weight in graph[node]:
            if not visited[next_node]:
                heapq.heappush(min_heap, (next_weight, next_node))      # weight를 기준으로 min_heap 구성
                                                                             # heapq는 튜플에서 첫 번째 요소로 비교한다
    return total_weight

graph = [
    [(1, 8), (3, 10)],
    [(0, 8), (2, 9), (4, 11)],
    [(1, 9), (3, 5), (4, 13), (6, 12)],
    [(0, 10), (2, 5)],
    [(1, 11), (2, 13), (5, 8)],
    [(4, 8), (6, 7)],
    [(2, 12), (5, 7)]
]

print(prim(graph, 0))