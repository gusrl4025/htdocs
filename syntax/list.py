s = [1, 'four',9 ,16, 25]
print(s)
print(s[1])
#len는 list의 길이
print(len(s))
#element의 교체
s[1] = 4
print(s)
#element의 삭제
del s[2]
print(s)
#element의 추가
#insert는 몇번째 index에 넣을 것인가까지 결정할수 잇음
#append는 무조건 마지막에 추가됨
s.insert(2,9)
print(s)