# def solution(n):
#     answer = 0
#     for i in range(3,n+1):
#         for x in range(2, i+1):
#             if(i%x) == 0:
#                 if(i == x) :
#                     answer+=1
#                 break;
#
#     return answer+1
def solution(n):
    answer = 0
    l = range(2, n)
    for x in l:
        if x < 4 :continue
        if x % 2 == 0:
            continue
        elif x % 3 == 0:
            continue



    return ""
print(solution(10))