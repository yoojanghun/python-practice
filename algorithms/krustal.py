# KRUSKAL’S ALGORITHM
# 최소 신장 트리를 구하는 알고리즘
# 신장 트리: 그래프의 모든 정점을 포함하는 트리
# (트리는 사이클이 없고, 연결 그래프이며, 간선 수가 |V|-1,
# 어떤 두 정점 사이에도 단 하나의 경로만 존재)
# 최소 신장 트리: 신장 트리 중 edge 가중치의 합이 최소가 되도록 만든 신장 트리

# greedy algorithm의 한 종류
# weight가 가장 작은 edge 선택해서 mst 배열에 추가 반복
# 만일 edge들이 cycle을 이루면 추가 안 함
# len(mst)가 |v|-1이 될 때까지 반복

# 백준 1197

V, E = map(int, input().split())        # 노드의 갯수: V, 간선의 갯수: N

nodes = [None] * (V+1)                     # make_set
for u in range(1, V+1):
    nodes[u] = u

def find_set(u):                        # find_set
    r = u
    while r != nodes[r]:
        r = nodes[r]
    while u != nodes[u]:
        temp = nodes[u]
        nodes[u] = r
        u = temp

    return nodes[u]

def union(u, v):                        # 각 원소가 속한 집합의 합집합
    u = find_set(u)
    v = find_set(v)
    if u != v:
        nodes[v] = u

edges = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

edges.sort(key=lambda x: x[2])          # weight 기준으로 sort
mst = []
for u, v, w in edges:
    if find_set(u) == find_set(v):
        continue
    else:
        mst.append((u, v, w))
        union(u, v)

sum = 0
for u, v, w in mst:
    sum += w

print(sum)