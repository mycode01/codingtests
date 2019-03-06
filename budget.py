def solution(d, budget):
    d.sort()
    m = 0
    for x in range(len(d)):
        if m + d[x] > budget:
            return x
        else :
            m+=d[x]
    return len(d)

# def solution(d, budget):
#     answer = 0
#     sorted(d)
#     for x in range(len(d)):
#         budget - d[x]
#         if budget >= 0:
#             answer+=1
#         else :
#             break;
#
#     return answer

print(solution(	[1, 3, 2, 5, 4], 9))