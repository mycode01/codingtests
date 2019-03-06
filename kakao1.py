def solution(record):
    answer = []
    revrecord = list(reversed(record))
    ids = list(set([x.split(" ")[1] for x in record]))
    lastidset = {}
    msg = ""
    for x in range(len(revrecord)):
        if revrecord[x].startswith("Enter"):
            # msg = revrecord[x].split(" ")[1]+"님이 들어왔습니다."
            msg = "님이 들어왔습니다."
        elif revrecord[x].startswith("Leave"):
            # msg = revrecord[x].split(" ")[1]+"님이 나갔습니다."
            msg = "님이 나갔습니다."

        # if revrecord[x].split(" ")[1] in ids :
        if lastidset.get(revrecord[x].split(" ")[1]):
            msg = lastidset[revrecord[x].split(" ")[1]]+msg
        else :
            lastidset[revrecord[x].split(" ")[1]] = revrecord[x].split(" ")[2]
        #     lastidset[revrecord[x].split(" ")[1]] = revrecord[x].split(" ")[2]
            if revrecord[x].startswith("Change"):
                continue
            msg = lastidset[revrecord[x].split(" ")[1]] + msg
        answer.append(msg)

    return list(reversed(answer))


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))