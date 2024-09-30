def solution(s):
    if len(s) == 1:
        if s == 'z':
            return -1
        else:
            return chr(ord(s)+1)
    res = s[0]
    mark = False
    mark_a = False
    for i in range(1,len(s)):
        print(i)
        print(res)
        if mark:
            if mark_a:
                res = res + 'b'
                mark_a = False
            else:
                res = res + 'a'
                mark_a = True
            continue
        if s[i] != s[i-1]:
            res = res + s[i]

        elif s[i] == s[i-1]:
            if s[i] == 'z':
                return -1
            res = res + chr(ord(s[i])+1)
            mark = True
            continue
        
    return res



res = solution('abccde')
print(res)