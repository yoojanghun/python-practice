# BFS: 시작 node부터 가까운 node들부터 우선적으로 탐색하는 방식
#      한 레벨(거리)의 모든 노드를 먼저 탐색한 뒤, 다음 레벨로 넘어간다.
#      Queue 자료구조를 사용하여 구현 가능

# deque: 양쪽 끝에서 데이터를 삽입하고 삭제하는 작업이 효율적으로(O(1) 시간에) 이루어지는 자료구조
#        deque에 append(), pop() 하면 stack으로
#        deque에 append(), popleft() 하면 queue로 사용 가능

from collections import deque

graph = [
    [1, 2, 3],
    [0, 4],
    [0, 4],
    [0, 4],
    [1, 2, 3]
]
visited = [False] * len(graph)

def BFS(graph, start):
    queue = deque([start])
    visited[start] = True                   # queue에 넣을 때 방문 처리

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for node in graph[node]:
            if not visited[node]:
                queue.append(node)          # queue에 넣을 때 방문 처리
                visited[node] = True

BFS(graph, 0)