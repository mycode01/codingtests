def solution(v):
    re_x = []
    re_y = []

    for (x, y) in v:
        if x in re_x :
            re_x.remove(x)
        else :
            re_x.append(x)
        if y in re_y:
            re_y.remove(y)
        else:
            re_y.append(y)

    return re_x+re_y


t1 = [[1, 4], [3, 4], [3, 10]]
print(solution(t1))
t2 = [[1, 1], [2, 2], [1, 2]]
print(solution(t2))