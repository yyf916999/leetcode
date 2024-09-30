

import statistics
def solution(arr,n):
    res = 0
    arr = sorted(arr)
    for i in range(n-1):
        res  += arr[-1]
        arr = arr[:-1]
    print(arr)
    res += statistics.median(arr)
    return res
res = solution([89,48,14],3)
print(res)