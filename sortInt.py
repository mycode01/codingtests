def solution(n):
    return int(''.join(sorted([x for x in str(n)], reverse=True)))

print(solution(118372))