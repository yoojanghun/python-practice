# Merge Sort = 배열을 절반으로 나눠서 각각 정렬하고 합침(merge)
#              필요한 divide의 횟수가 logn step으로 감소

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    merged = []
    i = 0
    j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            merged.append(left_arr[i])
            i += 1
        else:
            merged.append(right_arr[i])
            j += 1

    while i < len(left_arr):
        merged.append(left_arr[i])
        i += 1

    while j < len(right_arr):
        merged.append(right_arr[j])
        j += 1

    return merged

arr = [3, 4, 6, 2, 7, 1, 5, 8]
print(merge_sort(arr))