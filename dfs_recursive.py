# 인접 행렬로 나타난 그래프
graph = [
    [1, 2, 3],
    [0, 4],
    [0, 4],
    [0, 4],
    [1, 2, 3]
]

visited = [False] * len(graph)
def DFS(graph, start):
    visited[start] = True
    print(start, end=" ")
    for node in graph[start]:
        if not visited[node]:
            DFS(graph, node)

DFS(graph, 0)