def solution(clothes):
    l = set()
    for x in clothes:
        for y in x:
            l.add(y)

    return len(l)


t1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(t1))
t2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(t2))