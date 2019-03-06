from itertools import cycle
def solution(answers):
    n1 = cycle([1,2,3,4,5])
    n2 = cycle([2,1,2,3,2,4,2,5])
    n3 = cycle([3,3,1,1,2,2,4,4,5,5])

    score = [0,0,0]
    for v in answers:
        if v == next(n1):
            score[0]+=1
        if v == next(n2):
            score[1] += 1
        if v == next(n3):
            score[2] += 1
    return [i+1 for i, x in enumerate(score) if x == max(score)]


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
