import math

def getRank(l):
    scores = []
    for st in l:
        if failcheck(st) :
            scores.append((l.index(st)+1, 0))
            continue
        scores.append((l.index(st)+1, scoring(st)))
    rank = sorted(scores, key=lambda student: student[1], reverse=True)
    return [x[0] for x in rank]

def scoring(s):
    return math.ceil(10 + s.count('A') - (s.count('L') / 2) - s.count('P'))

def failcheck(s):
    return s.count('P') >= 3


s1 = ['AAALLLAPAA', 'AAAAAAAPPP', 'ALAAAAPAAA']
s2 = ['ALALLAAPAA', 'ALLLAAAPAA', 'APAPALLAAA']
print(getRank(s1))
print(getRank(s2))