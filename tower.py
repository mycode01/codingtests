def solution(heights):
    answer = []


    while len(heights) > 0:
        t = heights.pop()
        i = len(heights)
        for x in reversed(heights):
            if t < x:
                answer.append(i)
                break
            elif i is 1 :
                answer.append(0)
                break;
            i -= 1
    answer.append(0)
    answer.reverse()
    return answer


print(solution(	[6, 9, 5, 7, 4]))
print(solution([3,9,9,3,5,7,2]	))