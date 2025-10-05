# Quick Sort = 배열 원소 중 하나를 pivot으로 설정 후,
#              pivot보다 작은 값들은 왼쪽, 큰 값들은 오른쪽에 배치를 반복

# 아래는 pivot을 배열 마지막 원소로 설정
def quicksort1(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) - 1]

        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]

        return quicksort1(less) + equal + quicksort1(greater)

arr = [3, 4, 6, 2, 7, 1, 5, 8]
print(quicksort1(arr))

print()

def quicksort2(arr, left, right):
    if left + 1 >= right: return
    pivot = partition(arr, left, right)
    quicksort2(arr, left, pivot)
    quicksort2(arr, pivot + 1, right)

def partition(arr, left, right):
    pivot = arr[right-1]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return i-1

arr = [3, 4, 6, 2, 7, 1, 5, 8]
quicksort2(arr, 0, len(arr))
print(arr)