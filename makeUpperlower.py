def solution(s):
    answer = ''
    odd = True
    for x in s:
        if x == " ":
            odd = True
        elif odd:
            x =str.upper(x)
            odd = False
        else :
            x = str.lower(x)
            odd = True
        answer = answer + x
    return answer

print(solution("try hello world"))