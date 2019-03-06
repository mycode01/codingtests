def solution(A, B, M, X, Y):
    t = 0
    w = 0
    r = []

    for x in range(0,len(A)):
        if len(r) == t+1:
            if len(r[t]) == X or w + A[x] > Y:
                t += 1
                w = 0
        if len(r) <= t:
            r.append([])
        r[t].append(B[x])
        w += A[x]

    a = len(r)
    for x in r:
        a += len(list(set(x)))
    return a





print(solution([60, 80, 40], [2, 3, 5], 5, 2, 200))
print(solution([40, 40, 100, 80, 20], [3, 3, 2, 2, 3], 3, 5, 200) )


# A[0], B[0]는 0번째사람의 몸무게(A), 목적층(B)로 구성됨
# 이 순번은 변경되지 않음.
# 엘리베이터가 멈추는 총 횟수는? (몸무게로 결정됨)

# M은 건물의 층수, X는 총가용인원, 중량제한이 Y
# 1층으로 되돌아오는것도 횟수로 포함되어야함