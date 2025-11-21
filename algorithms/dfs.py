# Traversal: Node i 에서 시작하여 모든 노드들을 방문하는 작업
# Traversal 중 DFS(Depth-first search, 깊이 우선 탐색)

# DFS: 연결된 노드가 없을 때까지 다음 Node들을 탐색하다가, 더 이상 탐색할 노드가 없으면
#      이전 노드로 이동하여 같은 작업 반복
#      시작 노드에서 멀리 떨어진 노드 = 깊이 있는 노드
#      재귀 혹은 스택 자료구조를 사용하여 구현 가능

graph = [
    [1, 2, 3],
    [0, 4],
    [0, 4],
    [0, 4],
    [1, 2, 3]
]
n = len(graph)
visited = [False] * n

stack = []
def DFS(graph, s):
    stack.append(s)
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node, end=" ")        # 방문 순서 출력

        for v in graph[node]:
            if not visited[v]:
                stack.append(v)

DFS(graph, 0)