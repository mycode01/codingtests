import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    try:
        while True:
            x = heapq.heappop(scoville)
            if x >= K:
                break
            y = heapq.heappop(scoville)

            answer += 1
            r = x + (y * 2)
            heapq.heappush(scoville, r)
    except:
        answer = -1
    return answer

t1 = [1,2]

print(solution(t1, 3))