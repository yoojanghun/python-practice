# 그래프에서 시작 노드에서 끝 노드까지 이동할 때, 가장 비용이 최소인 path 찾기
# 시작 node s의 최단거리 dist[s] = 0으로, 나머지 node v의 최단거리 dist[v] = inf

# 모든 edge(u, v, w)에 대해 dist[v]와 경로를 갱신
# dist[v] = min(dist[v], dist[u] + w)
# 이 과정을 |V|-1회 반복

# 경로에서 최대 포함될 수 있는 node는 |V|-1개
# 음의 사이클이 있는 지 확인
# 경로 갱신이 끝난 후 dist[u] + w < dist[v]이면 음의 사이클 존재

n = 4
prev = [-1] * (n + 1)                             # 이전 node 저장
dist = [float("inf")] * (n + 1)                   # Node s와의 거리

def bellmanford(graph, s):
    dist[s] = 0

    for _ in range(n-1):
        for (u, v, w) in graph:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u                       # v 이전엔 u 였다

    for (u, v, w) in graph:
        if dist[u] + w < dist[v]:
            print("음의 사이클이 존재")

graph = [
    (1, 2, 6),
    (1, 3, 7),
    (2, 3, 8),
    (3, 4, -3),
    (4, 2, -2)
]

bellmanford(graph, s=1)
print(dist)

# 사이클 없는 모든 최단경로는 길이가 최대 n−1개의 간선을 가진다.
# 따라서 간선을 n−1번 반복해서 for 문을 돌면
# 길이 1, 2, … n−1인 모든 최단경로가 완성된다.
# 그래서 n−1번 반복하면 최단거리가 모두 결정된다.