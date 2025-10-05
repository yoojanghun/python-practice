# 이진트리: 각 노드가 최대 2개의 자식을 가지는 트리 자료 구조
# 완전이진트리: 이진트리에서 마지막 레벨을 제외한 모든 노드가 채워져 있으며, 마지막 레벨은 왼쪽부터 노드가 채워진 자료 구조
#             완전이진트리는 배열로 표현 가능 (A[i]의 자식 노드는 A[2i+1], A[2i+2])
# 힙: 완전이진트리 형태를 가진 자료구조. 부모 노드와 자식 노드 간의 대소 관계가 규칙을 가짐(최대 힙, 최소 힙)
# 최대 힙: 부모 노드가 항상 자식 노드보다 크거나 같다 (루트 노드가 가장 큼)
# 최소 힙: 부모 노드가 항상 자식 노드보다 작거나 같다 (루트 노드가 가장 작음)

# Sift down: 주어진 노드가 최대 힙을 만족하지 않을 때, 해당 노드(i)를 아래로 내려보내는 연산
#            자식 노드들은 각각 최대힙을 만족하고 있음을 가정. 해당 노드만 배치하면 됨.
#            left, right child 중 더 큰 값과 교환
def shiftdown(i, arr, n):
    child = 2*i+1           # left child
    while child < n:
        if child+1 < n and arr[child] < arr[child+1]:   # 자식 중 더 큰 값 선택
            child += 1      # right child
        if arr[i] > arr[child]:
            break           # 최대 힙 만족
        arr[i], arr[child] = arr[child], arr[i]
        i = child
        child = 2*i+1

# build heap: 주어진 완전이진트리(배열) 내 원소들을 최대 힙을 만족하도록 재배열하는 연산
def build_heap(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        shiftdown(i, arr, n)

# 주어진 배열(완전이진트리)에 대해 build heap 수행 후
# 최대값(root node)를 배열 맨 뒤로 보내고 교환, shift down 작업 반복
def heapsort(arr):
    build_heap(arr)
    n = len(arr)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        shiftdown(0, arr, i)

arr = [3, 4, 6, 2, 7, 1, 5, 8]
heapsort(arr)
print(arr)