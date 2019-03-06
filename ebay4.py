def solution(plain):
    answer = 0
    l = len(plain)
    for x in range(l):
        if(isPalindrome(plain[:x])):
            return x+l;
    return l<<1;

#
# def isPalindrome(str):
#     l = len(str)
#     half = l >>> 1;
#     for x in range(half+1):
#         if str[x] != str[l-x-1]:
#             return False
#         return True

def isPalindrome(n):
    p = ''
    l = len(n) -1
    for x in range(l, -1, -1):
        r = n[x]
        p = p+r
    if p == n:
        return True
    else :
        return False


print(solution('abab'))