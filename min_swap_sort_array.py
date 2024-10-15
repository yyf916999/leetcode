
def minSwaps(arr, n):
    temp = arr.copy()
    res = 0
    dic = {}
    temp = sorted(temp)
    for i in range(n):
        dic[arr[i]] = i
    
    init = 0
    for i in range(n):
        if (arr[i] != temp[i]):
            res += 1
            init = arr[i]
            
            arr[i], arr[dic[temp[i]]] = arr[dic[temp[i]]], arr[i]
            
            dic[init] = dic[temp[i]]
            dic[temp[i]] = i
    print(arr)
    return res



a = [101, 758, 315, 730,
     472, 619, 460, 479]
print(minSwaps(a,8))