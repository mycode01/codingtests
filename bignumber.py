def solution(numbers):
    numbers = list(map(str, numbers))
    # answer = ''.join(sorted(numbers,key=lambda x:x[0], reverse=True))
    answer = ''.join(sorted(numbers, cmp=comp))
    return answer

def comp(s1, s2):
    for y in s2


print(solution([6,10,2]))
print(solution([3,30,34,5,9])) # 9534330