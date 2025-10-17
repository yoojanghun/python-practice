def mergesort(arr, l, r):
    if l + 1 == r:
        return
    m = (l + r) // 2
    mergesort(arr, l, m)
    mergesort(arr, m, r)
    merge(arr, l, m, r)

def merge(arr, l, m, r):
    tmp = arr[l:r]
    i, j = 0, m - l                     # 파라미터 l, m에 각각 -l을 하여 0, m-l로 만듦
    k = l                               # 실제 arr의 index
    while i < m - l and j < r - l:
        if tmp[i] < tmp[j]:
            arr[k] = tmp[i]
            k += 1
            i += 1
        else:
            arr[k] = tmp[j]
            k += 1
            j += 1

    while i < m - l:
        arr[k] = tmp[i]
        i += 1
        k += 1

    while j < r - l:
        arr[k] = tmp[j]
        j += 1
        k += 1

arr = [3, 4, 8, 9, 2, 5, 6, 7]
mergesort(arr, 0, len(arr))
print(arr)