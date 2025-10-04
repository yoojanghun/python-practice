# Bubble Sort: 각 스텝에서 인접한 두 원소를 반복하여 비교 및 교환
#              각 스텝에서 고려해야 할 배열이 뒤에서부터 줄어든다

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):         # 각 스텝
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [3, 4, 6, 2, 7, 1, 5, 8]
print(bubble_sort(arr))