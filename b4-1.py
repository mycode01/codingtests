def solution(A, X):
    N = len(A)
    if N == 0:
        return -1
    l = 0
    r = N -1
    while l < r:
        m = (l + r) // 2
        if A[m+1] > X:
            r = m
        else:
            l = m +1
    if A[l] == X:
        return l
    return -1

print(solution([1,2,2,3,4,5,9,9,10,11,12,12], 5))
print(solution([1,2,3,4,5], 5))
print(solution([-200,-120,-1,0,110,120,130,140], 140))