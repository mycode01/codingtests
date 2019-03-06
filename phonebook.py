def solution(phone_book):
    for v in phone_book:
        for iv in phone_book:
            if v == iv : continue
            if v.startswith(iv) : return False

    return True

#
# t1 = ["12232332", "12", "222222"]
# print(solution(t1))
# t2 = ["911", "97625999", "91125426"]
# print(solution(t2))
t3 = ["113", "12340", "123440", "12345", "98346"]
print(solution(t3))