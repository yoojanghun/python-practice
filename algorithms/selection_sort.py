# Selection Sort = 각 스텝에서 최소값을 찾아 앞에 놓기 반복
#                  각 스텝에서 고려해야 할 배열이 앞에서부터 줄어듦

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):        # 각 스텝
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

arr = [3, 4, 6, 2, 7, 1, 5, 8]
print(selection_sort(arr))