# Insertion Sort = 정렬되지 않은 배열(오른쪽 배열)의 원소를 정렬된 배열(왼쪽 배열) 값들 사이에 끼워넣기
#                  각 스텝에서 고려해야 할 배열이 앞에서부터 줄어듦
#                  배열이 거의 정렬된 상태일 때 사용하면 매우 효율적

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr

arr = [3, 4, 6, 2, 7, 1, 5, 8]
print(insertion_sort(arr))