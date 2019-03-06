def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    answer = ""

    try:
        for x in range(0, len(participant)):
            answer = participant[x]
            if participant[x] != completion[x]:
                break
    except:
        pass

    return answer

print(solution({ "leo", "kiki", "eden" },  { "eden", "kiki" }))
print(solution({ "marina", "josipa", "nikola", "vinko", "filipa"},  { "josipa", "filipa", "marina", "nikola"}))
print(solution({ "mislav", "stanko", "mislav", "ana" },  { "stanko", "ana", "mislav"}))