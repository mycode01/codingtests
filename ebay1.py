def solution(price, money, count):
    answer = 0
    for x in range(count):
        answer+= price*(x+1)
    return 0 if money - answer > 0 else abs(money - answer)

print(solution(3, 20, 4))