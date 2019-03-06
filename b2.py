from datetime import datetime
def solution(S):
    l = []
    nc = set()

    t = S.split('\n\n') #한줄씩만든 list

    for x in t:
        splited = x.split(', ') #리스트를 한번 더 파싱함
        m = [x, splited[0], splited[1], datetime.strptime(splited[2], '%Y-%m-%d %H:%M:%S')] #이미지정보
        nc.add(splited[1]) #도시정보 set으로 리스트화
        l.append(m) #이미지 리스트


    ncl = {}
    for x in nc:
        i = 0
        for lx in l :
            if lx[2] == x:
                i+=1
        # ncl.append({x : i})
        ncl[x] = i
    #l의 [2]가 도시정보 [1]파일이름
    for x in l:
        a = x[2] + str(ncl[x[2]]).zfill(len(str(ncl[x[2]])))
        print(a)
        ncl[x[2]] -= 1
        x[1] = a


    print(sorted(l, key=lambda x:x[3]))



    pass


s = """photo.jpg, Warsaw, 2013-09-05 14:08:15\n
john.png, London, 2015-06-20 15:13:22\n
myFriends.png, Warsaw, 2013-09-05 14:07:13\n
Eiffel.jpg, Paris, 2015-07-23 08:03:02\n
pisatower.jpg, Paris, 2015-07-22 23:59:59\n
BOB.jpg, London, 2015-08-05 00:02:03\n
notredame.png, Paris, 2015-09-01 12:00:00\n
me.jpg, Warsaw, 2013-09-06 15:40:22\n
a.png, Warsaw, 2016-02-13 13:33:50\n
b.jpg, Warsaw, 2016-01-02 15:12:22\n
c.jpg, Warsaw, 2016-01-02 14:34:30\n
d.jpg, Warsaw, 2016-01-02 15:15:01\n
e.png, Warsaw, 2016-01-02 09:49:09\n
f.png, Warsaw, 2016-01-02 10:55:32\n
g.jpg, Warsaw, 2016-02-29 22:13:11"""
print(solution(s))