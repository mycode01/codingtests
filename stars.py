def solution(v):
    a, b = map(int, v.strip().split(' '))

    for x in range(b):
        print("*"*a)

    return

solution("5 3")
