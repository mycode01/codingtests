def solution(numbers):
    answer = []
    table = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
    sn = [str(x) for x in numbers]
    for x in sn:
        rep = ""
        for z in x:
            rep += " " + table[z]
        answer.append(rep)

    answer.sort()
    ret = []
    for x in answer:
        rep = ""
        for z in x.split(" ") :
            for k, v in table.items():
                if v == z :
                    rep += k
        ret.append(rep)

    return list(map(int, ret))


print(solution([4,5,11]))