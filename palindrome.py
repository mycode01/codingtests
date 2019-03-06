def ispalindrome(inp):
    s = str(inp)
    if len(s)%2 == 0:
        # print(s[:len(s)//2])
        # print(s[len(s)//2:])
        print(s[:len(s)//2] == s[len(s)//2:][::-1])
    else :
        # print(s[:len(s)//2])
        # print(s[len(s)//2:][:0:-1])
        print(s[:len(s) // 2] == s[len(s) // 2:][:0:-1])

def ispalindrome2(inp):
    if inp == int(str(inp)[::-1]):
        print(True)
    else :
        print(False)

ispalindrome(12321)
ispalindrome2(12321)
ispalindrome(21453)
ispalindrome2(21453)