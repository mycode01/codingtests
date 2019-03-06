def solution(a, b):
    args = sorted([a,b])
    answer = 0
    for x in range(args[0],args[1]+1):
        answer+=x

    return answer


print(solution(3,5))
print(solution(3,3))
print(solution(5,3))