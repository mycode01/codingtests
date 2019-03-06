import heapq
def solution(n):
    answer = []
    primes = getPrimes(n+1)

    heapq.heapify(primes)

    try:
        while True:
            a = heapq.heappop(primes)
            for x in range(len(primes)):
                if n == a * primes[x]:
                    answer.append(a)
                    answer.append(primes[x])
                    break

            if len(answer) > 0:
                break
    except:
        answer = [-1,-1]
    return answer


def getPrimes(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

    return primes

print(solution(12))