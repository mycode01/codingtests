def solution(x):
    return x%sum([int(z) for z in str(x)]) == 0

print(solution(12))