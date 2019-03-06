def solution(S):
    n = int(S,2)
    a = 0

    while True:
        if n == 1 :
            a+=1
            break
        if n % 2 == 0:
            n /= 2
        else :
            n += 1
        a+=1

    return a

print(solution('011100'))