def solution(skill, skill_trees):
    answer = 0
    t = 100
    for ut in skill_trees:
        l = []
        for s in skill:
            try:
                l.append(ut.index(s))
            except:
                l.append(t)
                t+=1
        if l == sorted(l):
            answer+=1

    return answer

def isCutted(l):
    f = False
    for x in l:
        if x == -1:
            if f :
                return False
            else:
                f = True
        else :
            continue

    return True


print(solution(	"CBD", ["BACDE", "CBADF", "AECB", "BDA","CASGX"]))