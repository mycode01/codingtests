from string import ascii_lowercase, ascii_uppercase
from itertools import cycle, islice
def solution(s, n):
    lo = cycle(list(ascii_lowercase))
    up = cycle(list(ascii_uppercase))
    answer = ""
    for x in s:
        if 65 <= ord(x) <= 90 : # upper
            while True:
                if next(up) == x:
                    for z in range(n-1):
                        next(up)
                    break
                else :
                    continue
            answer = answer + next(up)
        elif 97<=ord(x)<=122:
            while True:
                if next(lo) == x:
                    for z in range(n - 1):
                        next(lo)
                    break
                else:
                    continue
            answer= answer +  next(lo)
        else:
            answer= answer + x
    return answer

    # a = [ord(x)+n if 65<=(ord(x))<=90 else ord(x)+n if 97<=(ord(x))<=122 else ord(x) for x in s]

# 65 90 97 122

print(solution(	"AB", 1))