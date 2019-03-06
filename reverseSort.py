def solution(n):
    return list(reversed([int(x) for x in str(n)]))

print(solution(123456))