def is_substring(s1, s2):
    sp, ep = 0, 0
    while sp < len(s1):
        if s1[sp + ep] != s2[ep]:
            sp += 1
            ep = 0
            continue
        ep += 1
        if ep == len(s2):
            return True
    return False

a = "12123141231221412312121331"
b = "123"

print(is_substring(a, b))
