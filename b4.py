def solution(A, X):
    N = len(A) # n은 배열의 크기
    if N == 0:
        return -1  #배열이 비었다면 리턴
    l = 0 #l은 가산자, ++의 역할을 함
    r = N -1 #배열은 0부터 시작하므로 -1해줌,
    while l < r:
        m = (l + r) // 2 #반절 잘라서 해당숫자가 주어진 x보다 큰가 작은가를 비교해서 nlog로 만듬
        if A[m] > X: # 주어진 배열의 절반위치의 숫자가 x보다 크다면
            r = m - 1 # 검색할 배열의 크기를 줄임
        elif l == m :
            l +=1
        else: # 주어진 배열의 절반위치의 숫자가 x보다 작다면
            l = m  #비교 포인터를 줄임
    if A[l] == X:
        return l
    return -1

print(solution([1,2,2,3,4,5,9,9,10,11,12,12], 5))
print(solution([1,2,3,4,5], 5))
print(solution([-200,-120,-1,0,110,120,130,140], 140))