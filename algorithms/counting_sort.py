# Counting Sort = 원소들의 "값의 개수"를 세어서 정렬하는 알고리즘 (비교를 하지 않는 정렬)
#                 정렬할 배열의 "최댓값"을 마지막 인덱스로 하는 count 배열을 준비
#                 각 인덱스(값)에 해당하는 원소가 몇 번 등장했는지 count 배열에 기록
#                 (필요시 누적합을 구해 원소의 정렬된 위치를 계산)

def counting_sort(arr, right):      # right = 배열 최댓값 + 1
    n = len(arr)
    counts = [0] * right            # 마지막 인덱스는 배열의 최댓값

    for x in arr:                   # 인덱스에 해당하는 원소가 몇 번 등장했는지 기록
        counts[x] += 1

    for i in range(1, right):       # 누적합
        counts[i] += counts[i-1]

    sorted = [0] * n
    for x in reversed(arr):         # 각 누적값은 해당 요소가 들어갈 마지막 + 1 위치를 가리킴
        counts[x] -= 1              # 안정 정렬을 위해 뒤에서부터 삽입
        sorted[counts[x]] = x

    arr[:] = sorted

arr = [3, 4, 6, 2, 7, 1, 5, 8]
counting_sort(arr, max(arr)+1)
print(arr)